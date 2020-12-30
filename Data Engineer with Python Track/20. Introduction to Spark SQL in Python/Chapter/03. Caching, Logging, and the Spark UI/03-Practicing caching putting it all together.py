'''
Practicing caching: putting it all together


What was the best approach to caching df1 and df2 and why?

Your results will vary; but here is one (random) result for each of the two approaches:

First answer (cache df1):

    df1_1st : 2.4s
    df1_2nd : 0.1s
    df2_1st : 0.3s
    df2_2nd : 0.2s
    Overall elapsed : 3.9

Second answer (cache df2):

    df1_1st : 2.3s
    df1_2nd : 1.1s
    df2_1st : 1.7s
    df2_2nd : 0.1s
    Overall elapsed : 6.4

Answer the question
50XP
Possible Answers

    - Cache df1, because it improves time of the first action the most.

    - Cache df2, because it also causes df1 to be cached.

    - Cache df1, because it improves the time of the 2nd, 3rd, and 4th action.

    - Cache df2, because it gives the best overall time.

Answer : Cache df1, because it improves the time of the 2nd, 3rd, and 4th action.

'''
