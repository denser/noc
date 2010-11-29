# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Abstract script interfaces
##----------------------------------------------------------------------
## Copyright (C) 2007-2009 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
## Python modukes
import re
import types
import datetime
## NOC Modules
from noc.lib.text import list_to_ranges,ranges_to_list,list_to_ranges
from noc.lib.ip import IPv6
from noc.lib.validators import *

try:
    from django import forms
    from noc.lib.forms import NOCForm
except ImportError:
    # No django. Interface.get_form() is meaningless
    pass
##
##
##
class InterfaceTypeError(Exception): pass
##
## Abstract parameter
##
class Parameter(object):
    def __init__(self,required=True,default=None):
        self.required=required
        self.default=None
        if default is not None:
            self.default=self.clean(default)
    ##
    ## Returns ORParameter
    ##
    def __or__(self,other):
        return ORParameter(self,other)
    ##
    ##
    ##
    def raise_error(self,value,msg=""):
        raise InterfaceTypeError("%s: %s. %s"%(self.__class__.__name__,repr(value),msg))
    ##
    ## Perform input parameter normalization
    ##
    def clean(self,value):
        return value
    ##
    ## Clean up script input parameters.
    ## Call .clean() by default
    ##
    def script_clean_input(self,profile,value):
        return self.clean(value)
    ##
    ## Clean up script result
    ## Call .clean() by default
    def script_clean_result(self,profile,value):
        return self.clean(value)
    ##
    ## Perform input parameter normalization for form fields
    ##
    def form_clean(self,value):
        if not value and not self.required:
            return self.default if self.default else None
        try:
            return self.clean(value)
        except InterfaceTypeError,why:
            raise forms.ValidationError(why)
    ##
    ## Returns an form field object
    ##
    def get_form_field(self,label=None):
        return forms.CharField(required=self.required,initial=self.default,label=label)
##
##
##
class ORParameter(Parameter):
    """
    >>> ORParameter(IntParameter(),IPv4Parameter()).clean(10)
    10
    >>> ORParameter(IntParameter(),IPv4Parameter()).clean("192.168.1.1")
    '192.168.1.1'
    >>> ORParameter(IntParameter(),IPv4Parameter()).clean("xxx") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IPv4Parameter: 'xxx'
    >>> (IntParameter()|IPv4Parameter()).clean(10)
    10
    >>> (IntParameter()|IPv4Parameter()).clean("192.168.1.1")
    '192.168.1.1'
    >>> (IntParameter()|IPv4Parameter()).clean("xxx") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IPv4Parameter: 'xxx'
    >>> (IntParameter()|IPv4Parameter()).clean(None) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IPv4Parameter: None.
    >>> (IntParameter(required=False)|IPv4Parameter(required=False)).clean(None)
    >>> (IntParameter(required=False)|IPv4Parameter()).clean(None) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IPv4Parameter: None.
    """
    def __init__(self,left,right):
        super(ORParameter,self).__init__()
        self.left=left
        self.right=right
        self.required=self.left.required or self.right.required
        
    def clean(self,value):
        if value is None and self.required==False:
            return None
        try:
            return self.left.clean(value)
        except InterfaceTypeError:
            return self.right.clean(value)
        
    def script_clean_input(self,profile,value):
        try:
            return self.left.script_clean_input(profile,value)
        except InterfaceTypeError:
            return self.right.script_clean_input(profile,value)
        
    def script_clean_result(self,profile,value):
        try:
            return self.left.script_clean_result(profile,value)
        except InterfaceTypeError:
            return self.right.script_clean_result(profile,value)
##
##
##
class NoneParameter(Parameter):
    """
    >>> NoneParameter().clean(None)
    >>> NoneParameter().clean("None") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: NoneParameter: 'None'
    """
    def __init__(self,required=True):
        super(NoneParameter,self).__init__(required=required)
    def clean(self,value):
        if value is not None:
            self.raise_error(value)
        return value
