'''
Aggregating a few individuals' country data


The following query cursor yields birth-country and prize-affiliation-country information for three non-organization laureates:

    cursor = (db.laureates.find(
        {"gender": {"$ne": "org"}},
        ["bornCountry", "prizes.affiliations.country"]
    ).limit(3))

Instructions
100 XP

- Translate the above cursor cursor to an equivalent aggregation cursor, saving the pipeline stages to pipeline. Recall that the find collection method's "filter" parameter maps to the "$match" aggregation stage, its "projection" parameter maps to the "$project" stage, and the "limit" parameter (or cursor method) maps to the "$limit" stage.

'''

# Translate cursor to aggregation pipeline
pipeline = [
    {'$match': {'gender': {'$ne': 'org'}}},
    {'$project': {'bornCountry': 1, 'prizes.affiliations.country': 1}},
    {'$limit': 3}
]

for doc in db.laureates.aggregate(pipeline):
    print("{bornCountry}: {prizes}".format(**doc))
