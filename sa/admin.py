# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Copyright (C) 2007-2009 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
from django.contrib import admin
from django import forms
from models import *
from noc.lib.fileutils import in_dir
from noc.settings import config
import os

class ActivatorAdmin(admin.ModelAdmin):
    list_display=["name","ip","is_active"]
    
class TaskScheduleAdmin(admin.ModelAdmin):
    list_display=["periodic_name","is_enabled","run_every","timeout","retries","retry_delay","next_run","retries_left"]

class AdministrativeDomainAdmin(admin.ModelAdmin):
    list_display=["name","description"]
    search_fields=["name","description"]

class ObjectGroupAdmin(admin.ModelAdmin):
    list_display=["name","description"]
    search_fields=["name","description"]

class ManagedObjectAdminForm(forms.ModelForm):
    class Meta:
        model=ManagedObject
    def clean_scheme(self):
        if "profile_name" not in self.cleaned_data:
            return self.cleaned_data["scheme"]
        profile=profile_registry[self.cleaned_data["profile_name"]]
        if self.cleaned_data["scheme"] not in profile.supported_schemes:
            raise forms.ValidationError("Selected scheme is not supported for profile '%s'"%self.cleaned_data["profile_name"])
        return self.cleaned_data["scheme"]
    # Check repo_path remains inside repo
    def clean_repo_path(self):
        repo=os.path.join(config.get("cm","repo"),"config")
        if not in_dir(os.path.join(repo,self.cleaned_data["repo_path"]),repo) or self.cleaned_data["repo_path"].startswith(os.sep):
            raise forms.ValidationError("Repo path must be relative path inside repo")
        return os.path.normpath(self.cleaned_data["repo_path"])
        
class ManagedObjectAdmin(admin.ModelAdmin):
    form=ManagedObjectAdminForm
    fieldsets=(
        (None,{
            "fields": ("name","is_managed","administrative_domain","activator","profile_name","description")
        }),
        ("Access",{
            "fields": ("scheme","address","port","remote_path")
        }),
        ("Credentials",{
            "fields": ("user","password","super_password")
        }),
        ("SNMP",{
            "fields": ("snmp_ro","snmp_rw","trap_source_ip","trap_community")
        }),
        ("CM",{
            "fields": ("is_configuration_managed","repo_path")
        }),
        ("Groups", {
            "fields": ("groups",)
        }),
    )
    list_display=["name","is_managed","profile_name","address","administrative_domain","activator","is_configuration_managed","description","repo_path","action_links"]
    list_filter=["is_managed","is_configuration_managed","activator","administrative_domain","groups","profile_name"]
    search_fields=["name","address","repo_path","description"]
    object_class=ManagedObject
    ##
    ## Dirty hack to display PasswordInput in admin form
    ##
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ["password","super_password"]:
            kwargs["widget"]=forms.widgets.PasswordInput
            return db_field.formfield(**kwargs)
        return super(ManagedObjectAdmin,self).formfield_for_dbfield(db_field,**kwargs)
    ##
    ## Row-level access control
    ##
    def has_change_permission(self,request,obj=None):
        if obj:
            return obj.has_access(request.user)
        else:
            return admin.ModelAdmin.has_delete_permission(self,request)
            
    def has_delete_permission(self,request,obj=None):
        return self.has_change_permission(request,obj)
        
    def queryset(self,request):
        return ManagedObject.queryset(request.user)
        
    def save_model(self, request, obj, form, change):
        if obj.can_change(request.user,form.cleaned_data["administrative_domain"],form.cleaned_data["groups"]):
            admin.ModelAdmin.save_model(self,request,obj,form,change)
        else:
            raise "Permission denied"

class UserAccessAdmin(admin.ModelAdmin):
    list_display=["user","administrative_domain","group"]
    list_filter=["user","administrative_domain","group"]

admin.site.register(Activator,            ActivatorAdmin)
admin.site.register(AdministrativeDomain, AdministrativeDomainAdmin)
admin.site.register(ObjectGroup,          ObjectGroupAdmin)
admin.site.register(ManagedObject,        ManagedObjectAdmin)
admin.site.register(UserAccess,           UserAccessAdmin)
admin.site.register(TaskSchedule,         TaskScheduleAdmin)
