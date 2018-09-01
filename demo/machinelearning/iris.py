import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()

test_idx = [0,50,60]

# training datasets
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

classifier = tree.DecisionTreeClassifier()
classifier.fit(train_data, train_target)

print(test_target)
print(classifier.predict(test_data))

import graphviz
dot_data = tree.export_graphviz(classifier, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")
