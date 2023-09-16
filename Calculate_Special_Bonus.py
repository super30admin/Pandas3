import pandas as pd

#Approach - 1
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
     for i in range(len(employees)):
         print(employees.iloc[i]['employee_id'])
         if employees.iloc[i]['employee_id'] %2 == 0  or employees.iloc[i]['name'][0] == 'M':
            employees.iloc[i, employees.columns.get_loc('salary')] = 0
         return employees[['employee_id','salary']].rename(columns = {'salary':'bonus'}).sort_values(by = ['employee_id'])


#Approach - 2
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if (x['employee_id'] % 2  != 0) and (x['name'][0] != 'M') else 0, axis = 1)
    return employees[['employee_id','bonus']].sort_values('employee_id')
