'''
Machine Learning Pipelines


In the next two chapters you'll step through every stage of the machine learning pipeline, from data intake to model evaluation. Let's get to it!

At the core of the pyspark.ml module are the Transformer and Estimator classes. Almost every other class in the module behaves similarly to these two basic classes.

Transformer classes have a .transform() method that takes a DataFrame and returns a new DataFrame; usually the original one with a new column appended. For example, you might use the class Bucketizer to create discrete bins from a continuous feature or the class PCA to reduce the dimensionality of your dataset using principal component analysis.

Estimator classes all implement a .fit() method. These methods also take a DataFrame, but instead of returning another DataFrame they return a model object. This can be something like a StringIndexerModel for including categorical data saved as strings in your models, or a RandomForestModel that uses the random forest algorithm for classification or regression.

Which of the following is not true about machine learning in Spark?

Answer the question
50XP

Possible Answers :

    - Spark's algorithms give better results than other algorithms.

    - Working in Spark allows you to create reproducible machine learning pipelines.

    - Machine learning pipelines in Spark are made up of Transformers and Estimators.

    - PySpark uses the pyspark.ml submodule to interface with Spark's machine learning routines.

Answer : Spark's algorithms give better results than other algorithms.

'''