##
##
##
class StringParameter(Parameter):
    """
    >>> StringParameter().clean("Test")
    'Test'
    >>> StringParameter().clean(10)
    '10'
    >>> StringParameter().clean(None)
    'None'
    >>> StringParameter(default="test").clean("no test")
    'no test'
    >>> StringParameter(default="test").clean(None)
    'test'
    >>> StringParameter(choices=["1","2"]).clean("1")
    '1'
    >>> StringParameter(choices=["1","2"]).clean("3") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: StringParameter: '3'.
    """
    def __init__(self,required=True,default=None,choices=None):
        self.choices=choices
        super(StringParameter,self).__init__(required=required,default=default)
        
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        try:
            value=str(value)
        except:
            self.raise_error(value)
        if self.choices and value not in self.choices:
            self.raise_error(value)
        return value
##
##
##
class REStringParameter(StringParameter):
    """
    >>> REStringParameter("ex+p").clean("exp")
    'exp'
    >>> REStringParameter("ex+p").clean("exxp")
    'exxp'
    >>> REStringParameter("ex+p").clean("regexp 1")
    'regexp 1'
    >>> REStringParameter("ex+p").clean("ex") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: REStringParameter: 'ex'
    >>> REStringParameter("ex+p",default="exxp").clean("regexp 1")
    'regexp 1'
    >>> REStringParameter("ex+p",default="exxp").clean(None)
    'exxp'
    """
    def __init__(self,regexp,required=True,default=None):
        self.rx=re.compile(regexp) # Compile before calling the constructor
        super(REStringParameter,self).__init__(required=required,default=default)

    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        v=super(REStringParameter,self).clean(value)
        if not self.rx.search(v):
            self.raise_error(value)
        return v
##
##
##
class BooleanParameter(Parameter):
    """
    >>> BooleanParameter().clean(True)
    True
    >>> BooleanParameter().clean(False)
    False
    >>> BooleanParameter().clean("True")
    True
    >>> BooleanParameter().clean("yes")
    True
    >>> BooleanParameter().clean(1)
    True
    >>> BooleanParameter().clean(0)
    False
    >>> BooleanParameter().clean([]) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: BooleanParameter: [].
    >>> BooleanParameter(default=False).clean(None)
    False
    >>> BooleanParameter(default=True).clean(None)
    True
    """
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        if type(value)==types.BooleanType:
            return value
        if type(value) in [types.IntType,types.LongType]:
            return value!=0
        if type(value) in [types.StringType,types.UnicodeType]:
            return value.lower() in ["true","t","yes","y"]
        self.raise_error(value)
    ##
    def get_form_field(self,label=None):
        return forms.BooleanField(required=self.required,initial=self.default,label=label)
    
##
##
##
class IntParameter(Parameter):
    """
    >>> IntParameter().clean(1)
    1
    >>> IntParameter().clean("1")
    1
    >>> IntParameter().clean("not a number") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IntParameter: 'not a number'
    >>> IntParameter(min_value=10).clean(5) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IntParameter: 5
    >>> IntParameter(max_value=7).clean(10) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IntParameter: 10
    >>> IntParameter(max_value=10,default=7).clean(5)
    5
    >>> IntParameter(max_value=10,default=7).clean(None)
    7
    >>> IntParameter(max_value=10,default=15) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IntParameter: 15
    """
    def __init__(self,required=True,default=None,min_value=None,max_value=None):
        self.min_value=min_value
        self.max_value=max_value
        super(IntParameter,self).__init__(required=required,default=default)
        
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        try:
            i=int(value)
        except:
            self.raise_error(value)
        if (self.min_value is not None and i<self.min_value) or (self.max_value is not None and i>self.max_value):
            self.raise_error(value)
        return i
##
##
##
class ListParameter(Parameter):
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        try:
            return list(value)
        except:
            self.raise_error(value)
    
    def form_clean(self,value):
        try:
            return self.clean(eval(value,{},{}))
        except:
            self.raise_error(value)
