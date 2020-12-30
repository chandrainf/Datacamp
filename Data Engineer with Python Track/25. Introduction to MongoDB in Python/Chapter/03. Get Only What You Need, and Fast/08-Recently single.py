'''
Recently single?


A prize might be awarded to a single laureate or to several. For each prize category, report the most recent year that a single laureate -- rather than several -- received a prize in that category. As part of this task, you will ensure an index that speeds up finding prizes by category and then sorting results by decreasing year

Instructions
100 XP

- Specify an index model that indexes first on category (ascending) and second on year (descending).
- Save a string report for printing the last single-laureate year for each distinct category, one category per line. To do this, for each distinct prize category, find the latest-year prize (requiring a descending sort by year) of that category (so, find matches for that category) with a laureate share of "1".

'''
# Specify an index model for compound sorting
index_model = [('category', 1), ('year', -1)]
db.prizes.create_index(index_model)

# Collect the last single-laureate year for each category
report = ""
for category in sorted(db.prizes.distinct("category")):
    doc = db.prizes.find_one(
        {'category': category, "laureates.share": "1"},
        sort=[('year', -1)]
    )
    report += "{category}: {year}\n".format(**doc)

print(report)
