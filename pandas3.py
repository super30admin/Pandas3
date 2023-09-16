#Problem 1 : Drop rows from the dataframe based on certain condition applied on a column
import pandas as pd
df = pd.DataFrame({'Players':['Dhoni','Virat','Ganguli'],'Runs':[2500,3000,2000]})
print(df)
df_filtered = df[df['Runs'] >= 2500]
print('\n',df_filtered)
#Problem 2 :Insert row at given position in Pandas Dataframe
import pandas as pd
df = pd.DataFrame({'Players':['Dhoni','Virat','Ganguli'],'Runs':[2500,3000,2000]})

def Insert_row(position_index, df, new_row):
    df = pd.concat([df.iloc[:position_index], pd.DataFrame([new_row]), 				df.iloc[position_index:]]).reset_index(drop=True)
    df.reset_index(drop=True, inplace=True)
    return df

newrow={'Players':'Sachin','Runs':4000}
print(Insert_row(1,df,newrow))

#Problem 3 :Create a list from rows in Pandas dataframe
import pandas as pd

df = pd.DataFrame({'Players':['Dhoni','Virat','Ganguli'],'Runs':[2500,3000,2000]})
Row_list =[]

for index, rows in df.iterrows():
    my_list =[rows.Players, rows.Runs]
    Row_list.append(my_list)

print(Row_list)
print(len(Row_list))
print(Row_list[:3])

#Problem 4 :Ranking Rows of Pandas DataFrame
import pandas as pd

df = pd.DataFrame({'Players':['Dhoni','Virat','Ganguli'],'Runs':[2500,3000,2000]})
df['Runs'] = df['Runs'].rank(ascending = 1)
df = df.set_index('Runs')
print(df)
#Problem 5 :Sorting rows in pandas DataFrame 
import pandas as pd

df = pd.DataFrame({'Players':['Dhoni','Virat','Ganguli'],'Runs':[2500,3000,2000]})
df = df.sort_values(by ='Runs', ascending = 1)
print(df)

#Problem 6 :Fix Names in a Table(leetcode)
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by='user_id')
