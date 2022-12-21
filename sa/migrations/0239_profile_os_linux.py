# ---------------------------------------------------------------------
# Update Linux profile
# ---------------------------------------------------------------------
# Copyright (C) 2007-2022 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Third-party modules
import bson
import uuid
from pymongo import InsertOne, DeleteOne, UpdateMany

# NOC modules
from noc.core.migration.base import BaseMigration


class Migration(BaseMigration):
    def migrate(self):
        db = self.mongo_db
        os_linux_profile_id = db.noc.profiles.find_one({"name": "OS.Linux"})
        bulk, bulk_pcr, bulk_fw = [], [], []
        if os_linux_profile_id:
            os_linux_profile_id = os_linux_profile_id["_id"]
        else:
            os_linux_profile_id = bson.ObjectId()
            bulk += [
                InsertOne(
                    {
                        "_id": os_linux_profile_id,
                        "name": "OS.Linux",
                        "uuid": uuid.UUID("ffdf0793-da3c-4f5d-9647-b0f40bad6f53"),
                        "description": None,
                    }
                )
            ]
        old_profiles = set()
        for profile in db.noc.profiles.find({"name": {"$regex": "^Linux.+"}}, {"_id": 1}):
            profile_id = profile["_id"]
            bulk += [DeleteOne({"_id": profile_id})]
            bulk_pcr += [
                UpdateMany({"profile": profile_id}, {"$set": {"profile": os_linux_profile_id}})
            ]
            bulk_fw += [
                UpdateMany({"profile": profile_id}, {"$set": {"profile": os_linux_profile_id}})
            ]
            old_profiles.add(profile_id)
        if old_profiles:
            old_profiles = list(old_profiles)
            self.db.execute(
                """
                    UPDATE sa_managedobject
                    SET version = null, profile = %s
                    WHERE profile = ANY(ARRAY[%s]::CHAR(24)[])
                """,
                [str(os_linux_profile_id), [str(x) for x in old_profiles]],
            )
            db.noc.actioncommands.update_many(
                {"profile": {"$in": old_profiles}}, {"$set": {"profile": os_linux_profile_id}}
            )
            db.noc.firmwares.update_many(
                {"profile": {"$in": old_profiles}}, {"$set": {"profile": os_linux_profile_id}}
            )
            db.noc.specs.update_many(
                {"profile": {"$in": old_profiles}}, {"$set": {"profile": os_linux_profile_id}}
            )
        if bulk:
            db.noc.profiles.bulk_write(bulk)
        if bulk_pcr:
            db.noc.profilecheckrules.bulk_write(bulk_pcr)
        if bulk_fw:
            db.noc.firmwares(bulk_fw)
