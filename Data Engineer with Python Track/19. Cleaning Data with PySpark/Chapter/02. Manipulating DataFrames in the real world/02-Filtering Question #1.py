'''
Filtering Question #1


Consider the following Data Frame called users_df:

ID	        Name	    Age	    State
140	        George L	47	    Iowa
3260	    Mary R	    34	    Vermont
18502	    null	    68	    Ohio
999	        Rick W	    23	    California

If you wanted to return only the entries without nulls, which of following options would not work?

Answer the question
50XP

Possible Answers

    - users_df = users_df.filter(users_df.Name.isNotNull())

    - users_df = users_df.where(users_df.ID == 18502)

    - users_df = users_df.where(~ (users_df.ID == 18502) )

    - users_df = users_df.filter(~ col('Name').isNull())

Answer : users_df = users_df.where(users_df.ID == 18502)

'''
