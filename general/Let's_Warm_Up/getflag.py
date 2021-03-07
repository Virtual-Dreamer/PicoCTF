#!/usr/bin/python3

hex = '0x70'[2:]
bytes = bytes.fromhex(hex)
ascii = bytes.decode('ASCII')
print(ascii)

