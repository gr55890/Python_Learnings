import sys
import os 

#Add Circle class implementation below
class Circle:
        
        def __init__(self,radius):    
            self.radius=radius
        def area(self):
            ar=3.14*self.radius*self.radius
            return ar

'''Check the Tail section for input/output'''
res_lst=[]
lst = [1,2,3]
for radius in lst:
    res_lst.append(Circle(radius).area())
print(res_lst," ",Circle.no_of_circles)
#fout.write("{}\n{}".format(str(res_lst), str(Circle.no_of_circles)))
