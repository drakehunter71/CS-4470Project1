import pandas as pd

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

print(description(covid))
print(description(breastCancer))

covid.drop(columns=["Study Title", "Study URL", "Acronym", "Brief Summary"], inplace=True)
breastCancer.drop(columns=["Study Title", "Study URL", "Acronym", "Brief Summary"], inplace=True)

covid.to_csv("Data/covid.csv")
breastCancer.to_csv("Data/breastCancer.csv")