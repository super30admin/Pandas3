#example:1

import pandas as pd

movies = {'Name': ['The Godfather', 'Bird Box', 'Fight Club'],
		'Year': ['1972', '2018', '1999'],
		'Rating': ['9.2', '6.8', '8.8']}

df = pd.DataFrame(movies)
print(df)
df['Rating_Rank'] = df['Rating'].rank(ascending = True)
df = df.set_index('Rating_Rank')
print(df)
df = df.sort_index()
print(df)



#example:2:- rank the students based on the highest mark they have scored.

student_details = {'Name':['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind',
							'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'],
				'Subject':['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics',
							'Chemistry', 'Maths', 'Physics', 'Chemistry', 'Maths',
														'Physics', 'Chemistry'],
				'Marks':[80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70]
			}

df = pd.DataFrame(student_details)
print(df)
df['Mark_Rank'] = df['Marks'].rank(ascending = False)
df = df.set_index('Mark_Rank')
print(df)
df = df.sort_index()
print(df)