##
##
##
class InstanceOfParameter(Parameter):
    """
    >>> class C: pass
    >>> class X: pass
    >>> class CC(C): pass
    >>> InstanceOfParameter(cls=C).clean(C()) and "Ok"
    'Ok'
    >>> InstanceOfParameter(cls=C).clean(CC()) and "Ok"
    'Ok'
    >>> InstanceOfParameter(cls=C).clean(1) and "Ok" #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: InstanceOfParameter: 1
    >>> InstanceOfParameter(cls="C").clean(C()) and "Ok"
    'Ok'
    >>> InstanceOfParameter(cls="C").clean(1) and "Ok" #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: InstanceOfParameter: 1
    """
    def __init__(self,cls,required=True,default=None):
        super(InstanceOfParameter,self).__init__(required=required,default=default)
        self.cls=cls
        if isinstance(cls,basestring):
            self.is_valid=self.is_valid_classname
        else:
            self.is_valid=self.is_valid_instance
    
    def is_valid_instance(self,value):
        return isinstance(value,self.cls)
    
    def is_valid_classname(self,value):
        return hasattr(value,"__class__") and value.__class__.__name__==self.cls
        
    def clean(self,value):
        if value is None:
            if self.default is not None:
                return self.default
            if not self.required:
                return None
        try:
            if self.is_valid(value):
                return value
        except:
            pass
        self.raise_error(value)
##
##
##
class SubclassOfParameter(Parameter):
    """
    >>> class C: pass
    >>> class C1(C): pass
    >>> class C2(C1): pass
    >>> class C3(C1): pass
    >>> SubclassOfParameter(cls=C).clean(C2) and "Ok"
    'Ok'
    >>> SubclassOfParameter(cls=C).clean(1) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: SubclassOfParameter: 1
    >>> SubclassOfParameter(cls="C").clean(C2) and "Ok"
    'Ok'
    >>> SubclassOfParameter(cls=C).clean(1) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: SubclassOfParameter: 1
    >>> SubclassOfParameter(cls=C2).clean(C3) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: SubclassOfParameter: <class base.C3>
    >>> SubclassOfParameter(cls="C",required=False).clean(None)
    """
    def __init__(self,cls,required=True,default=None):
        super(SubclassOfParameter,self).__init__(required=required,default=default)
        self.cls=cls
        if isinstance(cls,basestring):
            self.is_valid=self.is_valid_classname
        else:
            self.is_valid=self.is_valid_class
    
    def is_valid_classname(self,value):
        def check_name(c,name):
            # Check class name
            if c.__name__==name:
                return True
            # Check base classes name
            for bc in c.__bases__:
                if check_name(bc,name):
                    return True
            #
            return False
        
        return check_name(value,self.cls)
    
    def is_valid_class(self,value):
        return issubclass(value,self.cls)
    
    def clean(self,value):
        if value is None:
            if self.default is not None:
                return self.default
            if not self.required:
                return None
        try:
            if self.is_valid(value):
                return value
        except:
            pass
        self.raise_error(value)
        
##
##
##
class ListOfParameter(ListParameter):
    """
    >>> ListOfParameter(element=IntParameter()).clean([1,2,3])
    [1, 2, 3]
    >>> ListOfParameter(element=IntParameter()).clean([1,2,"3"])
    [1, 2, 3]
    >>> ListOfParameter(element=IntParameter()).clean([1,2,"x"]) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: IntParameter: 'x'
    >>> ListOfParameter(element=StringParameter()).clean([1,2,3,"x"])
    ['1', '2', '3', 'x']
    >>> ListOfParameter(element=StringParameter(),default=[]).clean(None)
    []
    >>> ListOfParameter(element=StringParameter(),default=[1,2,3]).clean(None)
    ['1', '2', '3']
    """
    def __init__(self,element,required=True,default=None):
        self.element=element
        super(ListOfParameter,self).__init__(required=required,default=default)
        
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        v=super(ListOfParameter,self).clean(value)
        return [self.element.clean(x) for x in v]
        
    def script_clean_input(self,profile,value):
        if value is None and self.default is not None:
            return self.default
        v=super(ListOfParameter,self).script_clean_input(profile,value)
        return [self.element.script_clean_input(profile,x) for x in v]

    def script_clean_result(self,profile,value):
        if value is None and self.default is not None:
            return self.default
        v=super(ListOfParameter,self).script_clean_result(profile,value)
        return [self.element.script_clean_result(profile,x) for x in v]

