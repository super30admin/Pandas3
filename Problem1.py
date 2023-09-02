# Problem 1 : Drop rows from the dataframe based on certain condition applied on a column
import pandas as pd
df=pd.read_csv('nba.csv')

# Delete the rows based on the condition of the column
df_filtered=df[df['Age']>=25]
print(df_filtered)

# Delete rows based on multiple conditions on a column
Age_group=df[(df['Age']>=25)&(df['Age']<=30)]

df.drop(Age_group,Incpalce=True)
print(df)

# Delete rows based on multiple conditions on different columns

indexAge=df[(df['Name']=='John')&(df['Position']=='SG')].index

print(indexAge)