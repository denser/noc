# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Config *MUST* match all strings
# ---------------------------------------------------------------------
# Copyright (C) 2007-2015 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# NOC modules
from noc.cm.validators.text import TextValidator


class MatchAllStringsValidator(TextValidator):
    TITLE = "Config *MUST* match all strings"
    DESCRIPTION = """
        Config must contain all strings in arbitrary order
    """
    CONFIG_FORM = [
        {"name": "template", "xtype": "textarea", "fieldLabel": "Template", "allowBlank": False},
        {"name": "error_text", "xtype": "textarea", "fieldLabel": "Error text", "allowBlank": True},
        {"name": "strip", "xtype": "checkbox", "boxLabel": "Strip spaces", "inputValue": True},
    ]

    def check(self, template, error_text, strip=False, **kwargs):
        tpl = self.expand_template(template)
        tpl = tpl.splitlines()
        if strip:
            tpl = [x.strip() for x in tpl]
        seen = set(x for x in tpl if x)
        for line in self.get_config_block().splitlines():
            if strip:
                line = line.strip()
            if line in seen:
                seen.remove(line)
            if not seen:
                break
        if seen:
            if self.scope == self.INTERFACE:
                obj = self.object.name
            else:
                obj = None
            self.assert_error(
                "Config | Mismatch Template", obj=obj, msg=error_text or "\n".join(seen)
            )
