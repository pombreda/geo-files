#!/bin/bash
FORMAT=$1
[ $# -eq 0 ] && { echo "Usage: $0 format"; exit 1; }

mogrify -resize 600x600 -format $FORMAT svg/*.svg
mv svg/*.$FORMAT img/
