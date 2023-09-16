# Problem 4 :Ranking Rows of Pandas DataFrame
# To rank the rows of Pandas DataFrame we can use the DataFrame.rank() method which returns a rank of every respective index of a series passed. 
# import the required packages
import pandas as pd

# Define the dictionary for converting to dataframe
movies = {'Name': ['The Godfather', 'Bird Box', 'Fight Club'],
		'Year': ['1972', '2018', '1999'],
		'Rating': ['9.2', '6.8', '8.8']}

df = pd.DataFrame(movies)
print(df)

# Create a column Rating_Rank which contains
# the rank of each movie based on rating
df['Rating_Rank'] = df['Rating'].rank(ascending = 1)

# Set the index to newly created column, Rating_Rank
df = df.set_index('Rating_Rank')
print(df)


#Example 2
# Create a dictionary with student details
student_details = {'Name':['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind',
							'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'],
				'Subject':['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics',
							'Chemistry', 'Maths', 'Physics', 'Chemistry', 'Maths',
														'Physics', 'Chemistry'],
				'Marks':[80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70]
			}

# Convert dictionary to a DataFrame
df = pd.DataFrame(student_details)
print(df)

df['mark_rank']=df['Marks'].rank(ascending=0)
df=df.set_index('mark_rank')
df=df.sort_index()
print(df)