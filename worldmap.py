#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kartograph import Kartograph

K = Kartograph()

cfg = {
    'layers': [{
        'id': 'country',
        'src': 'shp/ne_50m_admin_0_countries.shp'
    }]
}
svg = 'svg/world.svg'
K.generate(cfg, outfile=svg, stylesheet='#country {fill: #000;}')