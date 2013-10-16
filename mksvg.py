#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kartograph import Kartograph
from geonamescache import GeonamesCache

K = Kartograph()
gc = GeonamesCache()
countries = gc.get_countries()

for iso2 in list(countries.keys()):
#for iso2 in ['FR']:
    cfg = {
        'layers': [{
            'id': 'country',
            'src': 'shp/ne_10m_admin_0_countries.shp',
            'filter': {'ISO_A2': iso2},
        }]
    }
    svg = 'svg/%s.svg' % iso2
    try:
        K.generate(cfg, outfile=svg, stylesheet='#country {fill: black;}')
    except Exception as err:
        print(
            ('Exception for country %s:\n%r' % (countries[iso2]['name'], err)))