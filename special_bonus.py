import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if x['employee_id'] % 2 != 0
    and not x['name'].startswith("M") else 0, axis = 1)

    return employees[['employee_id','bonus']].sort_values(by = ["employee_id"])










    # lst = []
    # for i in range(len(employees)):
    #     if employees['employee_id'][i] % 2 != 0 and employees['name'][i][0] != 'M':
    #         lst.append([employees['employee_id'][i],employees['salary'][i]])
    #     else:
    #         lst.append([employees['employee_id'][i],0])
    # return pd.DataFrame(lst,columns=["employee_id","bonus"]).sort_values(by=["employee_id"])
