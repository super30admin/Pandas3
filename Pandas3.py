#Question 1 : 

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x : x['salary'] if x['employee_id'] % 2  and not x['name'].startswith('M') else 0 , axis = 1)
    print (employees)

    return employees[['employee_id','bonus']].sort_values('employee_id')


#Question 2  :

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()

    return users.sort_values('user_id')
    



#Question 3 : 

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients = patients[patients['conditions'].str.startswith('DIAB1') | patients['conditions'].str.contains(' DIAB1')]

    return patients