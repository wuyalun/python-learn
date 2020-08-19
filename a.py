# !/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import csv
import time
import re
import binascii

#
# # s = '绝地求生'
# # ss = s.encode()
# # print(type(ss))
# # print(ss)
# # exit()
#
s = b'\xB2\xE2'
print(type(s))

ss = s.decode()
print(type(ss))
print(ss)


def str_to_hex(s):
    return r"/x" + r'/x'.join([hex(ord(c)).replace('0x', '') for c in s])


def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(r'/x')[1:]]])


def str_to_bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def bin_to_str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


a = "\xB2\xE2"
x = hex_to_str(a)
print(x)
print(hex_to_str(x))