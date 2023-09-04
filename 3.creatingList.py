
import pandas as pd

df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
					'Cost':[10000, 5000, 15000, 2000]})
print(df)

#The iterrows() method generates an iterator object of the DataFrame, allowing us to iterate each row in the DataFrame.
#Each iteration produces an index object and a row object (a Pandas Series object).
Row_list =[]
for index, rows in df.iterrows():
	my_list =[rows.Date, rows.Event, rows.Cost]
	Row_list.append(my_list)

print(Row_list)
print(len(Row_list))
print(Row_list[:3])

#itertuples() method generates an iterator object of the DataFrame, returning each row as a Pyton Tuple object.
Row_list =[]
for index, rows in df.itertuples():
	my_list =[rows.Date, rows.Event, rows.Cost]
	Row_list.append(my_list)

print(Row_list)
print(len(Row_list))
print(Row_list[:3])