##
##
##
class StringListParameter(ListOfParameter):
    """
    >>> StringListParameter().clean(["1","2","3"])
    ['1', '2', '3']
    >>> StringListParameter().clean(["1",2,"3"])
    ['1', '2', '3']
    """
    def __init__(self,required=True,default=None):
        super(StringListParameter,self).__init__(element=StringParameter(),required=required,default=default)
##
##
##
class DictParameter(Parameter):
    """
    >>> DictParameter(attrs={"i":IntParameter(),"s":StringParameter()}).clean({"i":10,"s":"ten"})
    {'i': 10, 's': 'ten'}
    >>> DictParameter(attrs={"i":IntParameter(),"s":StringParameter()}).clean({"i":"10","x":"ten"}) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: DictParameter: {'i': '10', 'x': 'ten'}
    """
    def __init__(self,required=True,default=None,attrs=None):
        super(DictParameter,self).__init__(required=required,default=default)
        self.attrs=attrs
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        if type(value)!=types.DictType:
            self.raise_error(value)
        if not self.attrs:
            return value
        in_value=value.copy()
        out_value={}
        for a_name,attr in self.attrs.items():
            if a_name not in in_value and attr.required:
                self.raise_error(value,"Attribute '%s' is required in %s"%(a_name,in_value))
            if a_name in in_value:
                try:
                    out_value[a_name]=attr.clean(in_value[a_name])
                except InterfaceTypeError, why:
                    self.raise_error(value,"Invalid value for '%s': %s"%(a_name,why))
                del in_value[a_name]
        for k,v in in_value.items():
            out_value[k]=v
        return out_value
        
    def script_clean_input(self,profile,value):
        if value is None and self.default is not None:
            return self.default
        if type(value)!=types.DictType:
            self.raise_error(value)
        if not self.attrs:
            return value
        in_value=value.copy()
        out_value={}
        for a_name,attr in self.attrs.items():
            if a_name not in in_value and attr.required:
                self.raise_error(value,"Attribute '%s' required"%a_name)
            if a_name in in_value:
                try:
                    out_value[a_name]=attr.script_clean_input(profile,in_value[a_name])
                except InterfaceTypeError:
                    self.raise_error(value,"Invalid value for '%s'"%a_name)
                del in_value[a_name]
        for k,v in in_value.items():
            out_value[k]=v
        return out_value
        
    def script_clean_result(self,profile,value):
        if value is None and self.default is not None:
            return self.default
        if type(value)!=types.DictType:
            self.raise_error(value)
        if not self.attrs:
            return value
        in_value=value.copy()
        out_value={}
        for a_name,attr in self.attrs.items():
            if a_name not in in_value and attr.required:
                self.raise_error(value,"Attribute '%s' required"%a_name)
            if a_name in in_value:
                try:
                    out_value[a_name]=attr.script_clean_result(profile,in_value[a_name])
                except InterfaceTypeError,why:
                    self.raise_error(value,"Invalid value for '%s': %s"%(a_name,str(why)))
                del in_value[a_name]
        for k,v in in_value.items():
            out_value[k]=v
        return out_value

##
##
##
rx_datetime=re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?$")
class DateTimeParameter(StringParameter):
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        if isinstance(value,datetime.datetime):
            return value.isoformat()
        if value.lower()=="infinite":
            return datetime.datetime(year=datetime.MAXYEAR,month=1,day=1)
        if rx_datetime.match(value):
            return value
        self.raise_error(value)
