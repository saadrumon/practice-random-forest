import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

features = pd.read_csv('data/temps.csv')

features = pd.get_dummies(features)
labels = np.array(features['actual'])
features = features.drop('actual', axis=1)
feature_list = list(features.columns)
features = np.array(features)

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.25, random_state=42)

baseline_preds = test_features[:, feature_list.index('average')]
baseline_errors = abs(baseline_preds - test_labels)

rf = RandomForestRegressor(n_estimators=1000, random_state=42)

rf.fit(train_features, train_labels)

predictions = rf.predict(test_features)

errors = abs(predictions - test_labels)
mape = (errors / test_labels) * 100
accuracy = 100 - np.mean(mape)
print('Accuracy: ', round(accuracy, 2), '%')

