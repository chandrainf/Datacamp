'''
"...it's the life in your years"


For the pipeline we developed in the last slide deck, I want you to replace the last ($bucket) stage with one such that, given the documents docs collected, we can get the following output:

    from operator import itemgetter

    print(max(docs, key=itemgetter("years")))
    print(min(docs, key=itemgetter("years")))

    {'firstname': 'Rita', 'surname': 'Levi-Montalcini', 'years': 103.0}
    {'firstname': 'Martin Luther', 'surname': 'King Jr.', 'years': 39.0}

You may assume that any earlier $project stage has been replaced by an equivalent $addFields stage.

Answer the question
50XP

Possible Answers

    - {"$project": {"years": 1, "firstname": 1, "surname": 1, "_id": 0}}

    - {"$addFields": {"firstname": 1, "surname": 1}}

    - {"$project": {"firstname": 1, "surname": 1}}

    - {"$project": {"firstname": 1, "surname": 1, "_id": 0}}
  
Answer : {"$project": {"years": 1, "firstname": 1, "surname": 1, "_id": 0}}

'''