##
##
##
class IPv4Parameter(StringParameter):
    """
    >>> IPv4Parameter().clean("192.168.0.1")
    '192.168.0.1'
    >>> IPv4Parameter().clean("192.168.0.256") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IPvParameter: '192.168.0.256'
    """
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        v=super(IPv4Parameter,self).clean(value)
        X=v.split(".")
        if len(X)!=4:
            self.raise_error(value)
        try:
            if len([x for x in X if 0<=int(x)<=255])!=4:
                self.raise_error(value)
        except:
            self.raise_error(value)
        return v
##
##
##
class IPv4PrefixParameter(StringParameter):
    """
    >>> IPv4PrefixParameter().clean("192.168.0.0/16")
    '192.168.0.0/16'
    >>> IPv4PrefixParameter().clean("192.168.0.256") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IPv4PrefixParameter: '192.168.0.256'
    >>> IPv4PrefixParameter().clean("192.168.0.0/33") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IPv4PrefixParameter: '192.168.0.0/33'
    >>> IPv4PrefixParameter().clean("192.168.0.0/-5") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: IPv4PrefixParameter: '192.168.0.0/-5'
    """
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        v=super(IPv4PrefixParameter,self).clean(value)
        if "/" not in v:
            self.raise_error(value)
        n,m=v.split("/",1)
        try:
            m=int(m)
        except:
            self.raise_error(value)
        if m<0 or m>32:
            self.raise_error(value)
        X=n.split(".")
        if len(X)!=4:
            self.raise_error(value)
        try:
            if len([x for x in X if 0<=int(x)<=255])!=4:
                self.raise_error(value)
        except:
            self.raise_error(value)
        return v
    

##
## IPv6 Parameter
##
class IPv6Parameter(StringParameter):
    """
    >>> IPv6Parameter().clean("::")
    '::'
    >>> IPv6Parameter().clean("::1")
    '::1'
    >>> IPv6Parameter().clean("2001:db8::1")
    '2001:db8::1'
    >>> IPv6Parameter().clean("2001:db8::")
    '2001:db8::'
    >>> IPv6Parameter().clean("::ffff:192.168.0.1")
    '::ffff:192.168.0.1'
    >>> IPv6Parameter().clean('g::')  #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: IPv6Parameter: 'g::'.
    >>> IPv6Parameter().clean("0:00:0:0:0::1")
    '::1'
    >>> IPv6Parameter().clean("::ffff:c0a8:1")
    '::ffff:192.168.0.1'
    >>> IPv6Parameter().clean("2001:db8:0:7:0:0:0:1")
    '2001:db8:0:7::1'
    """
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        v=super(IPv6Parameter,self).clean(value)
        if not is_ipv6(v):
            self.raise_error(value)
        return IPv6(v).normalized.address
    

##
##
##
class IPv6PrefixParameter(StringParameter):
    """
    >>> IPv6PrefixParameter().clean("::/128")
    '::/128'
    >>> IPv6PrefixParameter().clean("2001:db8::/32")
    '2001:db8::/32'
    >>> IPv6PrefixParameter().clean("2001:db8::/129") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: IPv6PrefixParameter: '2001:db8::/129'
    >>> IPv6PrefixParameter().clean("2001:db8::/g") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: IPv6PrefixParameter: '2001:db8::/g'
    >>> IPv6PrefixParameter().clean("2001:db8::") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    InterfaceTypeError: IPv6PrefixParameter: '2001:db8::'
    """
    def clean(self, value):
        if value is None and self.default is not None:
            return self.default
        v=super(IPv6PrefixParameter,self).clean(value)
        if "/" not in v:
            self.raise_error(value)
        n,m=v.split("/",1)
        try:
            m=int(m)
        except:
            self.raise_error(value)
        if m<0 or m>128:
            self.raise_error(value)
        n=IPv6Parameter().clean(n)
        return "%s/%d"%(n,m)
    

