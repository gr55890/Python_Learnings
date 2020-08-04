def train_with_profiling(opts, dirs):
    import cProfile, pstats, StringIO
    cProfile.runctx('train(opts, dirs)', \
                    {'train': train, 'opts': opts, 'dirs': dirs},
                    {}, 'mainstats')

    # create a stream for the profiler to write to
    profiling_output = StringIO.StringIO()
    p = pstats.Stats('mainstats', stream=profiling_output)

    # print stats to that stream
    # here we just report the top 30 functions, sorted by total amount of time spent in each
    p.strip_dirs().sort_stats('cumulative').print_stats(30)

    # print the result to the log
    print('---Profiling result follows---\n%s' % profiling_output.getvalue())
    profiling_output.close()
    print('---End of profiling result---') 

# !/usr/bin/python

import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))

#------------------------------------------------------------#
import calendar
import datetime

#monty=[calendar.month_abbr[i] for i in range(1,13)]
#print(monty)

year=2018
count=0
lst=[]
day_to_count = calendar.SUNDAY
for i in range(1,13):
     matrix= calendar.monthcalendar(year,i)
     print(matrix)
     num_days = sum(1 for x in matrix if x[day_to_count] != 0)
     print(num_days)
     if num_days>4:
        lst.append(i)
print(lst)
k=[]
for i in lst:
     month = datetime.date(2018, i, 1).strftime('%b')
     k.append(month)
print(k)

'''for k in range(0,12):
     if matrix[k][6]!= 0:
          count=count+1
     print(count)
'''

import unittest

def test_sample1():
    assert 3 == 3


class SampleTestClass(unittest.TestCase):


    def test_sample2(self):
        self.assertEqual(3, 3)

        