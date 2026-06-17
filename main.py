"Predicting paleoclimate using Alkane proxies from GC-MS data"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#Load Dataset
data = pd.read_csv("Alkane_Proxies.csv", sep="\t")
print(data.head())

#Features and Targets
X = data[['ACL', 'TAR', 'CPI', 'Paq', 'OEP']]
Y = data[['Plant_Type','Climate']]

# Train-Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)

#Prediction on a new sample data
New_Sample = pd.DataFrame([{'ACL': 31, 'TAR': 0.6, 'CPI': 4, 'Paq': 0.4, 'OEP': 1}])

prediction = model.predict(New_Sample)
print("Prediction for plant type & climate:", prediction[0])
