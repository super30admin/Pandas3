# Problem 3 :Create a list from rows in Pandas dataframe
# In order to iterate over the rows of the Pandas dataframe we can use DataFrame.iterrows() function 
# and then we can append the data of each row to the end of the list.
# importing pandas as pd
import pandas as pd


df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
					'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],
					'Cost':[10000, 5000, 15000, 2000]})


print(df)

#create an empty list
Row_List=[]

for index, rows in df.iterrows():
    my_list=[rows.Date,rows.Event,rows.Cost]

Row_List.append(my_list)

print(Row_List)

# In order to iterate over the rows of the Pandas dataframe we can use 
# DataFrame.itertuples() function and then we can append the data of each row to the end of the list.

# Create an empty list
Row_list =[]

# Iterate over each row
for rows in df.itertuples():
	# Create list for the current row
	my_list =[rows.Date, rows.Event, rows.Cost]
	
	# append the list to the final list
	Row_list.append(my_list)

# Print the list
print(Row_list)
