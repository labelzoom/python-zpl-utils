#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""print-zpl.py: Sends ZPL to a Zebra printer using a ZebraNet network adapter"""

import socket

zpl = '^XA^FO20,20^A0N,48^FDgithub.com/labelzoom^FS^XZ' # TODO: Replace this with the ZPL you want to print
printer_ip_or_hostname = '192.168.0.44' # TODO: Replace this with the IP address or hostname of the printer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((printer_ip_or_hostname, 9100))
s.sendall(str.encode(zpl))
s.close()
