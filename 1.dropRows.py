
import pandas as pd

df = pd.read_csv('nba.csv')
print(df.head(15))
print(df.shape)

#Delete rows based on the condition of a column
df_filtered = df[df['Age'] >= 25]

print(df_filtered.head(15))
print(df_filtered.shape)

#Delete rows based on multiple conditions on a column

# delete all rows with column 'Age' has value 30 to 40
indexAge = df[ (df['Age'] >= 30) & (df['Age'] <= 40) ].index
df.drop(indexAge , inplace=True)
df.head(15)

#Delete rows based on multiple conditions on different columns
indexAge = df[ (df['Name'] == 'John Holland') | (df['Position'] == 'SG') ].index
df.drop(indexAge , inplace=True)
df.head(15)
