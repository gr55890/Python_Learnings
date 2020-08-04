import math
import os
import random
import re
import sys
#import requests


#def avgRotorSpeed(statusQuery, parentId):
    # Write your code here

statusQuery = input()
number = int(input().strip())
URL= "https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={number}"
PARAMS= {'status':statusQuery,'page': number}
r= requests.get(url=URL,params=PARAMS)
print(r)