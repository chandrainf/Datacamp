'''
Meanwhile, in other categories...


We learned in the last exercise that there has been significantly more sharing of physics prizes since World War II: the ratio of the number of laureates who won an unshared prize in physics in or after 1945 to the number of laureates who shared a prize in physics in or after 1945 is approximately 0.13. What is this ratio for prize categories other than physics, chemistry, and medicine?

Instructions
100 XP

- Save an $elemMatch filter unshared to count laureates with unshared prizes in categories other than ("not in") ["physics", "chemistry", "medicine"] in or after 1945.
-Save an $elemMatch filter shared to count laureates with shared (i.e., "share" is not "1") prizes in categories other than ["physics", "chemistry", "medicine"] in or after 1945.

'''
# Save a filter for laureates with unshared prizes
unshared = {
    "prizes": {'$elemMatch': {
        "category": {"$nin": ["physics", "chemistry", "medicine"]},
        "share": "1",
        "year": {"$gte": "1945"},
    }}}

# Save a filter for laureates with shared prizes
shared = {
    "prizes": {"$elemMatch": {
        "category": {"$nin": ["physics", "chemistry", "medicine"]},
        "share": {"$ne": "1"},
        "year": {"$gte": "1945"},
    }}}

ratio = db.laureates.count_documents(
    unshared) / db.laureates.count_documents(shared)
print(ratio)
