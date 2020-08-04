import numpy as np 
import pandas as pd 

heights_A1 = np.array([176.2, 158.4, 167.6, 156.2, 161.4])
heights_A= pd.Series(heights_A1,index=['s1', 's2', 's3', 's4', 's5'])

weights_A1 = np.array([85.1, 90.2, 76.8, 80.4, 78.9])
weights_A= pd.Series(weights_A1,index=['s1', 's2', 's3', 's4', 's5'])

df_A1={'Student_height':heights_A,'Student_weight':weights_A}
df_A=pd.DataFrame(df_A1)
#print(df_A)
df_A.at['s3','Student_height']=np.NaN
df_A.at['s3','Student_weight']=np.NaN
#print(df_A)
df_A.at['s5','Student_weight']=np.NaN
df_A2=df_A.dropna(axis=0,how='any')
print(df_A2)