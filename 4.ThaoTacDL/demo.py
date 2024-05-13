#Buoi6 10/5/2024
import pandas as pd
import seaborn as sns
#Xem Qua
df = pd.read_csv('FoodPrice_in_Turkey.csv')
print(df.head(),'1')#xem 5 dong dau
print(df.tail(),'2')#xem 5 dong cuoi
print(df.sample(10),'3')#xem cac dong bat ky

###Xem Ky
#Cau Truc
print(df.shape,'4')#bnh dong bnh cot
print(df.info(),'5')#dinh dang du lieu cua tung cot
print(df.columns,'6')#in het ten cac cot

print(df.describe(),'7')#Noi dung
######mo ta khai quat
#mean
#median
#mode
######Mo ta ky hon
#range
#quantile
##q1:25%
##q2:50%
##q3:75%
#phuong sai(variance)va do lech chuan(standard deviation)

##Truy cap du lieu
#Truy cap truc tiep: location -> df.loc[ten dong, ten cot]
#Truy cap gian tiep: integer _> df.iloc[so thu tu dong, so thu tu cot]

##Loc du lieu
    #loc cot: name, age, gender :df[['name','age','gender']]
    #loc dong: df[df['age']>30]

##Chinh sua du lieu
    #Doi ten cot: df.rename(columns={'ten cu':'ten moi'})
    #Them cot: revenue (price*quantity):df['Revenue']=df['Price']*df['Quantity']
    #Xoa cot: df.drop('Revenue',axis=1, inplace=True)
    #Them dong: pd.concat()
    #Xoa dong: df.drop(hang,axis=0, inplace=True)

###Tao bang pivot
    #df.pivot_table(values=, index= ,colums=, aggfunc=)
    #count, mean, sum, max, min

### Noi bang:
    #Luu y laf loc du lieu truoc
    #UNION ->pd.concat([df1,df2,df3],axis=0)
    #JOIN ->pd.merge(df1,df2,on='key',how='inner')


