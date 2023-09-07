'''
1. Ranking the rows of a dataframe using rank method
'''

import pandas as pd

movies = {'Name': ['The Godfather', 'Bird Box', 'Fight Club'],
		'Year': ['1972', '2018', '1999'],
		'Rating': ['9.2', '6.8', '8.8']}

df = pd.DataFrame(movies)
print(df)

# Create a column Rating_Rank which contains the rank of each movie based on rating in ascending order
df['Rating_Rank'] = df['Rating'].rank(ascending = True)
# Set the index to newly created column, Rating_Rank and sort on it
df = df.set_index('Rating_Rank')
df = df.sort_index()
print(df)

# Ex: 2 Rank the students based on the highest mark they have scored
student_details = {'Name':['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind',
							'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'],
				'Subject':['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics',
							'Chemistry', 'Maths', 'Physics', 'Chemistry', 'Maths',
														'Physics', 'Chemistry'],
				'Marks':[80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70]
			}
df = pd.DataFrame(student_details)
print(df)

df['Marks_Rank'] = df['Marks'].rank(ascending=False,method='min')
df = df.set_index('Marks_Rank')
df = df.sort_index()
print(df)



