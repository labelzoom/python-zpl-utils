#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""png-to-zpl.py: Uses the LabelZoom API to convert a PNG image to ZPL"""

import requests

image_path = 'LabelZoom_Logo_f_400px.png' # TODO: Replace this with the relative or absolute path of the image you want to convert

with open(image_path, 'rb') as f:
    image_bytes = f.read()

url = 'https://www.labelzoom.net/api/v2/convert/png/to/zpl'
headers = { 'Content-Type': 'image/png', 'Accept': 'text/plain' }
response = requests.post(url, data=image_bytes, headers=headers)

try:
    zpl = response.text
    print(zpl)
except requests.exceptions.RequestException:
    print(response.text)
