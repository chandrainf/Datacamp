'''
Embedding aggregation expressions


The $expr operator allows embedding of aggregation expressions in a normal query (or in a $match stage). Which of the following expressions counts the number of laureate documents with string-valued bornCountries when passed to db.laureates.count_documents?

You can assume (and check!) that the following is true:

    assert all(isinstance(v, str) for v in db.laureates.distinct("bornCountry"))

Instructions
50 XP

Possible Answers

    - {"bornCountry": {"$in": db.laureates.distinct("bornCountry")}}

    - {"$expr": {"$in": ["$bornCountry", db.laureates.distinct("bornCountry")]}}

    - {"$expr": {"$eq": [{"$type": "$bornCountry"}, "string"]}}

    - {"bornCountry": {"$type": "string"}}

    - All of the above

Answer : All of the above

'''