##
## IPv4/IPv6 parameter
##
class IPParameter(StringParameter):
    def clean(self,value):
        """
        >>> IPParameter().clean("192.168.0.1")
        '192.168.0.1'
        >>> IPParameter().clean("::")
        '::'
        """
        if ":" in value:
            return IPv6Parameter().clean(value)
        else:
            return IPv4Parameter().clean(value)
    

##
##
##
class VLANIDParameter(IntParameter):
    """
    >>> VLANIDParameter().clean(10)
    10
    >>> VLANIDParameter().clean(5000) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: VLANIDParameter: 5000
    >>> VLANIDParameter().clean(0) #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: VLANIDParameter: 0
    """
    def __init__(self,required=True,default=None):
        super(VLANIDParameter,self).__init__(required=required,default=default,min_value=1,max_value=4095)

##
##
##
class VLANIDListParameter(ListOfParameter):
    """
    >>> VLANIDListParameter().clean(["1","2","3"])
    [1, 2, 3]
    >>> VLANIDListParameter().clean([1,2,3])
    [1, 2, 3]
    """
    def __init__(self,required=True,default=None):
        super(VLANIDListParameter,self).__init__(element=VLANIDParameter(),required=required,default=default)

##
##
##
class VLANIDMapParameter(StringParameter):
    def clean(self,value):
        """
        >>> VLANIDMapParameter().clean("1,2,5-10")
        '1-2,5-10'
        """
        vp=VLANIDParameter()
        try:
            return list_to_ranges([vp.clean(v) for v in ranges_to_list(value)])
        except SyntaxError:
            self.raise_error(value)
##
##
##
rx_mac_address_cisco=re.compile(r"^[0-9A-F]{4}(?P<sep>[.\-])[0-9A-F]{4}(?P=sep)[0-9A-F]{4}$")
rx_mac_address_cisco_media=re.compile("^01[0-9A-F]{2}\.[0-9A-F]{4}\.[0-9A-F]{4}\.[0-9A-F]{2}$")
rx_mac_address_sixblock=re.compile("^([0-9A-F]{1,2}):([0-9A-F]{1,2}):([0-9A-F]{1,2}):([0-9A-F]{1,2}):([0-9A-F]{1,2}):([0-9A-F]{1,2})$")
rx_mac_address_hp=re.compile("^[0-9A-F]{6}-[0-9A-F]{6}$")
class MACAddressParameter(StringParameter):
    """
    >>> MACAddressParameter().clean("1234.5678.9ABC")
    '12:34:56:78:9A:BC'
    >>> MACAddressParameter().clean("1234.5678.9abc")
    '12:34:56:78:9A:BC'
    >>> MACAddressParameter().clean("0112.3456.789a.bc")
    '12:34:56:78:9A:BC'
    >>> MACAddressParameter().clean("1234.5678.9abc.def0") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: MACAddressParameter: '1234.5678.9ABC.DEF0'
    >>> MACAddressParameter().clean("12:34:56:78:9A:BC")
    '12:34:56:78:9A:BC'
    >>> MACAddressParameter().clean("12-34-56-78-9A-BC")
    '12:34:56:78:9A:BC'
    >>> MACAddressParameter().clean("0:13:46:50:87:5")
    '00:13:46:50:87:05'
    >>> MACAddressParameter().clean("123456-789abc")
    '12:34:56:78:9A:BC'
    >>> MACAddressParameter().clean("12-34-56-78-9A-BC-DE") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: MACAddressParameter: '12:34:56:78:9A:BC:DE'
    >>> MACAddressParameter().clean("AB-CD-EF-GH-HJ-KL") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    InterfaceTypeError: MACAddressParameter: 'AB:CD:EF:GH:HJ:KL'
    >>> MACAddressParameter().clean("aabb-ccdd-eeff")
    'AA:BB:CC:DD:EE:FF'
    """
    def clean(self,value):
        if value is None and self.default is not None:
            return self.default
        value=super(MACAddressParameter,self).clean(value)
        value=value.upper()
        match=rx_mac_address_cisco_media.match(value)
        if match:
            value=value.replace(".","")[2:]
            return "%s:%s:%s:%s:%s:%s"%(value[:2],value[2:4],value[4:6],value[6:8],value[8:10],value[10:])
        match=rx_mac_address_cisco.match(value)
        if match:
            value=value.replace(".","").replace("-","")
        else:
            match=rx_mac_address_hp.match(value)
            if match:
                value=value.replace("-","")
            else:
                value=value.replace("-",":")
                match=rx_mac_address_sixblock.match(value)
                if not match:
                    self.raise_error(value)
                value=""
                for i in range(1,7):
                    v=match.group(i)
                    if len(v)==1:
                        v="0"+v
                    value+=v
        return "%s:%s:%s:%s:%s:%s"%(value[:2],value[2:4],value[4:6],value[6:8],value[8:10],value[10:])
