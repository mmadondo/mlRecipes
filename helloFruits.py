from sklearn import tree
import matplotlib.pyplot as plt
#training data to classify fruits: 
# Examples
# Weight Texture Label
# 150g   Bumpy   Orange
# 170g   Bumpy   Orange
# 140g   Smooth  Apple
# 130g   Smooth  Apple

# features: 1 = smooth and 0 = bumpy
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# labels: 0 is an apple and 1 is an orange
labels = [0, 0, 1, 1]

#train classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

#Make prediction using test fruit
print(clf.predict([[160, 0]]))
