import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].apply(helper_func)]

def helper_func(content):
    return any([x.startswith('DIAB1') for x in content.split()])

