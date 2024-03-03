import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

c = pd.read_csv("Data/covid.csv")
bc = pd.read_csv("Data/breastCancer.csv")


#Number of Trials by Phase
cTemp = c["Phases"].value_counts().reset_index()
cTemp["disease"] = "Covid"
cCount = pd.DataFrame(columns=["Phases", "count", "disease"])
for val in ["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"]:
    cCount = pd.concat([cCount, cTemp[cTemp["Phases"] == val]])

bcCount = bc["Phases"].value_counts().reset_index()
bcCount["disease"] = "Breast cancer"

count1 = pd.concat([cCount, bcCount])

sns.barplot(count1, x="Phases", y="count", hue="disease", palette="flare")
plt.title("Distribution of Studies by Phase")
plt.show()

#Distribution of Phases over time
years = [2020, 2021, 2022, 2023, 2024]
titles = ["Covid", "Breast Cancer"]

indicator = 0
for df in [c, bc]:

    #dataframe to store counted data
    temp = pd.DataFrame(columns=["Year", "Phases", "count"])

    #Count by phase for each year, ordering and concatenating results to temp
    for year in years:
        d = df[df["Start Year"] == year]["Phases"].value_counts().reset_index()
        d["Year"] = year
        for val in ["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"]:
            temp = pd.concat([temp, d[d["Phases"] == val]])

    #Plot the results
    sns.barplot(temp, x="Year", y="count", hue="Phases", palette="flare")
    plt.title("Distribution of " + titles[indicator] + " Studies by Phase Annually")
    plt.show()

    indicator += 1

cFiltered = c[c["Past Completion"] >= 365]
bcFiltered = bc[bc["Past Completion"] >= 365]

cProbs = pd.DataFrame(columns=["Phases", "Probability"])
bcProbs = pd.DataFrame(columns=["Phases", "Probability"])
for value in ["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"]:
    tempC = c[c["Phases"] == value]
    cCounts = tempC["Study Results"].value_counts().reset_index()
    cCounts["Probability"] = round((cCounts['count']/tempC.shape[0])*100,2)
    if cCounts.shape[0] == 1:
        cCounts["Study Results"] = "YES"
        cCounts["Probability"] = 0
    cCounts = cCounts[cCounts["Study Results"] == "YES"].drop(columns=["count", "Study Results"])
    cCounts["Phases"] = value
    cProbs = pd.concat([cProbs, cCounts])

    tempBC = bc[bc["Phases"] == value]
    bcCounts = tempBC["Study Results"].value_counts().reset_index()
    bcCounts["Probability"] = round((bcCounts['count']/tempBC.shape[0])*100,2)
    if bcCounts.shape[0] == 1:
        bcCounts["Study Results"] = "YES"
        bcCounts["Probability"] = 0
    bcCounts = bcCounts[bcCounts["Study Results"] == "YES"].drop(columns=["count", "Study Results"])
    bcCounts["Phases"] = value
    bcProbs = pd.concat([bcProbs, bcCounts])

cProbs["Disease"] = "Covid"
bcProbs["Disease"] = "Breast Cancer"

probs = pd.concat([cProbs, bcProbs])

sns.barplot(probs, x="Phases", y="Probability", hue="Disease", palette="flare")
plt.title("Probability of Results being Posted by Phase (Completed for at Least a Year)")
plt.xticks(rotation=45)
plt.show()