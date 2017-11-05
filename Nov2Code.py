from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original')
# Display our dataset
mnist
X, y = mnist["data"], mnist["target"]
# Display each of our variables
X.shape
y.shape
# Split our data into training and test data
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
import numpy as np
# Randomly shuffle our dataset
shuffle_index = np.random.permutation(60000)
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]
# Detect all 5s in our dataset
y_train_5 = (y_train == 5)  # True for all 5s, False for all other digits.
y_test_5 = (y_test == 5)
# Fit the model using the above classifier
from sklearn.linear_model import SGDClassifier
sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(X_train, y_train_5)
# Get our results
sgd_clf.predict([some_digit])
# Get our results from cross-validation
from sklearn.model_selection import cross_val_score
cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring="accuracy")


