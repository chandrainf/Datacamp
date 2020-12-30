'''
Field Paths and Sets


Previously, we confirmed -- via a Python loop -- that for each prize, either all laureates have a 1/3 share, or none do. Now, let's do this via an aggregation (result should be an empty list):

    list(db.prizes.aggregate([
        {"$project": {"allThree": {"$setEquals": [____, ____]},
                    "noneThree": {"$not": {"$setIsSubset": [____, ____]}}}},
        {"$match": {"$nor": [{"allThree": True}, {"noneThree": True}]}}]))

Which values fill the blanks?

Instructions
50 XP

Possible Answers

    - "$laureates.share", ["3"], ["3"], "$laureates.share"

    - "laureates.share", ["3"], ["3"], "laureates.share"

    - "laureates.share", {"3"}, {"3"}, "laureates.share"

    - "$laureates.share", {"3"}, {"3"}, "$laureates.share"

Answer : "$laureates.share", ["3"], ["3"], "$laureates.share"

'''
