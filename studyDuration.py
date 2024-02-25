import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from dataInitialization import description

covid = pd.read_csv("Data/covid.csv")
breastCancer = pd.read_csv("Data/breastCancer.csv")

# ['Unnamed: 0', 'NCT Number', 'Study Status', 'Study Results',
#        'Conditions', 'Interventions', 'Primary Outcome Measures',
#        'Secondary Outcome Measures', 'Other Outcome Measures', 'Sponsor',
#        'Collaborators', 'Sex', 'Age', 'Phases', 'Enrollment', 'Funder Type',
#        'Study Type', 'Study Design', 'Other IDs', 'Start Date',
#        'Primary Completion Date', 'Completion Date', 'First Posted',
#        'Results First Posted', 'Last Update Posted', 'Locations',
#        'Study Documents', 'Has Secondary Outcome', 'Has More Than 2 Outcomes',
#        'Has Collaborators', 'Has Study Docs', 'Study Length']

print(covid.columns)
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
plt.tight_layout()
plt.savefig("GraphImages/bothStudyLengthDensity.png")
plt.show()

for df in [covid, breastCancer]:
    for hue in [""]:
        sb.displot(data=df, x="Study Length", hue="Phases", kind="kde")
        plt.title("Study Length KDE")
        plt.xlabel("Study Length (days)")
        plt.ylabel("Density")
        plt.show()
