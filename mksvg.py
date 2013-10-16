#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kartograph import Kartograph
from geonamescache import GeonamesCache

K = Kartograph()
gc = GeonamesCache()
countries = gc.get_countries()

for iso2 in list(countries.keys()):
#for iso2 in ['FR', 'ES']:
    cfg = {
        'layers': [{
            'id': 'country',
            'src': 'shp/ne_50m_admin_0_countries.shp',
#            'src': 'shp/ne_10m_admin_1_states_provinces.shp',
            'filter': {'iso_a2': iso2},
        }]
    }
    svg = 'svg/%s.svg' % iso2
    try:
        K.generate(cfg, outfile=svg, stylesheet='#country {fill: #000;}')
    except Exception as err:
        print(
            ('Exception for country %s:\n%r' % (countries[iso2]['name'], err)))