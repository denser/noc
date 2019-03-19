# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Config check
# ---------------------------------------------------------------------
# Copyright (C) 2007-2019 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# NOC modules
from noc.core.error import NOCError
from noc.services.discovery.jobs.base import DiscoveryCheck


class ConfigCheck(DiscoveryCheck):
    """
    Version discovery
    """
    name = "config"
    required_script = "get_config"

    def handler(self):
        self.logger.info("Checking config")
        config = self.get_config()
        if config:
            changed = self.object.save_config(config, validate=False)
            self.set_artefact("config_changed", changed)
            self.set_artefact("config_acquired", True)
        else:
            self.logger.error("Cannot get config")

    def get_config(self):
        p = self.object.get_config_policy()
        if p == "s":  # Script
            return self.get_config_script()
        elif p == "S":  # Script, Download
            return self.get_config_script() or self.get_config_download()
        elif p == "D":  # Download, Script
            return self.get_config_download() or self.get_config_script()
        elif p == "d":  # Download
            return self.get_config_download()
        self.logger.error("Invalid config policy: %s", p)
        return None

    def get_config_script(self):
        if "get_config" not in self.object.scripts:
            self.logger.info("get_config script is not supported. Cannot request config from device")
            return None
        self.logger.info("Requesting config from device")
        try:
            return self.object.scripts.get_config()
        except NOCError as e:
            self.logger.error("Failed to request config: %s", e)
            return None

    def get_config_download(self):
        self.logger.info("Downloading config from external storage")
        # Check storage is set
        storage = self.object.object_profile.config_download_storage
        if not storage:
            self.logger.error("Failed to download. External storage is not set")
            return None
        # Check path template
        tpl = self.object.object_profile.config_download_template
        if not tpl:
            self.logger.error("Failed to download. Path template is not set")
            return None
        # Render path
        path = tpl.render_subject(object=self.object).strip()
        if not path:
            self.logger.error("Failed to download. Empty path")
            return None
        # Download
        self.logger.info("Downloading from %s:%s", storage.name, path)
        try:
            with storage.open_fs() as fs:
                with fs.open(path) as f:
                    return f.read()
        except storage.Error as e:
            self.logger.info("Failed to download: %s", e)
            return None
