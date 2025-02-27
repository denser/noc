//---------------------------------------------------------------------
// main.label Model
//---------------------------------------------------------------------
// Copyright (C) 2007-2021 The NOC Project
// See LICENSE for details
//---------------------------------------------------------------------
console.debug("Defining NOC.main.label.Model");

Ext.define("NOC.main.label.Model", {
    extend: "Ext.data.Model",
    rest_url: "/main/label/",

    fields: [
        {
            name: "id",
            type: "string"
        },
        {
            name: "name",
            type: "string"
        },
        {
            name: "description",
            type: "string"
        },
        {
            name: "bg_color1",
            type: "int"
        },
        {
            name: "fg_color1",
            type: "int",
            defaultValue: 16777215
        },
        {
            name: "bg_color2",
            type: "int"
        },
        {
            name: "fg_color2",
            type: "int",
            defaultValue: 16777215
        },
        {
            name: "display_order",
            type: "int",
            defaultValue: 0
        },
        {
            name: "is_protected",
            type: "boolean"
        },
        {
            name: "propagate",
            type: "boolean"
        },
        {
            name: "is_matching",
            type: "boolean"
        },
        {
            name: "is_builtin",
            type: "boolean",
            persist: false
        },
        {
            name: "is_matched",
            type: "boolean",
            persist: false
        },
        {
            name: "is_wildcard",
            type: "boolean",
            persist: false
        },
        {
            name: "is_scoped",
            type: "boolean",
            persist: false
        },
        {
            name: "is_autogenerated",
            type: "boolean",
            persist: false
        },
        {
            name: "enable_agent",
            type: "boolean"
        },
        {
            name: "enable_service",
            type: "boolean"
        },
        {
            name: "enable_serviceprofile",
            type: "boolean"
        },
        {
            name: "enable_managedobject",
            type: "boolean"
        },
        {
            name: "enable_managedobjectprofile",
            type: "boolean"
        },
        {
            name: "enable_administrativedomain",
            type: "boolean"
        },
        {
            name: "enable_firmwarepolicy",
            type: "boolean"
        },
        {
          name: "enable_alarm",
          type: "boolean"
        },
        {
            name: "enable_authprofile",
            type: "boolean"
        },
        {
            name: "enable_commandsnippet",
            type: "boolean"
        },
        {
            name: "enable_allocationgroup",
            type: "boolean"
        },
        {
            name: "enable_networksegment",
            type: "boolean"
        },
        {
            name: "enable_object",
            type: "boolean"
        },
        {
            name: "enable_objectmodel",
            type: "boolean"
        },
        {
            name: "enable_platform",
            type: "boolean"
        },
        {
            name: "enable_resourcegroup",
            type: "boolean"
        },
        {
            name: "enable_sensor",
            type: "boolean"
        },
        {
            name: "enable_sensorprofile",
            type: "boolean"
        },
        {
            name: "enable_interface",
            type: "boolean"
        },
        {
            name: "enable_subscriber",
            type: "boolean"
        },
        {
            name: "enable_subscriberprofile",
            type: "boolean"
        },
        {
            name: "enable_supplier",
            type: "boolean"
        },
        {
            name: "enable_supplierprofile",
            type: "boolean"
        },
        {
            name: "enable_dnszone",
            type: "boolean"
        },
        {
            name: "enable_dnszonerecord",
            type: "boolean"
        },
        {
            name: "enable_division",
            type: "boolean"
        },
        {
            name: "enable_kbentry",
            type: "boolean"
        },
        {
            name: "enable_ipaddress",
            type: "boolean"
        },
        {
            name: "enable_addressprofile",
            type: "boolean"
        },
        {
            name: "enable_ipaddressrange",
            type: "boolean"
        },
        {
            name: "enable_ipprefix",
            type: "boolean"
        },
        {
            name: "enable_prefixprofile",
            type: "boolean"
        },
        {
            name: "enable_vrf",
            type: "boolean"
        },
        {
            name: "enable_vrfgroup",
            type: "boolean"
        },
        {
            name: "enable_asn",
            type: "boolean"
        },
        {
            name: "enable_assetpeer",
            type: "boolean"
        },
        {
            name: "enable_peer",
            type: "boolean"
        },
        {
            name: "enable_vc",
            type: "boolean"
        },
        {
            name: "enable_vlan",
            type: "boolean"
        },
        {
            name: "enable_vlanprofile",
            type: "boolean"
        },
        {
            name: "enable_vpn",
            type: "boolean"
        },
        {
            name: "enable_vpnprofile",
            type: "boolean"
        },
        {
            name: "enable_slaprobe",
            type: "boolean"
        },
        {
            name: "enable_slaprofile",
            type: "boolean"
        },
        {
            name: "enable_workflowstate",
            type: "boolean"
        },
        {
            name: "expose_metric",
            type: "boolean"
        },
        {
            name: "expose_datastream",
            type: "boolean"
        },
        {
            name: "expose_alarm",
            type: "boolean"
        },
        {
            name: "remote_system",
            type: "string"
        },
        {
            name: "remote_id",
            type: "string"
        },
        {
            name: "match_regex",
            type: "auto"
        },
        {
            name: "match_vlanfilter",
            type: "auto"
        },
        {
            name: "match_prefixfilter",
            type: "auto"
        },
    ]
});