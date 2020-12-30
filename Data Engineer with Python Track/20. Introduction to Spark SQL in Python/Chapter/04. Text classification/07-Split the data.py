'''
Split the data


A dataframe df_examples is available having columns endword: string, features: vector, outvec: vector, and label: int. You're going to split it to obtain training and testing set, which you will use to train and test a classifier.

Instructions
100 XP

- Split the examples into train and test using a 80/20 split.
- Print the number of training examples.
- Print the number of test examples.

'''
# Split the examples into train and test, use 80/20 split
df_trainset, df_testset = df_examples.randomSplit((0.80, 0.20), 42)

# Print the number of training examples
print("Number training: ", df_trainset.count())

# Print the number of test examples
print("Number test: ", df_testset.count())
