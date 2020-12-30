'''
Categorical data validation


What expression asserts that the distinct Nobel Prize categories catalogued by the "prizes" collection are the same as those catalogued by the "laureates"? Remember to explore example documents in the console via e.g. db.prizes.find_one() and db.laureates.find_one().

Instructions
50 XP

Possible Answers

    - assert db.prizes.distinct("category") == db.laureates.distinct("prizes.category")

    - assert db.prizes.distinct("laureates.category") == db.laureates.distinct("prizes.category")

    - assert set(db.prizes.distinct("category")) == set(db.laureates.distinct("prizes.category"))


Answer : assert set(db.prizes.distinct("category")) == set(db.laureates.distinct("prizes.category"))

'''
