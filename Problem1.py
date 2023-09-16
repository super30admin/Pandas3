'''
1. We perform deletion of rows based on condition on a column using filtering based on boolean array
2. We use drop method to drop those indices which have failed the condition
3. We drop based on multiple conditions on different columns
'''
import pandas as pd

df = pd.read_csv('nba.csv')
print(df.head(15))
print(df.shape)

# 1. Delete rows based on the condition of a column
df_filtered = df[df['Age'] >= 25]
print(df_filtered.head(15))
print(df_filtered.shape)

# 2.i. Delete rows based on multiple conditions on a column using df.drop()
indices = df[(df['Age'] >= 40) & (df['Age'] <= 50)].index
df_filtered = df.drop(index=indices)
print(df_filtered.head(15))
print(df_filtered.shape)

# 2.ii. Delete rows based on multiple conditions on a column using df.drop()
indices = df[(df['Name'] != 'John Holland') & (df['Position'] == 'PG')].index
df_filtered = df.drop(index=indices)
print(df_filtered.head(15))
print(df_filtered.shape)

