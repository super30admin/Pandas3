'''
1. Take name column and use the capitalize function to make the First letter of the first word of Name capital.
'''
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize() 
    return users.sort_values('user_id')