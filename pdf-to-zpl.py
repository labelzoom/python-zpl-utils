#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""pdf-to-zpl.py: Uses the LabelZoom API to convert a PDF document to ZPL"""

import requests

document_path = 'document.pdf' # TODO: Replace this with the relative or absolute path of the document you want to convert

with open(document_path, 'rb') as f:
    pdf_bytes = f.read()

token = '00000000-0000-0000-0000-000000000000' # TODO: Replace with your API key
url = 'https://www.labelzoom.net/api/v2/convert/pdf/to/zpl'
headers = { 'Content-Type': 'application/pdf', 'Accept': 'text/plain', 'Authorization': f'Bearer {token}' }
response = requests.post(url, data=pdf_bytes, headers=headers)

try:
    zpl = response.text
    print(zpl)
except requests.exceptions.RequestException:
    print(response.text)
