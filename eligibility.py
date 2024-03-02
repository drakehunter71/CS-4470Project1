import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

c = pd.read_csv("Data/covid.csv")
bc = pd.read_csv("Data/breastCancer.csv")

cSex = c["Sex"].value_counts().reset_index()
cSex["Disease"] = "Covid"

bcSex = bc["Sex"].value_counts().reset_index()
bcSex["Disease"] = "Breast Cancer"

sex = pd.concat([cSex, bcSex])

sns.barplot(sex, x="Sex", y="count", hue="Disease", palette="flare")
plt.title("Distribution of Studies by Sex")
plt.show()

# filtered = sex[sex["Sex"] != "ALL"]
# sns.barplot(filtered, x="Sex", y="count", hue="Disease", palette="flare")
# plt.title("Distribution of Studies by Sex (Not Including Mixed Studies)")
# plt.show()


def counter(groupings):
    ages = groupings.split(",")
    for age in ages:
        t = age.replace(" ", "")
        if t not in ageCounts:
            ageCounts[t] = 1
        else:
            ageCounts[t] = ageCounts[t] + 1


ageCounts = {}
c["Age"].apply(counter)
cAge = pd.DataFrame(
    {
        "Age": list(ageCounts.keys()),
        "count": list(ageCounts.values()),
        "Disease": ["Covid"] * len(list(ageCounts.keys())),
    }
)

ageCounts = {}
bc["Age"].apply(counter)
bcAge = pd.DataFrame(
    {
        "Age": list(ageCounts.keys()),
        "count": list(ageCounts.values()),
        "Disease": ["Breast Cancer"] * len(list(ageCounts.keys())),
    }
)

age = pd.concat([cAge, bcAge])

sns.barplot(age, x="Age", y="count", hue="Disease", palette="flare")
plt.title("Distribution of Studies by Age Grouping")
plt.show()
