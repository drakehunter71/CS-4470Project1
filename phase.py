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

    temp = pd.DataFrame(columns=["Year", "Phases", "count"])

    for year in years:
        d = df[df["Start Year"] == year]["Phases"].value_counts().reset_index()
        d["Year"] = year
        for val in ["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"]:
            temp = pd.concat([temp, d[d["Phases"] == val]])

    print(temp)

    sns.barplot(temp, x="Year", y="count", hue="Phases", palette="flare")
    plt.title("Distribution of " + titles[indicator] + " Studies by Phase Annually")
    plt.show()

    indicator += 1