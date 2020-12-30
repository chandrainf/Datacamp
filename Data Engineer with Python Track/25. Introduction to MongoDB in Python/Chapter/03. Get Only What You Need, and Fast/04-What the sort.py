'''
What the sort?


This block prints out the first five projections of a sorted query. What "sort" argument fills the blank?

    docs = list(db.laureates.find(
        {"born": {"$gte": "1900"}, "prizes.year": {"$gte": "1954"}},
        {"born": 1, "prizes.year": 1, "_id": 0},
        sort=____))
    for doc in docs[:5]:
        print(doc)


    {'born': '1916-08-25', 'prizes': [{'year': '1954'}]}
    {'born': '1915-06-15', 'prizes': [{'year': '1954'}]}
    {'born': '1901-02-28', 'prizes': [{'year': '1954'}, {'year': '1962'}]}
    {'born': '1913-07-12', 'prizes': [{'year': '1955'}]}
    {'born': '1911-01-26', 'prizes': [{'year': '1955'}]}


Instructions
50 XP

Possible Answers

    - [("prizes.year", 1), ("born", -1)]

    - {"prizes.year": 1, "born": -1}

    - None

    - [("prizes.year", 1)]

Answer : [("prizes.year", 1), ("born", -1)]

'''
