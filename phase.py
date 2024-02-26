import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

c = pd.read_csv("Data/covid.csv")
bc = pd.read_csv("Data/breastCancer.csv")

cTemp = c["Phases"].value_counts().reset_index()
cTemp["disease"] = "Covid"
cCount = pd.DataFrame(columns=["Phases", "count", "disease"])
for val in ["EARLY_PHASE1", "PHASE1", "PHASE1|PHASE2", "PHASE2", "PHASE2|PHASE3", "PHASE3", "PHASE4"]:
    cCount = pd.concat([cCount, cTemp[cTemp["Phases"] == val]])

bcCount = bc["Phases"].value_counts().reset_index()
bcCount["disease"] = "Breast cancer"

count = pd.concat([cCount, bcCount])

sns.barplot(count, x="Phases", y="count", hue="disease", palette="flare")
plt.title("Distribution of Studies by Phase")
plt.show()