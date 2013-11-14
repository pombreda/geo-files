#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kartograph import Kartograph
import os

K = Kartograph()
css = '#country {fill: #000;}'

for iso2 in os.listdir('shp'):
    source_file = 'shp/%s/%s.shp' % (iso2, iso2)
    target_file = 'svg/%s.svg' % iso2
    cfg = {
        'layers': [{
            'id': 'country',
            'src': source_file,
        }]
    }

    try:
        K.generate(cfg, outfile=target_file, stylesheet=css)
    except Exception as err:
        print(('Exception for country %s:\n%r' % iso2))