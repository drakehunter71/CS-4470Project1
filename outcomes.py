import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

c = pd.read_csv("Data/covid.csv")
bc = pd.read_csv("Data/breastCancer.csv")

cCount = c["Has Secondary Outcome"].value_counts().reset_index()
cCount["Disease"] = "Covid"

bcCount = bc["Has Secondary Outcome"].value_counts().reset_index()
bcCount["Disease"] = "Breast Cancer"

count = pd.concat([cCount, bcCount])
"""
sns.barplot(count, x="Has Secondary Outcome", y="count", hue="Disease", palette="flare")
plt.title("Distribution of Studies by Presence of a Secondary Outcome")
plt.show()
"""

cCount = c["Has More Than 2 Outcomes"].value_counts().reset_index()
cCount["Disease"] = "Covid"
cCount = pd.concat([cCount[cCount["Has More Than 2 Outcomes"] == "YES"], cCount[cCount["Has More Than 2 Outcomes"] == "NO"]])

bcCount = bc["Has More Than 2 Outcomes"].value_counts().reset_index()
bcCount["Disease"] = "Breast Cancer"

count = pd.concat([cCount, bcCount])
"""
sns.barplot(count, x="Has More Than 2 Outcomes", y="count", hue="Disease", palette="flare")
plt.title("Distribution of Studies by Presence of Three or More Outcomes")
plt.show()
"""

cFiltered = c[["Has Secondary Outcome", "Study Results"]]
cProbs = pd.DataFrame(columns=["Has Secondary Outcome", "Probability"])
for value in ["YES", "NO"]:
    temp = cFiltered[cFiltered["Has Secondary Outcome"] == value]
    counts = temp["Study Results"].value_counts().reset_index()
    counts["Probability"] = round((counts["count"]/temp.shape[0])*100, 2)
    counts["Has Secondary Outcome"] = value
    counts = counts.drop(columns=["count"])
    counts = counts[counts["Study Results"] == "YES"].drop(columns=["Study Results"])
    cProbs = pd.concat([cProbs, counts])
cProbs["Disease"] = "Covid"

bcFiltered = bc[["Has Secondary Outcome", "Study Results"]]
bcProbs = pd.DataFrame(columns=["Has Secondary Outcome", "Probability"])
for value in ["YES", "NO"]:
    temp = bcFiltered[bcFiltered["Has Secondary Outcome"] == value]
    counts = temp["Study Results"].value_counts().reset_index()
    counts["Probability"] = round((counts["count"]/temp.shape[0])*100, 2)
    counts["Has Secondary Outcome"] = value
    counts = counts.drop(columns=["count"])
    counts = counts[counts["Study Results"] == "YES"].drop(columns=["Study Results"])
    bcProbs = pd.concat([bcProbs, counts])
bcProbs["Disease"] = "Breast Cancer"

probs = pd.concat([cProbs, bcProbs])

sns.barplot(probs, x="Disease", y="Probability", hue="Has Secondary Outcome", palette="flare")
plt.title("Probability of Results Being Posted by the Presence of a Secondary Outcome")
plt.show()

cFiltered = c[["Has More Than 2 Outcomes", "Study Results"]]
cProbs = pd.DataFrame(columns=["Has More Than 2 Outcomes", "Probability"])
for value in ["YES", "NO"]:
    temp = cFiltered[cFiltered["Has More Than 2 Outcomes"] == value]
    counts = temp["Study Results"].value_counts().reset_index()
    counts["Probability"] = round((counts["count"]/temp.shape[0])*100, 2)
    counts["Has More Than 2 Outcomes"] = value
    counts = counts.drop(columns=["count"])
    counts = counts[counts["Study Results"] == "YES"].drop(columns=["Study Results"])
    cProbs = pd.concat([cProbs, counts])
cProbs["Disease"] = "Covid"

bcFiltered = bc[["Has More Than 2 Outcomes", "Study Results"]]
bcProbs = pd.DataFrame(columns=["Has More Than 2 Outcomes", "Probability"])
for value in ["YES", "NO"]:
    temp = bcFiltered[bcFiltered["Has More Than 2 Outcomes"] == value]
    counts = temp["Study Results"].value_counts().reset_index()
    counts["Probability"] = round((counts["count"]/temp.shape[0])*100, 2)
    counts["Has More Than 2 Outcomes"] = value
    counts = counts.drop(columns=["count"])
    counts = counts[counts["Study Results"] == "YES"].drop(columns=["Study Results"])
    bcProbs = pd.concat([bcProbs, counts])
bcProbs["Disease"] = "Breast Cancer"

probs = pd.concat([cProbs, bcProbs])

sns.barplot(probs, x="Disease", y="Probability", hue="Has More Than 2 Outcomes", palette="flare")
plt.title("Probability of Results Being Posted by the Presence More than 2 Outcomes")
plt.show()