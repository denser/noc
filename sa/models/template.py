# ---------------------------------------------------------------------
# Template helper utilities
# ---------------------------------------------------------------------
# Copyright (C) 2007-2019 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import os

# Third-party modules
from django.template import Template, Context


def render_template(name, context=None):
    """
    Render template
    :param name:
    :param context:
    :return:
    """

    def get_path(name):
        local_path = os.path.join("local", "templates", name)
        if os.path.exists(local_path):
            return local_path
        default_path = os.path.join("templates", name)
        if os.path.exists(default_path):
            return default_path
        return None

    # Get cached template
    if name not in _tpl_cache:
        path = get_path(name)
        if path:
            with open(path) as f:
                _tpl_cache[name] = Template(f.read())
        else:
            _tpl_cache[name] = None
    #
    tpl = _tpl_cache[name]
    if tpl:
        return tpl.render(Context(context or {}))
    else:
        return None


def render_message(name, context=None):
    """
    Render template. Treat first Subject: line as a subject.
    Returns subject, body tuple
    :param name:
    :param context:
    :return: subject, body tuple
    """

    def strip_leading_newlines(lines):
        lc = lines[:]
        while lc and not lc[0].strip():
            lc.pop(0)
        return lc

    msg = render_template(name, context)
    if not msg:
        return None, None  # No template
    ln = strip_leading_newlines(msg.splitlines())
    if ln and ln[0].startswith("Subject"):
        subject = ln.pop(0)[8:].strip()
        body = "\n".join(strip_leading_newlines(ln[1:]))
        return subject, body
    else:
        return None, "\n".join(ln)


_tpl_cache = {}  # name -> template instance
