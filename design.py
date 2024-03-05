import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

c = pd.read_csv("Data/covid.csv")
bc = pd.read_csv("Data/breastCancer.csv")


# Manipulate data to acquire a df with each attribute of design separated
def expand(design):
    values = [t.split(":")[1][1:] for t in design.split("|")]
    expDesign["Allocation"].append(values[0])
    expDesign["Intervention Model"].append(values[1])
    expDesign["Masking"].append(values[2])
    expDesign["Mask"].append(values[2].split(" ")[0])
    expDesign["Purpose"].append(values[3])


expDesign = {
    "Allocation": [],
    "Intervention Model": [],
    "Masking": [],
    "Mask": [],
    "Purpose": [],
}
c["Study Design"].apply(expand)
cDesign = pd.DataFrame(expDesign)

expDesign = {
    "Allocation": [],
    "Intervention Model": [],
    "Masking": [],
    "Mask": [],
    "Purpose": [],
}
bc["Study Design"].apply(expand)
bcDesign = pd.DataFrame(expDesign)
bcDesign["Allocation"] = bcDesign["Allocation"].replace("", "NA")

# Distribution Analysis

for attribute in ["Allocation", "Intervention Model", "Mask", "Purpose"]:
    cTemp = cDesign[attribute].value_counts().reset_index()
    cTemp["Disease"] = "Covid"

    bcTemp = bcDesign[attribute].value_counts().reset_index()
    bcTemp["Disease"] = "Breast cancer"

    temp = pd.concat([cTemp, bcTemp])

    sns.barplot(temp, x=attribute, y="count", hue="Disease", palette="flare")
    plt.xticks(rotation=45)
    plt.title("Distribution of Studies by " + attribute)
    plt.show()

# Compare design with results

cDesign["Has Results"] = c["Study Results"]
bcDesign["Has Results"] = bc["Study Results"]

for attribute in ["Allocation", "Intervention Model", "Mask", "Purpose"]:

    cTemp = cDesign[[attribute, "Has Results"]]
    cd = {attribute: [], "Probability": [], "Disease": []}
    for value in cTemp[attribute].unique():
        df = cTemp[cTemp[attribute] == value]
        n = df.shape[0]
        df = df["Has Results"].value_counts().reset_index()
        try:
            percent = round(
                ((df[df["Has Results"] == "YES"]["count"].iloc[0]) / n) * 100, 2
            )
        except:
            # Handles edge case of one category having no results at all
            percent = 0

        cd[attribute].append(value)
        cd["Probability"].append(percent)
        cd["Disease"].append("Covid")

    bcTemp = bcDesign[[attribute, "Has Results"]]
    bcd = {attribute: [], "Probability": [], "Disease": []}
    for value in bcTemp[attribute].unique():
        df = bcTemp[bcTemp[attribute] == value]
        n = df.shape[0]
        df = df["Has Results"].value_counts().reset_index()
        try:
            percent = round(
                ((df[df["Has Results"] == "YES"]["count"].iloc[0]) / n) * 100, 2
            )
        except:
            # Handles edge case of one category having no results at all
            percent = 0

        bcd[attribute].append(value)
        bcd["Probability"].append(percent)
        bcd["Disease"].append("Breast Cancer")

    cPercents = pd.DataFrame(cd)
    bcPercents = pd.DataFrame(bcd)

    percents = pd.concat([cPercents, bcPercents])

    sns.barplot(percents, x=attribute, y="Probability", hue="Disease", palette="flare")
    plt.title("Probability of Results by " + attribute)
    plt.xticks(rotation=45)
    plt.show()
