'''
Sharing in physics after World War II


What is the approximate ratio of the number of laureates who won an unshared ({"share": "1"}) prize in physics after World War II ({"year": {"$gte": "1945"}}) to the number of laureates who won a shared prize in physics after World War II?

For reference, the code below determines the number of laureates who won a shared prize in physics before 1945.

    db.laureates.count_documents({
        "prizes": {"$elemMatch": {
            "category": "physics",
            "share": {"$ne": "1"},
            "year": {"$lt": "1945"}}}})

Instructions
50 XP

Possible Answers

    - 0.06

    - 0.13

    - 0.33

    - 0.50

Answer : 0.13

'''
