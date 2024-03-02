import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

c = pd.read_csv("Data/covid.csv")
bc = pd.read_csv("Data/breastCancer.csv")


def total(interventions):
    l = interventions.split("|")
    for intervention in l:
        t = intervention.split(":")[0]
        if t not in count.keys():
            count[t] = 1
        else:
            count[t] = count[t] + 1


count = {}
c["Interventions"].apply(total)
cCount = pd.DataFrame(
    {
        "Intervention": list(count.keys()),
        "count": list(count.values()),
        "Disease": ["Covid"] * len(list(count.keys())),
    }
)

count = {}
bc["Interventions"].apply(total)
bcCount = pd.DataFrame(
    {
        "Intervention": list(count.keys()),
        "Count": list(count.values()),
        "Disease": ["Breast cancer"] * len(list(count.keys())),
    }
)

counts = pd.concat([cCount, bcCount])

sns.barplot(counts, x="Intervention", y="count", hue="Disease", palette="flare")
plt.title("Distribution of Studies by Intervention Type(s)")
plt.xticks(rotation=45)
plt.show()
