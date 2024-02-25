import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from dataInitialization import description

covid = pd.read_csv("Data/covid.csv")
breastCancer = pd.read_csv("Data/breastCancer.csv")

[
    "NCT Number",
    "Study Title",
    "Study URL",
    "Acronym",
    "Study Status",
    "Brief Summary",
    "Study Results",
    "Conditions",
    "Interventions",
    "Primary Outcome Measures",
    "Secondary Outcome Measures",
    "Other Outcome Measures",
    "Sponsor",
    "Collaborators",
    "Sex",
    "Age",
    "Phases",
    "Enrollment",
    "Funder Type",
    "Study Type",
    "Study Design",
    "Other IDs",
    "Start Date",
    "Primary Completion Date",
    "Completion Date",
    "First Posted",
    "Results First Posted",
    "Last Update Posted",
    "Locations",
    "Study Documents",
    "Study Length",
]
print("Covid")
print(description(covid))
print("")
print("BreatCancer")
print(description(breastCancer))

import seaborn as sb
import matplotlib.pyplot as plt

covid["Dataset"] = "COVID"
breastCancer["Dataset"] = "Breast Cancer"

combined_df = pd.concat([covid, breastCancer])

sb.displot(data=combined_df, x="Study Length", hue="Dataset", kind="kde")
plt.title("Study Length KDE")
plt.xlabel("Study Length (days)")
plt.ylabel("Density")
plt.show()
