'''
Evaluate the classifier


A trained logistic regression model df_fitted is available. A dataframe df_testset is available containing test data for this model.

Instructions
100 XP

- Score the trained model on the test data.
- Print the Area Under Curve metric.

'''
# Score the model on test data
testSummary = df_fitted.evaluate(df_testset)

# Print the AUC metric
print("\ntest AUC: %.3f" % testSummary.areaUnderROC)
