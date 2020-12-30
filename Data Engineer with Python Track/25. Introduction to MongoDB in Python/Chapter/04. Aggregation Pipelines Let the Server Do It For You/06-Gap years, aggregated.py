'''
Gap years, aggregated

In a previous exercise, you collected instances of prize categories not being awarded in particular years. You implemented this using a for loop in Python. You will now implement this as an aggregation pipeline that:

    1. Filters for original prize categories (i.e. sans economics),
    2. Projects category and year,
    3. Groups distinct prize categories awarded by year,
    4. Projects prize categories not awarded by year,
    5. Filters for years with missing prize categories, and
    6. Returns a cursor of documents in reverse chronological order, one per year, each with a list of missing prize categories for that year.

Remember to use field paths (precede field names with "$") to extract field values in expressions.

Instructions
100 XP

- Make the $group stage output a document for each prize year (set "_id" to the field path for year) with the set of categories awarded that year.
- Given your intermediate collection of year-keyed documents, $project a field named "missing" with the (original) categories not awarded that year. Again, mind your field paths!
- Use a $match stage to only pass through documents with at least one missing prize category.
- Finally, add sort documents in descending order.

'''

from collections import OrderedDict

original_categories = sorted(
    set(db.prizes.distinct("category", {"year": "1901"})))
pipeline = [
    {"$match": {"category": {"$in": original_categories}}},
    {"$project": {"category": 1, "year": 1}},

    # Collect the set of category values for each prize year.
    {"$group": {"_id": '$year', "categories": {"$addToSet": "$category"}}},

    # Project categories *not* awarded (i.e., that are missing this year).
    {"$project": {"missing": {"$setDifference": [
        original_categories, '$categories']}}},

    # Only include years with at least one missing category
    {"$match": {"missing.0": {"$exists": True}}},

    # Sort in reverse chronological order. Note that "_id" is a distinct year at this stage.
    {"$sort": OrderedDict([("_id", -1)])},
]
for doc in db.prizes.aggregate(pipeline):
    print("{year}: {missing}".format(
        year=doc["_id"], missing=", ".join(sorted(doc["missing"]))))
