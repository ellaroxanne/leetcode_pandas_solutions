import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals.sort_values(by = ['weight'], ascending = False)
    return pd.DataFrame(animals[animals['weight'] > 100]['name'])
