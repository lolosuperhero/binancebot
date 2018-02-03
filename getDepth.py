#!/usr/bin/env python
# coding=utf-8
import requests
import json


link = "http://www.binance.com/api/v1/depth?symbol=LSKETH&limit=100"
f = requests.get(link)
j = json.loads(f.text)

#  "bids": [
#    [
#      "4.00000000",     // PRICE
#      "431.00000000",   // QTY
#      []                // Ignore.
#    ]
bidsTotal = 0
sumAllQuantity = 0
for bids in j['bids']:
    bidsTotal+=float(bids[0])*float(bids[1])
    sumAllQuantity+=float(bids[1])
print("total bids=%f" % (bidsTotal))

#  "asks": [
#    [
#      "4.00000200",
#      "12.00000000",
#      []
#    ]
#  ]
asksTotal = 0
for asks in j['asks']:
    asksTotal+=float(asks[0])*float(asks[1])
    sumAllQuantity+=float(asks[1])
print("total asks=%f" % (asksTotal))

#fair value
fairValue=(bidsTotal+asksTotal)/sumAllQuantity
print("fairValue=%f" % (fairValue))

link = "http://www.binance.com/api/v1/aggTrades?symbol=LSKETH&limit=100"
f = requests.get(link)
j = json.loads(f.text)
cpt = 0
for trades in j:
    cpt+=1
    if cpt==1:
        firstValue=float(trades['p'])
    else:
        lastValue=float(trades['p'])
tendance=(lastValue-firstValue)
print("tendance=%f" % (tendance))
