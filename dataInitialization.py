import pandas as pd
import numpy as np
from numpy import NaN
from datetime import date

# Read in original datasets
covid = pd.read_csv("Data/covidOriginal.csv")
breastCancer = pd.read_csv("Data/breastCancerOriginal.csv")


# Function from class to describe pandas database objects
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
    output = pd.DataFrame(
        {
            "variable": variables,
            "dtype": dtypes,
            "count": count,
            "unique": unique,
            "missing value": missing,
        }
    )
    return output


# Dropping irrelevant attributes
covid.drop(
    columns=["Study Title", "Study URL", "Acronym", "Brief Summary"], inplace=True
)
breastCancer.drop(
    columns=["Study Title", "Study URL", "Acronym", "Brief Summary"], inplace=True
)

# Define new categorical variables for attributes that are filled optionally (presence of a value may indicate a more in depth study)
for df in [covid, breastCancer]:
    df["Has Secondary Outcome"] = np.where(
        df["Secondary Outcome Measures"].notnull(), "YES", "NO"
    )
    df["Has More Than 2 Outcomes"] = np.where(
        df["Other Outcome Measures"].notnull(), "YES", "NO"
    )
    df["Has Collaborators"] = np.where(df["Collaborators"].notnull(), "YES", "NO")
    df["Has Study Docs"] = np.where(df["Study Documents"].notnull(), "YES", "NO")


# function used to convert the originally read in dates into date objects, retaining all missing values
def fixDate(val):
    if type(val) == str:
        l = val.split("-")
    else:
        return NaN

    if len(l) != 3:
        return date(int(l[0]), int(l[1]), 1)
    else:
        return date(int(l[0]), int(l[1]), int(l[2]))


# Create a list of attributes consisting of values of dates
dateAttributes = [
    "Start Date",
    "Primary Completion Date",
    "Completion Date",
    "First Posted",
    "Results First Posted",
    "Last Update Posted",
]

# Apply the previously defined function to all predifined attributes for both datasets
for df in [covid, breastCancer]:
    for att in dateAttributes:
        df[att] = df[att].apply(fixDate)
    df["Study Length"] = (
        pd.to_datetime(df["Completion Date"]) - pd.to_datetime(df["Start Date"])
    ).dt.days


# Creation of new categorical variable to help gorup abservations annually
cutoffs = [date(2021, 1, 1), date(2022, 1, 1), date(2023, 1, 1), date(2024, 1, 1)]
cutoffsText = ["2020", "2021", "2022", "2023", "2024"]


def timeGroup(val):
    i = 0
    for cutoff in cutoffs:
        if val < cutoff:
            return cutoffsText[i]
        elif val > date(2023, 12, 31):
            return cutoffsText[4]
        i += 1


covid["Start Year"] = covid["Start Date"].apply(timeGroup)
breastCancer["Start Year"] = breastCancer["Start Date"].apply(timeGroup)

# cnct = covid["NCT Number"]
# bcnct = breastCancer["NCT Number"]

# events = pd.read_csv("Data/reportedEventsOriginal.txt", delimiter="|")
# events = events[events["nct_id"].isin(cnct) | events["nct_id"].isin(bcnct)]

# Output the cleaned datasets to new csv files
covid.to_csv("Data/covid.csv")
breastCancer.to_csv("Data/breastCancer.csv")
# events.to_csv("Data/reportedEvents.csv")
