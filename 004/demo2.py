import pandas as pd

df = pd.read_csv('shopeep_koreantop_clothing_shop_data.csv')
# print(df.head(),'1')
# print(df.info(),'2')
# print(df.describe(),'3')
print(df.columns)
#Loc du lieu
    #Loc ra cot shop_location
print(df['shop_location'])
    
    #loc ra cac cot join_day, join_month, join_year
print(df[['join_day','join_month','join_year']])

    #Loc ra du lieu join_month='April'
print(df[df['join_month']=='April'])

    #Loc ra du lieu co dieu kien join_year = 2021 va follower_count >=10000
print(df[(df['join_year']==2021)&(df['follower_count']>=10000)])

    #hien thi cac thong tin ve respontime, response_rate cau join_month='April'
print(df[df['join_month']=='April'][['response_time','response_rate']])


