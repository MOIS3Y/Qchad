#!/usr/bin/env python3
from time import sleep


with open('/tmp/test.txt', 'a') as f:
    for i in range(60):
        f.write(str(i))
