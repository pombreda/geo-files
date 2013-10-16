#!/bin/bash
mogrify -resize 600x600 -format png svg/*.svg
mv svg/*.png png/