##
class InterfaceNameParameter(StringParameter):
    def script_clean_input(self,profile,value):
        return profile.convert_interface_name(value)
        
    def script_clean_result(self,profile,value):
        return self.script_clean_input(profile,value)


## Stub for interface registry
interface_registry={}

class InterfaceBase(type):
    def __new__(cls,name,bases,attrs):
        m=type.__new__(cls,name,bases,attrs)
        interface_registry[name]=m
        return m
##
##
##
class Interface(object):
    __metaclass__=InterfaceBase
    ##
    ## Generator returning (parameter name, parameter instance) pairs
    ##
    def gen_parameters(self):
        for n,p in self.__class__.__dict__.items():
            if issubclass(p.__class__,Parameter) and n!="returns":
                yield (n,p)
    ##
    ## Clean up all parameters except "returns"
    ##
    def clean(self,__profile=None,**kwargs):
        in_kwargs=kwargs.copy()
        out_kwargs={}
        for n,p in self.gen_parameters():
            if n not in in_kwargs and p.required:
                if p.default is not None:
                    out_kwargs[n]=p.default
                else:
                    raise InterfaceTypeError("Parameter '%s' required"%n)
            if n in in_kwargs:
                if not (in_kwargs[n] is None and not p.required):
                    try:
                        if __profile:
                            out_kwargs[n]=p.script_clean_input(__profile,in_kwargs[n])
                        else:
                            out_kwargs[n]=p.clean(in_kwargs[n])
                    except InterfaceTypeError,why:
                        raise InterfaceTypeError("Invalid value for '%s': %s"%(n,why))
                del in_kwargs[n]
        # Copy other parameters
        for k,v in in_kwargs.items():
            if k!="__profile":
                out_kwargs[k]=v
        return out_kwargs
    ##
    ## Clean up returned result
    ##
    def clean_result(self,result):
        try:
            rp=self.returns
        except AttributeError:
            return result # No return result restriction
        return rp.clean(result)
    ##
    ## Clean up script input
    ##
    def script_clean_input(self,__profile,**kwargs):
        return self.clean(__profile=__profile,**kwargs)
    ##
    def script_clean_result(self,__profile,result):
        try:
            rp=self.returns
        except AttributeError:
            return result
        return rp.script_clean_result(__profile,result)
    ##
    def requires_input(self):
        for n,p in self.gen_parameters():
            return True
        return False
        
    def get_form(self,data=None):
        def get_clean_field_wrapper(form,name,param):
            def clean_field_wrapper(form,name,param):
                data=form.cleaned_data[name]
                if not param.required and not data:
                    return None
                try:
                    return param.form_clean(data)
                except InterfaceTypeError:
                    raise forms.ValidationError("Invalid value")
            return lambda: clean_field_wrapper(form,name,param)
        f=NOCForm(data)
        for n,p in self.gen_parameters():
            f.fields[n]=p.get_form_field(n)
            setattr(f,"clean_%s"%n,get_clean_field_wrapper(f,n,p))
        return f
##
## Module Test
##
if __name__ == "__main__":
    import doctest
    doctest.testmod()
