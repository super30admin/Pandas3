import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    #'yes' if cond.startswith('DIAB1') else 'no'
    patients = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    return patients
