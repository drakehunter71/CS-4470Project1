import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date


c = pd.read_csv("Data/covid.csv")
bc = pd.read_csv("Data/breastCancer.csv")

def timeDif(val):
    exp = val.split("-")
    day = date(int(exp[0]), int(exp[1]), int(exp[2]))
    return (date.today()-day).days

c["Past Completion"] = c["Completion Date"].apply(timeDif)
bc["Past Completion"] = bc["Completion Date"].apply(timeDif)

cFiltered = c[c["Past Completion"] >= 365]
bcFiltered = bc[bc["Past Completion"] >= 365]

cCount = cFiltered["Study Results"].value_counts().reset_index()
cCount["Disease"] = "Covid"

bcCount = bcFiltered["Study Results"].value_counts().reset_index()
bcCount["Disease"] = "Breast Cancer"

count = pd.concat([cCount, bcCount])

sns.barplot(count, x="Study Results", y="count", hue="Disease", palette="flare")
plt.title("Distribution of Studies by Presence of Results")
plt.show()

years = [2020, 2021, 2022, 2023]

"""
for year in years:
    temp = cFiltered[cFiltered["Start Year"] == year]
    counts = temp["Study Results"].value_counts().reset_index()
    if counts.shape[0] == 1:
        percent = 0
    else:
        percent = round((counts[counts["Study Results"] == "YES"]["count"].iloc[0]/temp.shape[0])*100, 2)
"""

cTemp = cFiltered[["Start Year", "Study Results"]]
cProbs = pd.DataFrame(columns=["Start Year", "Probability"])
for year in years:
    temp = cTemp[cTemp["Start Year"] == year]
    counts = temp["Study Results"].value_counts().reset_index()
    counts["Probability"] = round((counts["count"]/temp.shape[0])*100, 2)
    counts["Start Year"] = year
    counts = counts.drop(columns=["count"])
    counts = counts[counts["Study Results"] == "YES"].drop(columns=["Study Results"])
    cProbs = pd.concat([cProbs, counts])
cProbs["Disease"] = "Covid"
    
bcTemp = bcFiltered[["Start Year", "Study Results"]]
bcProbs = pd.DataFrame(columns=["Start Year", "Probability"])
for year in years:
    temp = bcTemp[bcTemp["Start Year"] == year]
    counts = temp["Study Results"].value_counts().reset_index()
    counts["Probability"] = round((counts["count"]/temp.shape[0])*100, 2)
    counts["Start Year"] = year
    counts = counts.drop(columns=["count"])
    counts = counts[counts["Study Results"] == "YES"].drop(columns=["Study Results"])
    bcProbs = pd.concat([bcProbs, counts])
bcProbs["Disease"] = "Breast Cancer"

probs = pd.concat([cProbs, bcProbs])

sns.barplot(probs, x="Disease", y="Probability", hue="Start Year", palette="flare")
plt.title("Probability of Results Being Posted by Start Year (Completed for at Least a Year)")
plt.show()