'''
Test vs Train
After you've cleaned your data and gotten it ready for modeling, one of the most important steps is to split the data into a test set and a train set. After that, don't touch your test data until you think you have a good model! As you're building models and forming hypotheses, you can test them on your training data to get an idea of their performance.

Once you've got your favorite model, you can see how well it predicts the new data in your test set. This never-before-seen data will give you a much more realistic idea of your model's performance in the real world when you're trying to predict or classify new data.

In Spark it's important to make sure you split the data after all the transformations. This is because operations like StringIndexer don't always produce the same index even when given the same list of strings.

Why is it important to use a test set in model evaluation?

Answer the question
50XP

Possible Answers

    - Evaluating your model improves its accuracy.

    - By evaluating your model with a test set you can get a good idea of performance on new data.

    - Using a test set lets you check your code for errors.

Answer : By evaluating your model with a test set you can get a good idea of performance on new data.

'''
