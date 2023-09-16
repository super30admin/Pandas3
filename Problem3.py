'''
1. Iterating over the entire df using iterrows
2. Iterating over the entire df using itertuples
'''
import pandas as pd

df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
					'Cost':[10000, 5000, 15000, 2000]})
print(df)


# 1. Using iterrows
# Create an empty list
result =[]
# Iterate over each row using iterrows
for index, rows in df.iterrows():
	# Create list for the current row
	my_list =[rows.Date, rows.Event, rows.Cost]
	# append the list to the final list
	result.append(my_list)
print(result)


# 2. Using itertuples
result =[]
# Iterate over each row using itertuples
for  rows in df.itertuples():
	my_list =[rows.Date, rows.Event, rows.Cost]
	result.append(my_list)
print(result)
