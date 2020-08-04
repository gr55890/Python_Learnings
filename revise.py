import numpy as np 
import pandas as pd 
import random 

heights_A1 = np.array([176.2, 158.4, 167.6, 156.2, 161.4])
heights_A= pd.Series(heights_A1,index=['s1', 's2', 's3', 's4', 's5'])

weights_A1 = np.array([85.1, 90.2, 76.8, 80.4, 78.9])
weights_A= pd.Series(weights_A1,index=['s1', 's2', 's3', 's4', 's5'])

df_A1={'Student_height':heights_A,'Student_weight':weights_A}
df_A=pd.DataFrame(df_A1)

a= df_A[df_A['Student_height']>=160.0]
b= df_A[df_A['Student_weight']<=80.0]
print(a)
print(b)
#print(df_A_filter)

df_A_filter2= df_A[df_A.index == 's5']
print(df_A_filter2)
#df_A_filter.remove_duplicates(keep=False,inplace=True)

df_A['Gender'] = ['M', 'F', 'M', 'M', 'F']
#print(df_A)
df_groups=df_A.groupby('Gender').mean()
print(df_groups)
