#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kartograph import Kartograph
import os

K = Kartograph()
css = '#country {fill: #000;}'

for iso3 in os.listdir('shp/countries'):
    source_file = 'shp/countries/%s/%s.shp' % (iso3, iso3)
    target_file = 'svg/countries/%s.svg' % iso3
    cfg = {
        'layers': [{
            'id': 'country',
            'src': source_file,
        }]
    }

    try:
        K.generate(cfg, outfile=target_file, stylesheet=css)
    except Exception as err:
        print(('Exception for country %s:\n%r' % iso3))