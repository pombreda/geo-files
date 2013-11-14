#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fiona
import os

shpsource = 'source_data/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'

with fiona.open(shpsource) as source:
    driver = source.driver
    schema = source.schema

    for country in source:
        iso2 = country['properties'].get('ISO_A2', None)
        if not iso2:
            print(('No ISO2 code fpr %s', country.properties.get('NAME', None)))
            continue

        target_dir = 'shp/%s' % iso2
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        with fiona.open(os.path.join(target_dir, '%s.shp' % iso2), 'w',
            driver=driver, schema=schema) as target:

            target.write(country)