'''
High-share categories


In the year 3030, everybody wants to be a Nobel laureate. Over the last thousand years, many new categories have been added. You serve a MongoDB prizes collection with the same schema as we've seen. Many people theorize that they have a better chance in "high-share" categories. They are hitting your server with similar, long-running queries. It's time to cover those queries with an index.

Which of the following indexes is best suited to speeding up the operation db.prizes.distinct("category", {"laureates.share": {"$gt": "3"}})?

Answer the question
50XP

Possible Answers

    - [("category", 1)]

    - [("category", 1), ("laureates.share", 1)]

    - [("laureates.share", 1)]

    - [("laureates.share", 1), ("category", 1)]

Answer : [("laureates.share", 1), ("category", 1)]

'''
