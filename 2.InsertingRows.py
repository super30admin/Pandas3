
import pandas as pd


df = pd.DataFrame({'Date':['10/2/2011', '12/2/2011', '13/2/2011', '14/2/2011'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
					'Cost':[10000, 5000, 15000, 2000]})
print(df)

# Function to insert row in the dataframe
def Insert_row(row_number, df, row_value):
	
	start_upper = 0
	end_upper = row_number
	start_lower = row_number
	end_lower = df.shape[0]

	upper_half = [*range(start_upper, end_upper, 1)]
	lower_half = [*range(start_lower, end_lower, 1)]

	lower_half = [x.__add__(1) for x in lower_half]
	index_ = upper_half + lower_half

	df.index = index_
	df.loc[row_number] = row_value

	df = df.sort_index()
	return df

row_number = 2
row_value = ['11/2/2011', 'Wrestling', 12000]

if row_number > df.index.max()+1:
	print("Invalid row_number")
else:
	
	df = Insert_row(row_number, df, row_value)
	print(df)

#Another customized function which will use Pandas.concat() function to insert a row at any given position in the dataframe.

def Insert_row_(row_number, df, row_value):
	
	df1 = df[0:row_number]
	df2 = df[row_number:]
	df1.loc[row_number]=row_value
	df_result = pd.concat([df1, df2])
	df_result.index = [*range(df_result.shape[0])]
	return df_result

row_number = 2
row_value = ['11/2/2011', 'Wrestling', 12000]
if row_number > df.index.max()+1:
	print("Invalid row_number")
else:
	df = Insert_row_(2, df, row_value)
	print(df)

