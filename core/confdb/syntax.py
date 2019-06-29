# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# Normalized config syntax
# ----------------------------------------------------------------------
# Copyright (C) 2007-2019 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
from collections import namedtuple
# NOC modules
from .patterns import (ANY, HHMM, INTEGER, IF_NAME, BOOL, ETHER_MODE, FLOAT, CHOICES, VR_NAME,
                       FI_NAME, IPv4_PREFIX, IPv6_PREFIX, UNIT_NAME, IPv4_ADDRESS, IPv6_ADDRESS,
                       IP_ADDRESS, ISO_ADDRESS)


SyntaxDef = namedtuple("SyntaxDef", ["token", "children", "required", "name", "multi", "default", "gen"])


def DEF(token, children=None, required=False, multi=False, name=None, default=None, gen=None):
    return SyntaxDef(token, children, required, name, multi, default, gen)


SYNTAX = [
    DEF("system", [
        DEF("hostname", [
            DEF(ANY, required=True, name="hostname", gen="make_hostname")
        ]),
        DEF("domain-name", [
            DEF(ANY, required=True, name="domain_name", gen="make_domain_name")
        ]),
        DEF("prompt", [
            DEF(ANY, required=True, name="prompt", gen="make_prompt")
        ]),
        DEF("clock", [
            DEF("timezone", [
                DEF(ANY, [
                    DEF("offset", [
                        DEF(HHMM, required=True, name="tz_offset", gen="make_tz_offset")
                    ])
                ], required=True, name="tz_name", gen="make_tz")
            ], required=True)
        ]),
        DEF("user", [
            DEF(ANY, [
                DEF("uid", [
                    DEF(INTEGER, required=True, name="uid", gen="make_user_uid")
                ]),
                DEF("full-name", [
                    DEF(ANY, required=True, name="full_name", gen="make_user_full_name")
                ]),
                # enable level 15 should be encoded as `level-15`
                DEF("class", [
                    DEF(ANY, required=True, multi=True, name="class_name", gen="make_user_class")
                ]),
                DEF("authentication", [
                    DEF("encrypted-password", [
                        DEF(ANY, required=True, name="password", gen="make_user_encrypted_password")
                    ]),
                    DEF("ssh-rsa", [
                        DEF(ANY, required=True, multi=True, name="rsa", gen="make_user_ssh_rsa")
                    ]),
                    DEF("ssh-dsa", [
                        DEF(ANY, required=True, multi=True, name="dsa", gen="make_user_ssh_dsa")
                    ])
                ])
            ], multi=True, name="username")
        ])
    ]),
    DEF("interfaces", [
        DEF(IF_NAME, [
            DEF("type", [
                DEF(CHOICES("physical", "SVI", "aggregated", "loopback", "management",
                            "null", "tunnel", "other", "template", "dry", "unknown"),
                    required=True, name="type", gen="make_interface_type")
            ]),
            DEF("description", [
                DEF(ANY, required=True, name="description", gen="make_interface_description")
            ]),
            DEF("admin-status", [
                DEF(BOOL, required=True, name="admin_status", gen="make_interface_admin_status")
            ]),
            DEF("mtu", [
                DEF(INTEGER, required=True, name="mtu", gen="make_interface_mtu")
            ]),
            DEF("speed", [
                DEF(INTEGER, required=True, name="speed", gen="make_interface_speed")
            ]),
            DEF("duplex", [
                DEF(BOOL, required=True, name="duplex", gen="make_interface_duplex")
            ]),
            DEF("flow-control", [
                DEF(BOOL, required=True, name="flow_control", gen="make_interface_flow_control")
            ]),
            DEF("ethernet", [
                DEF("auto-negotiation", [
                    DEF(ETHER_MODE, multi=True, name="mode", gen="make_interface_ethernet_autonegotiation")
                ])
            ]),
            DEF("storm-control", [
                DEF("broadcast", [
                    DEF("level", [
                        DEF(FLOAT, required=True, name="level", gen="make_interface_storm_control_broadcast_level")
                    ])
                ]),
                DEF("multicast", [
                    DEF("level", [
                        DEF(FLOAT, required=True, name="level", gen="make_interface_storm_control_multicast_level")
                    ])
                ]),
                DEF("unicast", [
                    DEF("level", [
                        DEF(FLOAT, required=True, name="level", gen="make_interface_storm_control_unicast_level")
                    ])
                ])
            ])
        ], multi=True, name="interface", gen="make_interface")
    ]),
    DEF("protocols", [
        DEF("cdp", [
            DEF("interface", [
                DEF(IF_NAME, multi=True, name="interface", gen="make_cdp_interface")
            ])
        ]),
        DEF("lldp", [
            DEF("interface", [
                DEF(IF_NAME, [
                    DEF("admin-status", [
                        DEF("rx", gen="make_lldp_admin_status_rx"),
                        DEF("tx", gen="make_lldp_admin_status_tx")
                    ])
                ], multi=True, name="interface", gen="make_lldp_interface")
            ])
        ]),
        DEF("udld", [
            DEF("interface", [
                DEF(IF_NAME, multi=True, name="interface", gen="make_udld_interface")
            ])
        ]),
        DEF("spanning-tree", [
            DEF("mode", [
                DEF(CHOICES("stp", "rstp", "mstp", "pvst", "rapid-pvst"), required=True,
                    name="mode", gen="make_spanning_tree_mode")
            ]),
            DEF("priority", [
                DEF(INTEGER, name="priority", required=True, gen="make_spanning_tree_priority")
            ]),
            DEF("instance", [
                DEF(INTEGER, [
                    DEF("bridge-priority", [
                        DEF(INTEGER, required=True,
                            name="priority", gen="make_spanning_tree_instance_bridge_priority")
                    ])
                ], multi=True, name="instance", default="0")
            ]),
            DEF("interface", [
                DEF(IF_NAME, [
                    DEF("admin-status", [
                        DEF(BOOL, required=True, name="admin_status", gen="make_interface_spanning_tree_admin_status")
                    ]),
                    DEF("cost", [
                        DEF(INTEGER, required=True,
                            name="cost", gen="make_spanning_tree_interface_cost")
                    ]),
                    DEF("bpdu-filter", [
                        DEF(BOOL, required=True, name="enabled", gen="make_spanning_tree_interface_bpdu_filter")
                    ]),
                    DEF("bpdu-guard", [
                        DEF(BOOL, required=True, name="enabled", gen="make_spanning_tree_interface_bpdu_guard")
                    ]),
                    DEF("mode", [
                        DEF(CHOICES("normal", "portfast", "portfast-trunk"), required=True,
                            name="mode", gen="make_spanning_tree_interface_mode")
                    ])
                ], multi=True, name="interface"),
            ])
        ]),
        DEF("loop-detect", [
            DEF("interface", [
                DEF(IF_NAME, multi=True, name="interface", gen="make_loop_detect_interface")
            ])
        ])
    ]),
    DEF("virtual-router", [
        DEF(VR_NAME, [
            DEF("forwarding-instance", [
                DEF(FI_NAME, [
                    DEF("type", [
                        DEF(CHOICES("table", "vrf", "vpls"), required=True, name="type",
                            gen="make_forwarding_instance_type")
                    ]),
                    DEF("description", [
                        DEF(ANY, required=False, name="description", gen="make_forwarding_instance_description")
                    ]),
                    DEF("route-distinguisher", [
                        DEF(ANY, required=True, name="rd", gen="make_forwarding_instance_rd")
                    ]),
                    DEF("vrf-target", [
                        DEF("import", [
                            DEF(ANY, multi=True, name="target", gen="make_forwarding_instance_import_target")
                        ]),
                        DEF("export", [
                            DEF(ANY, multi=True, name="target", gen="make_forwarding_instance_export_target")
                        ])
                    ]),
                    DEF("vpn-id", [
                        DEF(ANY, required=True, name="vpn_id", gen="make_forwarding_instance_vpn_id")
                    ]),
                    DEF("vlans", [
                        DEF(INTEGER, [
                            DEF("name", [
                                DEF(ANY, required=True, name="name", gen="make_vlan_name")
                            ]),
                            DEF("description", [
                                DEF(ANY, required=True, name="description", gen="make_vlan_description")
                            ])
                        ], multi=True, name="vlan_id", gen="make_vlan_id")
                    ]),
                    DEF("interfaces", [
                        DEF(IF_NAME, [
                            DEF("unit", [
                                DEF(UNIT_NAME, [
                                    DEF("description", [
                                        DEF(ANY, required=True, name="description", gen="make_unit_description")
                                    ]),
                                    DEF("inet", [
                                        DEF("address", [
                                            DEF(IPv4_PREFIX, multi=True, name="address", gen="make_unit_inet_address")
                                        ])
                                    ]),
                                    DEF("inet6", [
                                        DEF("address", [
                                            DEF(IPv6_PREFIX, multi=True, name="address", gen="make_unit_inet6_address")
                                        ])
                                    ]),
                                    DEF("iso", gen="make_unit_iso"),
                                    DEF("mpls", gen="make_unit_mpls"),
                                    DEF("bridge", [
                                        DEF("switchport", [
                                            DEF("untagged", [
                                                DEF(ANY, required=True, multi=True,
                                                    name="vlan_filter", gen="make_switchport_untagged")
                                            ]),
                                            DEF("native", [
                                                DEF(ANY, required=True,
                                                    name="vlan_id", gen="make_switchport_native")
                                            ]),
                                            DEF("tagged", [
                                                DEF(ANY, required=True, multi=True,
                                                    name="vlan_filter", gen="make_switchport_tagged")
                                            ])
                                        ]),
                                        DEF("port-security", [
                                            DEF("max-mac-count", [
                                                DEF(INTEGER, required=True,
                                                    name="limit", gen="make_unit_port_security_max_mac")
                                            ])
                                        ]),
                                        DEF("input_vlan_map", [
                                            DEF("stack", [
                                                DEF(CHOICES("0", "1", "2"), required=True, default="0",
                                                    name="stack", gen="make_input_vlan_map_stack")]),
                                            DEF("outer_vlans", [
                                                DEF(ANY, required=False, multi=True, name="vlan_filter",
                                                    gen="make_input_vlan_map_outer_vlans"),
                                            ]),
                                            DEF("inner_vlans", [
                                                DEF(ANY, required=False, multi=True, name="vlan_filter",
                                                    gen="make_input_vlan_map_inner_vlans"),
                                            ]),
                                            DEF("rewrite", [
                                                DEF(CHOICES("pop", "push", "swap", "drop"), [
                                                    DEF(ANY, name="vlan", required=False,
                                                        gen="make_input_vlan_map_rewrite_vlan")
                                                ], name="op",
                                                    required=True, gen="make_input_vlan_map_rewrite_operation"),
                                            ], required=False, multi=True, name="op_num")
                                        ], multi=True, required=True, name="num"),
                                        DEF("output_vlan_map", [
                                            DEF("stack", [
                                                DEF(CHOICES("0", "1", "2"), required=True, default="0",
                                                    name="stack", gen="make_output_vlan_map_stack")]),
                                            DEF("outer_vlans", [
                                                DEF(ANY, required=False, multi=True, name="vlan_filter",
                                                    gen="make_output_vlan_map_outer_vlans"),
                                            ]),
                                            DEF("inner_vlans", [
                                                DEF(ANY, required=False, multi=True, name="vlan_filter",
                                                    gen="make_output_vlan_map_inner_vlans"),
                                            ]),
                                            DEF("rewrite", [
                                                DEF(CHOICES("pop", "push", "swap", "drop"), [
                                                    DEF(ANY, name="vlan", required=False,
                                                        gen="make_output_vlan_map_rewrite_vlan")
                                                ], name="op",
                                                    required=True, gen="make_output_vlan_map_rewrite_operation"),
                                            ], required=False, multi=True, name="op_num")
                                        ], multi=True, required=True, name="num"),
                                        DEF("dynamic_vlans", [
                                            DEF(ANY, [
                                                DEF("service", [
                                                    DEF(CHOICES("voice", "mvr"), name="service",
                                                        gen="make_interface_serivce_vlan")
                                                ]),
                                            ], multi=True, name="vlan_filter")
                                        ], required=False)
                                    ]),
                                ], multi=True, name="unit", default="0")
                            ])
                        ], required=True, multi=True, name="interface")
                    ]),
                    DEF("route", [
                        DEF("inet", [
                            DEF("static", [
                                DEF(IPv4_PREFIX, [
                                    DEF("next-hop", [
                                        DEF(IPv4_ADDRESS, multi=True,
                                            name="next_hop", gen="make_inet_static_route_next_hop")
                                    ]),
                                    DEF("discard", gen="make_inet_static_route_discard")
                                ], name="route")
                            ])
                        ]),
                        DEF("inet6", [
                            DEF("static", [
                                DEF(IPv4_PREFIX, [
                                    DEF("next-hop", [
                                        DEF(IPv6_ADDRESS, multi=True,
                                            name="next_hop", gen="make_inet6_static_route_next_hop")
                                    ])
                                ])
                            ])
                        ]),
                    ]),
                    DEF("protocols", [
                        DEF("telnet", gen="make_protocols_telnet"),
                        DEF("ssh", gen="make_protocols_ssh"),
                        DEF("http", gen="make_protocols_http"),
                        DEF("https", gen="make_protocols_https"),
                        DEF("snmp", [
                            DEF("community", [
                                DEF(ANY, [
                                    DEF("level", [
                                        DEF(CHOICES("read-only", "read-write"), required=True,
                                            name="level", gen="make_snmp_community_level")
                                    ], required=True)
                                ], required=True, multi=True, name="community")
                            ]),
                            DEF("trap", [
                                DEF("community", [
                                    DEF(ANY, [
                                        DEF("host", [
                                            DEF(IP_ADDRESS, required=True, multi=True)
                                        ], required=True)
                                    ], required=True, multi=True)
                                ], required=True)
                            ])
                        ]),
                        DEF("isis", [
                            DEF("area", [
                                DEF(ISO_ADDRESS, required=True, multi=True)
                            ]),
                            DEF("interface", [
                                DEF(UNIT_NAME, [
                                    DEF("level", [
                                        DEF(CHOICES("1", "2"), required=True, multi=True)
                                    ])
                                ], required=True, multi=True)
                            ])
                        ]),
                        DEF("ospf", [
                            DEF("interface", [
                                DEF(UNIT_NAME, required=True, multi=True)
                            ])
                        ]),
                        DEF("ldp", [
                            DEF("interface", [
                                DEF(UNIT_NAME, required=True, multi=True)
                            ])
                        ]),
                        DEF("rsvp", [
                            DEF("interface", [
                                DEF(UNIT_NAME, required=True, multi=True)
                            ])
                        ]),
                        DEF("pim", [
                            DEF("mode", [
                                DEF(CHOICES("sparse", "dense", "sparse-dense"), required=True),
                            ], required=True),
                            DEF("interface", [
                                DEF(UNIT_NAME, required=True, multi=True)
                            ])
                        ]),
                        DEF("igmp-snooping", [
                            DEF("vlan", [
                                DEF(INTEGER, [
                                    DEF("version", [
                                        DEF(CHOICES("1", "2", "3"), required=True)
                                    ]),
                                    DEF("immediate-leave"),
                                    DEF("interface", [
                                        DEF(UNIT_NAME, [
                                            DEF("multicast-router")
                                        ], multi=True),
                                    ])
                                ], multi=True)
                            ])
                        ])
                    ])
                ], required=True, multi=True, name="instance", default="default")
            ], required=True)
        ], required=True, multi=True, name="vr", default="default")
    ]),
    # hints section will be dropped on ConfDB cleanup
    DEF("hints", [
        DEF("interfaces", [
            DEF("defaults", [
                DEF("admin-status", [
                    DEF(BOOL, required=True, name="admin_status",
                        gen="make_defaults_interface_admin_status")
                ])
            ])
        ]),
        DEF("protocols", [
            DEF("lldp", [
                DEF("status", [
                    DEF(BOOL, name="status", required=True, gen="make_global_lldp_status")
                ]),
                DEF("interface", [
                    DEF(IF_NAME, [
                        DEF("off", gen="make_lldp_interface_disable")
                    ], multi=True, name="interface")
                ])
            ]),
            DEF("spanning-tree", [
                DEF("status", [
                    DEF(BOOL, name="status", required=True, gen="make_global_spanning_tree_status")
                ]),
                DEF("priority", [
                    DEF(INTEGER, required=True, name="priority", gen="make_global_spanning_tree_priority")
                ]),
                DEF("interface", [
                    DEF(IF_NAME, [
                        DEF("off", gen="make_spanning_tree_interface_disable")
                    ], multi=True, name="interface")
                ])
            ]),
            DEF("loop-detect", [
                DEF("status", [
                    DEF(BOOL, name="status", required=True, gen="make_global_loop_detect_status")
                ]),
                DEF("interface", [
                    DEF(IF_NAME, [
                        DEF("off", gen="make_loop_detect_interface_disable")
                    ], multi=True, name="interface")
                ])
            ])
        ])
    ])
]
