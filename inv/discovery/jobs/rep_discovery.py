## -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## REP Link Discovery Job
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from link_discovery import LinkDiscoveryJob
from noc.settings import config


class REPLinkDiscoveryJob(LinkDiscoveryJob):
    """
    REP Link Discovery
    """
    name = "rep_discovery"
    map_task = "get_rep_topology"
    method = "rep"
    ignored = not config.getboolean("rep_discovery", "enabled")
    initial_submit_interval = config.getint("rep_discovery",
        "initial_submit_interval")
    initial_submit_concurrency = config.getint("rep_discovery",
        "initial_submit_concurrency")

    def process_result(self, object, result):
        first_mac, last_mac = self.get_object_macs(object)
        if not first_mac or not last_mac:
            return  # ID discovery is incomplete
        for segment in result:
            # Find own ports
            o = [i for i, p in enumerate(segment)
                 if first_mac <= p["mac"] <= last_mac]
            if not o:
                continue  # Not found
            elif len(o) == 2:
                # Inside the ring
                self.submit_pair(object,
                    segment[o[0]], segment[o[0] - 1])
                self.submit_pair(object,
                    segment[o[1]], segment[o[1] + 1])
            elif len(o) == 1:
                # End of the ring
                if o[0] == 0:
                    # First
                    self.submit_pair(object,
                        segment[o[0]], segment[o[0] + 1])
                else:
                    # Last
                    self.submit_pair(object,
                        segment[o[0]], segment[o[0] - 1])
            else:
                # Something strange
                self.error("Invalid REP discovery result: %r" % segment)
                continue

    def submit_pair(self, object, local_info, remote_info):
        remote_object = self.get_neighbor_by_mac(remote_info["mac"])
        if not remote_object:
            return  # Not found still
        self.submit_candidate(
            object.profile.convert_interface_name(local_info["port"]),
            remote_object,
            remote_object.profile.convert_interface_name(remote_info["port"])
        )
