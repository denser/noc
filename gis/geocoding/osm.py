# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# OSM Nominatim geocoder
# ---------------------------------------------------------------------
# Copyright (C) 2007-2019 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Third-party modules
from six.moves.urllib.parse import quote as urllib_quote
import requests
# NOC modules
from base import Geocoder


class Nominatim(Geocoder):
    name = "osm"

    def forward(self, s):
        url = "http://nominatim.openstreetmap.org/search?q="
        url += urllib_quote(s) + "&format=json&addressdetails=1"
        r = requests.get(url)
        d = r.json()
        if d:
            lon = float(d[0]["lon"])
            lat = float(d[0]["lat"])
            return "EPSG:4326", lon, lat
        else:
            return None, None, None
