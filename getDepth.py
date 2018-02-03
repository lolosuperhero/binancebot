#!/usr/bin/env python
# coding=utf-8
import requests
import json

link = "http://www.binance.com/api/v1/depth?symbol=LSKETH&limit=5"
f = requests.get(link)

j = json.loads(f.text)

print j['bids'][0][0]
