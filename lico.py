#!/usr/bin/env python
# -*- coding: utf-8 -*-
# data from http://linuxcounter.net/xml/where_users_live.xml
import numpy
import colorbrewer

from bs4 import BeautifulSoup

# mapping of ISO2 country codes to data
lico_data = {}

with open('where_users_live.xml', 'r') as f:
    lico_xml = f.read()

lico_soup = BeautifulSoup(lico_xml, 'xml')
for line in lico_soup.find_all('line'):
    iso2 = line.find('code').text.lower()
    user_count = float(line.find('users').text)
    pop_count = float(line.find('population').text)
    lico_data[iso2] = user_count

user_counts = list(lico_data.values())
min_users = min(user_counts)
max_users = max(user_counts)

color_scheme = colorbrewer.Blues[9]
bins = numpy.linspace(min_users, max_users, len(color_scheme))

with open('svg/world-choropleth.svg', 'r') as f:
    map_svg = f.read()

map_soup = BeautifulSoup(map_svg, 'xml')

#FIXME append country classes to <style id="style_css_sheet" type="text/css">

for path in map_soup.find_all(['path', 'g', 'circle']):
    classes = path.attrs.get('class', '').split()

    if not classes or classes[0] not in ['landxx', 'circlexx', 'unxx']:
        continue

    if classes[1] == 'coastxx':
        iso2 = classes[2]
    elif classes[1] == 'subxx':
        iso2 = classes[3]
    else:
        iso2 = classes[1]

    country_val = lico_data.get(iso2, None)
    if not country_val:
        continue

    color = color_scheme[numpy.digitize([country_val], bins)[0] - 1]
    path['style'] = 'fill:#%02x%02x%02x;' % color


with open('svg/lico.svg', 'w') as f:
    f.write(str(map_soup))