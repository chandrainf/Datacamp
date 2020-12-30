'''
Passing the aggregation baton to Python


Construct an aggregation pipeline to collect, in reverse chronological order (i.e., descending year), prize documents for all original categories (that is, $in categories awarded in 1901). Project only the prize year and category (including document _id is fine).

The aggregation cursor will be fed to Python's itertools.groupby function to group prizes by year. For each year that at least one of the original prize categories was missing, a line with all missing categories for that year will be printed.

Instructions
100 XP

- Save to pipeline an aggregation pipeline to collect prize documents as detailed above. Use Python's collections.OrderedDict to specify any sorting.

'''
from collections import OrderedDict
from itertools import groupby
from operator import itemgetter

original_categories = set(db.prizes.distinct("category", {"year": "1901"}))

# Save an pipeline to collect original-category prizes
pipeline = [
    {"$match": {"category": {"$in": list(original_categories)}}},
    {"$project": {"category": 1, "year": 1}},
    {"$sort": OrderedDict([("year", -1)])}
]
cursor = db.prizes.aggregate(pipeline)
for key, group in groupby(cursor, key=itemgetter("year")):
    missing = original_categories - {doc["category"] for doc in group}
    if missing:
        print("{year}: {missing}".format(
            year=key, missing=", ".join(sorted(missing))))
