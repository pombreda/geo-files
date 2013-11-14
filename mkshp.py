#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fiona
import os
import argparse

parser = argparse.ArgumentParser(description='Create shapefiles for countries.')
parser.add_argument('shp', help='Source shapefile')
parser.add_argument('--iso3', help='ISO 3166-1 alpha-3 country code.')
args = parser.parse_args()


with fiona.open(args.shp) as source:
    driver = source.driver
    schema = source.schema

    for country in source:
        try:
            iso3 = country['properties']['adm0_a3']
        except KeyError:
            iso3 = country['properties']['ADM0_A3']

        if args.iso3 and iso3 != args.iso3:
            continue

        target_dir = 'shp/countries/%s' % iso3
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        with fiona.open(os.path.join(target_dir, '%s.shp' % iso3), 'w',
            driver=driver, schema=schema) as target:

            target.write(country)