import pandas as pd

df = pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')

#Tinh nhanh: so tien tip trung binh trong mot nha hang theo gioi tinh
#df.groupby('gender')['tip'].mean()
#<bang du lieu>.groupby('nhom')['gia tri].ham()
print(df.groupby('join_year')['rating_bad'].max().reset_index())#reset_index de chuyen ve 1 bang

#Groupby mot cot, mot gia tri, nhieu ham toan tu
#tinh rating_bad trung binh va rating_bad lon nhat theo join_year
print(df.groupby('join_year')['rating_bad'].agg(['mean','max']).reset_index())

#Groupby mot cot, nhieu gia tri, nhieu ham
#tinh rating_bad trung binh vaf rating_good lon nhat theo join_year
print(df.groupby('join_year')[['rating_bad','rating_good']].agg({'rating_bad':'mean','rating_good':'max'}))


#Groupby 2 cot, mot gia tri
#tinh rating_good trung binh theo join_year va shop_loction
df.groupby(['join_year'])

######Gom nhom du lieu (groupby)

#df.groupby('nhom')['gia tri'].ham()
#df.groupby('nhom')['gia tri'].agg()

#Nhieu
    #Nhieu nhom: .groupby(['nhom1','nhom2'])
    #Nhieu gia tri: [['gia tri 1','gia tri 2']]
    #Nhieu ham: .agg(['ham 1','ham 2'])
    #chi dinh gia tri nay di voi gia tri kia: .agg({'giatri1':'ham1','giatri2':'ham2'})


###Chuyen doi dinh dang du lieu
    #.astype('dinh dang minh muon)
df['date']=df['join_month']+" "+df['join_day'].astype('str')+","+df['join_year'].astype('str')
print(df[['join_month','join_day','join_year','date']])