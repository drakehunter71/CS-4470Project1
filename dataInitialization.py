import pandas as pd
import numpy as np

covid = pd.read_csv("Data/covidOriginal.csv")
breastCancer = pd.read_csv("Data/breastCancerOriginal.csv")

def description(df):
    variables = []
    dtypes = []
    count = []
    unique = []
    missing = []
    for item in df.columns:
        variables.append(item)
        dtypes.append(df[item].dtype)
        count.append(len(df[item]))
        unique.append(len(df[item].unique()))
        missing.append(df[item].isna().sum())
    # creating an output df
    output = pd.DataFrame({'variable': variables, 'dtype': dtypes, 'count': count, 'unique': unique, 'missing value': missing
    })
    return output

covid.drop(columns=["Study Title", "Study URL", "Acronym", "Brief Summary"], inplace=True)
breastCancer.drop(columns=["Study Title", "Study URL", "Acronym", "Brief Summary"], inplace=True)

for df in [covid, breastCancer]:
    df["Has Secondary Outcome"] = np.where(df["Secondary Outcome Measures"].notnull(), 1, 0)
    df["Has More Than 2 Outcomes"] = np.where(df["Other Outcome Measures"].notnull(), 1, 0)
    df["Has Collaborators"] = np.where(df['Collaborators'].notnull(), 1, 0)
    df["Has Study Docs"] = np.where(df["Study Documents"].notnull(), 1, 0)

print(description(covid))
print(description(breastCancer))

covid.to_csv("Data/covid.csv")
breastCancer.to_csv("Data/breastCancer.csv")