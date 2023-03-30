# ----------------------------------------------------------------------
# Cleanup cfgmetricsources collection
# ----------------------------------------------------------------------
# Copyright (C) 2007-2023 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# NOC modules
from noc.core.migration.base import BaseMigration


class Migration(BaseMigration):
    def migrate(self):
        self.mongo_db["ds_cfgmetricsources"].delete_many({})
