import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

c = pd.read_csv("Data/covid.csv")
bc = pd.read_csv("Data/breastCancer.csv")

cCount = c["Has Collaborators"].value_counts().reset_index()
cCount["Disease"] = "Covid"

bcCount = bc["Has Collaborators"].value_counts().reset_index()
bcCount["Disease"] = "Breast Cancer"

count = pd.concat([cCount, bcCount])

sns.barplot(count, x="Has Collaborators", y="count", hue="Disease", palette="flare")
plt.title("Distribution of Studies by Presence of Collaborators")
plt.show()

cFiltered = c[["Has Collaborators", "Study Results"]]
cProbs = pd.DataFrame(columns=["Has Collaborators", "Probability"])
for value in ["YES", "NO"]:
    temp = cFiltered[cFiltered["Has Collaborators"] == value]
    counts = temp["Study Results"].value_counts().reset_index()
    counts["Probability"] = round((counts["count"] / temp.shape[0]) * 100, 2)
    counts["Has Collaborators"] = value
    counts = counts.drop(columns=["count"])
    counts = counts[counts["Study Results"] == "YES"].drop(columns=["Study Results"])
    cProbs = pd.concat([cProbs, counts])
cProbs["Disease"] = "Covid"

bcFiltered = bc[["Has Collaborators", "Study Results"]]
bcProbs = pd.DataFrame(columns=["Has Collaborators", "Probability"])
for value in ["YES", "NO"]:
    temp = bcFiltered[bcFiltered["Has Collaborators"] == value]
    counts = temp["Study Results"].value_counts().reset_index()
    counts["Probability"] = round((counts["count"] / temp.shape[0]) * 100, 2)
    counts["Has Collaborators"] = value
    counts = counts.drop(columns=["count"])
    counts = counts[counts["Study Results"] == "YES"].drop(columns=["Study Results"])
    bcProbs = pd.concat([bcProbs, counts])
bcProbs["Disease"] = "Breast Cancer"

probs = pd.concat([cProbs, bcProbs])

sns.barplot(
    probs, x="Disease", y="Probability", hue="Has Collaborators", palette="flare"
)
plt.title("Probability of Results Being Posted by the Presence of Collaborators")
plt.show()
