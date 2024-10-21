import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    df=report.melt(id_vars='product')
    df.rename(columns={'variable':'quarter','value':'sales'},inplace=True)
    return df
    
