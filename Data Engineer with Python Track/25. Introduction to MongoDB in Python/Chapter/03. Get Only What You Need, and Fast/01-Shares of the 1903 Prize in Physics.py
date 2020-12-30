'''
Shares of the 1903 Prize in Physics


You want to examine the laureates of the 1903 prize in physics and how they split the prize. Here is a query without projection:

    db.laureates.find_one({"prizes": {"$elemMatch": {"category": "physics", "year": "1903"}}})

Which projection(s) will fetch ONLY the laureates' full names and prize share info? I encourage you to experiment with the console and re-familiarize yourself with the structure of laureate collection documents.

Instructions
50 XP

Possible Answers

    - ["firstname", "surname", "prizes"]

    - ["firstname", "surname", "prizes.share"]

    - {"firstname": 1, "surname": 1, "prizes.share": 1, "_id": 0}

    - All of the above

Answer : {"firstname": 1, "surname": 1, "prizes.share": 1, "_id": 0}

'''
