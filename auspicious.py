import pandas as pd
nameid = pd.Series(range(101, 111))
name = pd.Series(['person' + str(i) for i in range(1, 11)])
M={'nameid':nameid, 'name':name}
master = pd.DataFrame(M)
transaction = pd.DataFrame({'nameid':[108, 108, 108,103], 'product':['iPhone', 'Nokia', 'Micromax', 'Vivo']})
mdf=master.merge(transaction,on='nameid')
print(mdf)