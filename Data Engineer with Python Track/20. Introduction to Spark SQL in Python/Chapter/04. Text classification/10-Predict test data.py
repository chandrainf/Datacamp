'''
Predict test data


A fitted logistic model df_fitted is available. A dataframe df_testset is available containing test data for this model. A variable fields is available, containing the list ['prediction', 'label', 'endword', 'doc', 'probability']; this is used to specify which prediction fields to print.

Instructions
100 XP

- Apply the model to the data in df_testset.
- Print "incorrect" if prediction does not match label.

'''
# Apply the model to the test data
predictions = df_fitted.transform(df_testset).select(fields)

# Print incorrect if prediction does not match label
for x in predictions.take(8):
    print()
    if x.label != int(x.prediction):
        print("INCORRECT ==> ")
    for y in fields:
        print(y, ":", x[y])
