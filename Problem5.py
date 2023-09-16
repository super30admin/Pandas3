'''
1. Sorting rows of a dataframe on one column
2. Sorting on more than one columns
3. If we want NA values on top use na_position parameter
'''

import pandas as pd

data = {'name': ['Simon', 'Marsh', 'Gaurav', 'Alex', 'Selena'],
		'Maths': [8, 5, 6, 9, 7],
		'Science': [7, 9, 5, 4, 7],
		'English': [7, 4, 7, 6, 8]}

df = pd.DataFrame(data)

# 1. Sort the dataframe’s rows by Science, in ascending order
a = df.sort_values(by ='Science', ascending = True)
print("Sorting rows by Science in ascending order:\n \n", a)

# 2. Sort the dataframe’s rows by Science, Maths, in descending order
b = df.sort_values(by =['Science','Maths'], ascending = False)
print("Sorting rows by Science, Maths in descending order:\n \n", b)


# 3. If we want missing values first in sorted df
data = {'name': ['Simon', 'Marsh', 'Gaurav', 'Alex', 'Selena'],
		'Maths': [8, 5, 6, 9, 7],
		'Science': [7, 9, 5, pd.NA, 7],
		'English': [7, 4, 7, 6, 8]}
df = pd.DataFrame(data)

a = df.sort_values(by ='Science', na_position ='first' )
print(a)
