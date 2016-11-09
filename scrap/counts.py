#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
from lianjia_wuhan import ershoufang

while True:
    print(ershoufang.find().count())
    time.sleep(5)
