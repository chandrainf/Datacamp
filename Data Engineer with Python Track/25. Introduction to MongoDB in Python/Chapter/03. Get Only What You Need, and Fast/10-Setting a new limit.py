'''
Setting a new limit?


How many documents does the following expression return?

    list(db.prizes.find({"category": "economics"},
                        {"year": 1, "_id": 0})
        .sort("year")
        .limit(3)
        .limit(5))

Instructions
50 XP

Possible Answers

    - 3: the first call to limit takes precedence

    - 5: the second call to limit overrides the first

    - none: instead, an error is raised

Answer : 5: the second call to limit overrides the first

'''
