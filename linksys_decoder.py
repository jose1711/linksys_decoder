#!/usr/bin/env python3
'''
Decoder for Linksys.cfg file. Can be used to recover
password from a saved config file.

based on C code from
http://www.linksysinfo.org/index.php?threads/recover-password-from-config-file.6468/

Usage:
  linksys_decoder.py linksys_router.cfg
'''
from struct import unpack
from sys import argv
from string import printable

last_empty = False

with open(argv[1], 'rb') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        c = unpack('>b', c)[0]
        decoded = ~((c << 2) | ((c & 0xc0) >> 6)) % 256
        if not decoded:
            print(' ')
            continue
        if chr(decoded) in printable:
            print(chr(decoded), end='')
            last_empty = False
        else:
            if not last_empty:
                last_empty = True
                print('\n', end='')
