# Sorting rows by Science
import pandas as pd

# create dataframe
data = {'name': ['Simon', 'Marsh', 'Gaurav', 'Alex', 'Selena'],
		'Maths': [8, 5, 6, 9, 7],
		'Science': [7, 9, 5, 4, 7],
		'English': [7, 4, 7, 6, 8]}

df = pd.DataFrame(data)

# Sort the dataframe’s rows by Science,
# in descending order
a = df.sort_values(by ='Science', ascending = False)
print("Sorting rows by Science:\n \n", a)


# Sort rows by Maths and then by English in ascending order
b=df.sort_values(by=['Maths','English'], ascending=True)
print("Sorting rows by Maths & then english:\n \n", b)

#3: If you want missing values first.
c=df.sort_values(by='Science',na_position='first')
print(c)



