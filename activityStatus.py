import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

c = pd.read_csv("Data/covid.csv")
bc = pd.read_csv("Data/breastCancer.csv")

cCount = pd.DataFrame(columns=["Study Status", "count", "disease"])
bcCount = pd.DataFrame(columns=["Study Status", "count", "disease"])

order = ["NOT_YET_RECRUITING", "RECRUITING", "ENROLLING_BY_INVITATION", "ACTIVE_NOT_RECRUITING", "cOMPLETED", "TERMINATED",
         "SUSPENDED", "WITHDRAWN", "UNKNOWN"]

temp = c["Study Status"].value_counts().reset_index()
temp["disease"] = "Covid"
for cat in order:
    cCount = pd.concat([cCount, temp[temp["Study Status"] == cat]])

bcCount = bc["Study Status"].value_counts().reset_index()
bcCount["disease"] = "Breast Cancer"

count1 = pd.concat([cCount, bcCount])

sns.barplot(count1, x="Study Status", y="count", hue="disease", palette="flare")
plt.title("Distribution of Studies by Status")
plt.show()