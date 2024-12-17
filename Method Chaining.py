import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals.sort_values(by='weight', ascending=False,inplace=True)
    df=animals[['name']][animals['weight'] > 100]
    return df
