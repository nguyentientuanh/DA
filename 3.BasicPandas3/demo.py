#Buoi5 8/5/2024
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
filename = "FoodPrice_in_Turkey.csv"
df= pd.read_csv('FoodPrice_in_Turkey.csv')
# print(df.head(),'1')
# print(df.info(),'2')
# print(df.describe(),'3')
# print(df.count(),'4')
# print(df['Price'].min(),'5')
# print(df['Price'].max(),'6')
# print(df['Price'].mean(),'7')
# print(df['Price'].median(),'8')
# print(df['ProductName'].mode(),'9')
# print(df['Price'].var(),'10')
# print(df['Price'].std(),'11')
#df.pivot_table(values='Price', index='ProductName', columns='Place', aggfunc='mean')
#df=sns.load_dataset("penguins")
sns.histplot(df['Price'])
print(plt.show(),'1')
df.pivot_table(values=['Price', 'Year'],
               index='ProductName',
               columns='Place',
               aggfunc={'Price':'min','Year':'max'})



