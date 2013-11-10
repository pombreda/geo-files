#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import simplemapplot
import pandas as pd
from geonamescache import GeonamesCache


parser = argparse.ArgumentParser(
    description='Create a Choropleth world map without a legend.')
parser.add_argument('file', help='CSV data file')
args = parser.parse_args()

colors = ["#ffffff", '#ff0000']
countries = GeonamesCache().get_countries_by_names()

df = pd.read_csv(args.file)
country_data = df['Country']

colorize = {}
for name in country_data:
    colorize[countries[name]['iso'].lower()] = 1

simplemapplot.make_world_country_map(data=colorize, colors=colors)