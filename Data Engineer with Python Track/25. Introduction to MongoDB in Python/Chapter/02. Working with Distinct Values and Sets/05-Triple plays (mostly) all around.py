'''
Triple plays (mostly) all around


Prizes can be shared, even by more than two laureates. In fact, all prize categories but one – literature – have had prizes shared by three or more laureates.

Instructions
100 XP

- Save a filter document criteria that, when passed to db.prizes.distinct, returns all prize categories shared by three or more laureates. That is, "laureates.2" must exist for such documents.
- Save these prize categories as a Python set called triple_play_categories.
- Confirm via an assertion that "literature" is the only prize category with no prizes shared by three or more laureates.

'''

# Save a filter for prize documents with three or more laureates
criteria = {'laureates.2': {'$exists': True}}

# Save the set of distinct prize categories in documents satisfying the criteria
triple_play_categories = set(db.prizes.distinct('category', criteria))

# Confirm literature as the only category not satisfying the criteria.
assert set(db.prizes.distinct("category")) - \
    triple_play_categories == {"literature"}
