'''
Print word frequencies


After combining the values (counts) with the same key (word), you'll print the word frequencies using the take(N) action. You could have used the collect() action but as a best practice, it is not recommended as collect() returns all the elements from your RDD. You'll use take(N) instead, to return N elements from your RDD.

What if we want to return the top 10 words? For this first, you'll need to swap the key (word) and values (counts) so that keys is count and value is the word. After you swap the key and value in the tuple, you'll sort the pair RDD based on the key (count) and print the top 10 words in descending order.

You already have a SparkContext sc and resultRDD available in your workspace.

Instructions
100 XP

- Print the first 10 words and their frequencies from the resultRDD.
- Swap the keys and values in the resultRDD.
- Sort the keys according to descending order.
- Print the top 10 most frequent words and their frequencies.

'''
# Display the first 10 words and their frequencies
for word in resultRDD.take(10):
    print(word)

# Swap the keys and values
resultRDD_swap = resultRDD.map(lambda x: (x[1], x[0]))

# Sort the keys in descending order
resultRDD_swap_sort = resultRDD_swap.sortByKey(ascending=False)

# Show the top 10 most frequent words and their frequencies
for word in resultRDD_swap_sort.take(10):
    print("{} has {} counts". format(word[1], word[0]))
