import numpy as np 
import pandas as pd 
import random 

heights_A1 = np.array([176.2, 158.4, 167.6, 156.2, 161.4])
heights_A= pd.Series(heights_A1,index=['s1', 's2', 's3', 's4', 's5'])

weights_A1 = np.array([85.1, 90.2, 76.8, 80.4, 78.9])
weights_A= pd.Series(weights_A1,index=['s1', 's2', 's3', 's4', 's5'])

df_A1={'Student_height':heights_A,'Student_weight':weights_A}
df_A=pd.DataFrame(df_A1)

g= ['M', 'F', 'M', 'M', 'F']
df_A['Gender']=g
s1=[165.4, 82.7, 'F']
s=pd.Series(s1,index=['Student_height', 'Student_weight', 'Gender'],name='s6')
#print(df_A)
df_AA=df_A.append(s)
print(df_AA)



#-------------------------------------------------------------------------------#
height=df_A['Student_height']
#print(height)

df_s2s5s1=df_A.loc[['s2','s5','s1']]
print(df_s2s5s1)

#df_s1s4=df.loc[['s1','s4']]

#df_A.to_csv('classA.csv')
print(df_A)
df_A2=pd.read_csv('classA.csv')
print(df_A2)
df_A3=pd.read_csv('classA.csv',index_col=0)
print(df_A3)

random.seed(100)
heights_B1= np.random.normal(loc=170.0, scale=25.0, size=5)
#print(heights_B1)
heights_B= pd.Series(heights_B1,index=['s1','s2','s3','s4','s5'])

random.seed(100)
weights_B1= np.random.normal(loc=75.0, scale=12.0, size=5)
#print(weights_B1)
weights_B=pd.Series(weights_B1,index=['s1','s2','s3','s4','s5'])

df_B1={'Student_height':heights_B,'Student_weight':weights_B}
df_B=pd.DataFrame(df_B1)
#print(df_B)

#df_B.to_csv('classB.csv')
print(type(heights_B1))
print(type(weights_B1))

