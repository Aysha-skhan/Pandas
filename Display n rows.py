#Read only small chunk from data
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return(employees.head(n))
#where n is input
n=int(input('Enter no. of rows to display'))
