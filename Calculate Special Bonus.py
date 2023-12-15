import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if x['employee_id'] % 2 and not x['name'].startswith('M') else 0, axis =1)
    
    #print(employees[['employes_id','bonus']].sort_values(by = 'employee_id'))
    return employees[['employee_id','bonus']].sort_values(by = 'employee_id')

# def calculate_special_bonus(employeess: pd.DataFrame) -> pd.DataFrame:
#     mylist = []
#     for i in range(len(employeess)):
#         e_id = employeess['employees_id'][i]
#         salary = employeess['salary'][i]
#         if (employeess['employees_id'][i] % 2 !=0 and employeess['name'][i][0] != 'M'):
#             mylist.append([e_id,salary])
#         else:
#             mylist.append([e_id,0])
   
#     return pd.DataFrame(mylist,columns = ['employees_id', 'bonus']).sort_values(by = 'employees_id')
    