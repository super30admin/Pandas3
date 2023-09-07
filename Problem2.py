'''
1. Insert row at given position in Pandas Dataframe using a custom function, index slicing and adding 1 to lower half indices.
2. Then adding the df belonging to row number at the end of df. Later, sorting on index will give the result.
3. Using concat function to concat upper and lower half of dataframes and reindexing using iterator on length of combined df.
'''

import pandas as pd

df = pd.DataFrame({'Date':['10/2/2011', '12/2/2011', '13/2/2011', '14/2/2011'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
					'Cost':[10000, 5000, 15000, 2000]})

print(df)

# Custom function to insert row in the dataframe
def Insert_row(row_number, df, row_value):
	# Start of upper half
	start_upper = 0
	# End of upper half
	end_upper = row_number
	# Start value of lower half
	start_lower = row_number
	# End value of lower half
	end_lower = df.shape[0]
	# Create a list of upper_half index using iterator from range()
	upper_half = [*range(start_upper, end_upper, 1)]
	# Create a list of lower_half index
	lower_half = [*range(start_lower, end_lower, 1)]
	# Increment the value of lower half by 1 using __add__() method
	lower_half = [x.__add__(1) for x in lower_half]
	# Combine the two lists
	index_ = upper_half + lower_half
	# Update the index of the dataframe
	df.index = index_
	# Insert a row at the end
	df.loc[row_number] = row_value
	# Sort the index labels
	df = df.sort_index()
	# return the dataframe
	return df

row_number = 2
row_value = ['11/2/2011', 'Wrestling', 12000]

if row_number > df.index.max()+1:
	print("Invalid row_number")
else:
	df2 = Insert_row(row_number, df, row_value)
	print(df2)


# 2. Using pd.concat()
df = pd.DataFrame({'Date':['10/2/2011', '12/2/2011', '13/2/2011', '14/2/2011'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
					'Cost':[10000, 5000, 15000, 2000]})
print(df)

def Insert_row_(row_number, df, row_value):
	df1 = df[0:row_number]
	df2 = df[row_number:]
	# Insert the row in the upper half as opposed to the end in prev case
	df1.loc[row_number]=row_value
	# Concat the two dataframes using pd.concat
	df_result = pd.concat([df1, df2])
	# Reindexing
	df_result.index = [*range(df_result.shape[0])]
	return df_result

# Row to insert 
row_number = 2
row_value = ['11/2/2011', 'Wrestling', 12000]

if row_number > df.index.max()+1:
	print("Invalid row_number")
else:

	df = Insert_row_(2, df, row_value)
	print(df)

