import pandas as pd
d = pd.read_csv("seattle-weather.csv")
print(d)
print(d['date'][d['weather']=='rain'])
k={'a':[1,2,3,4],
   'b':['k','j','l','m']
        }
j=pd.DataFrame(k)
print(j)
print(d.shape)
print(d.head())
print(d.tail())
print(d.head(4))
print(d.tail(4))
print(d[300:306])
print(d[['date','wind']])
print(d.wind)
print(d.describe())
print(d.index)
print(d.set_index('date',inplace=True))
print(d.loc['2015-12-31'])
d.reset_index(inplace=True)
print(d)
