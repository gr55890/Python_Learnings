import os
import sys

#Add Circle class implementation below
class Circle:
    def __init__(self,radius):  
        self.radius=radius
      
'''Check the Tail section for input/output'''

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        lst = list(map(lambda x: float(x.strip()), input().split(',')))
        for radius in lst:
            res_lst.append(Circle(radius).area())
        fout.write("{}\n{}".format(str(res_lst), str(Circle.no_of_circles)))


       # HMSET roomrate:New_Delhi:Maidens_Hotel:2017-10-06:single '{"occupancy":2,"avail_count":13,"booked_count":4,"currencyisocode":"INR","currency_name":"Rupee"}'
       # redis.hmset("roomrate:New_Delhi:Maidens_Hotel:2017-10-06:single",'{"occupancy":2,"avail_count":13,"booked_count":4,"currencyisocode":"INR","currency_name":"Rupee"}');

import calendar

year = 2016
month = 3
day_to_count = calendar.SUNDAY

matrix = calendar.monthcalendar(year,month)

num_days = sum(1 for x in matrix if x[day_to_count] != 0)

