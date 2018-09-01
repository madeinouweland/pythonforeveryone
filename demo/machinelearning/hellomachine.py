from sklearn import tree
features = [[6, 4], [7, 5], [8, 6], [4, 6], [5, 6]] # weight, strings
labels = ["bass guitar", "bass guitar", "bass guitar", "electrical guitar", "electrical guitar"]
classifier = tree.DecisionTreeClassifier()
classifier.fit(features, labels)
print(classifier.predict([[8, 5]])) # weight, strings
print(classifier.predict([[3, 6]])) # weight, strings
