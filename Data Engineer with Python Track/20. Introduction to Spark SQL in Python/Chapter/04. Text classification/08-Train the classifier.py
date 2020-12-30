'''
Train the classifier


The dataframe df_trainset you created in the previous exercise is available. You're now going to use it to train a Logistic Regression Classifier.

Instructions
100 XP

- Import the Logistic Regression Classifier.
- Instantiate the classifier. Set maximum iterations to 100, the regularization parameter to 0.4, and the elastic net parameter to 0.0.
- Train the classifier on the trainset.
- Print the number of training iterations

'''
# Import the logistic regression classifier
from pyspark.ml.classification import LogisticRegression

# Instantiate logistic setting elasticnet to 0.0
logistic = LogisticRegression(maxIter=100, regParam=0.4, elasticNetParam=0.0)

# Train the logistic classifer on the trainset
df_fitted = logistic.fit(df_trainset)

# Print the number of training iterations
print("Training iterations: ", df_fitted.summary.totalIterations)
