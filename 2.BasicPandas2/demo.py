import pandas as pd

filename = "FoodPrice_in_Turkey.csv"
df= pd.read_csv('FoodPrice_in_Turkey.csv')
df = df.rename(columns={'Place':'DiaDiem', 'ProductName':'TenSP'})
print(df.head(),'1')

#THEM COT MOI
df['GiamGia']='15%'
print(df.head(),'2')


df['GiaMoi']=df['Price']-df['Price']*15/100
print(df.head(),'3')

#XOA COT
#C1
# df1=df[['Price','GiamGia','GiaMoi']]
# print(df1.head(),'4')
#C2
# df=df.drop(['Month','Year'],axis=1)
# print(df.head(),'4')
df.drop(['Month','Year'],axis=1,inplace=True)
print(df.head(),'4')

#Thay Doi Bang
df.replace(52,'RR',inplace=True)
print(df.head(),'5')

df['UmName'].replace('KG',"kg",inplace=True)
print(df.head(),'6')



