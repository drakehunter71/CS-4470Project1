import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

c = pd.read_csv("Data/covid.csv")
bc = pd.read_csv("Data/breastCancer.csv")

"""
def splitDesign(design):
    return(design.split("|")[i])

temp = pd.DataFrame(columns=["Study Design"])

i=0
temp["Study Design"] = c["Study Design"].apply(splitDesign)
print(temp["Study Design"].unique())

i=1
temp["Study Design"] = c["Study Design"].apply(splitDesign)
print(temp["Study Design"].unique())

i=2
temp["Study Design"] = c["Study Design"].apply(splitDesign)
print(temp["Study Design"].unique())

i=3
temp["Study Design"] = c["Study Design"].apply(splitDesign)
print(temp["Study Design"].unique())

"""

#Manipulate data to acquire a df with each attribute of design separated
def expand(design):
    values = [t.split(":")[1][1:] for t in design.split("|")]
    expDesign["Allocation"].append(values[0])
    expDesign["Intervention Model"].append(values[1])
    expDesign["Masking"].append(values[2])
    expDesign["Mask"].append(values[2].split(" ")[0])
    expDesign["Purpose"].append(values[3])

expDesign = {"Allocation" : [], "Intervention Model" : [], "Masking" : [], "Mask" : [], "Purpose" : []}
c["Study Design"].apply(expand)
cDesign = pd.DataFrame(expDesign)

expDesign = {"Allocation" : [], "Intervention Model" : [], "Masking" : [], "Mask" : [], "Purpose" : []}
bc["Study Design"].apply(expand)
bcDesign = pd.DataFrame(expDesign)

#Distribution Analysis

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