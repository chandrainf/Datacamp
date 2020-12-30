'''
Filtering Question #2


Consider the following Data Frame called users_df:

ID      Name	    Age	    State
140     George L	47	    Iowa
3260	Mary R	    34	    Vermont
18502	Audrey V	68	    Ohio
999     Rick W	    23	    California


If we wanted to return only the Name and State fields for any ID greater than 3000, which code snippet meets these requirements?

Answer the question
50XP

Possible Answers

    -users_df.filter('ID > 3000').select("Name", "State")

    -users_df.select("Name", "State").filter('ID > 3000')

    -users_df.filter(users_df.ID = 3260).filter(users_df.ID = 18502)

    -```users_df.select("Name", "State")

Answer : users_df.filter('ID > 3000').select("Name", "State")

'''
