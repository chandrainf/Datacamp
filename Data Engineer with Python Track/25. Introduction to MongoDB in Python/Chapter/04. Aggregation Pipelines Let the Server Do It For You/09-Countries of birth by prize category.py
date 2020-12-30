'''
Countries of birth by prize category


Some prize categories have laureates hailing from a greater number of countries than do other categories. You will build an aggregation pipeline for the prizes collection to collect these numbers, using a $lookup stage to obtain laureate countries of birth.

Instructions
100 XP

- $unwind the laureates array field to output one pipeline document for each array element.
- After pulling in laureate bios with a $lookup stage, unwind the new laureate_bios array field (each laureate has only a single biography document).
- Collect the set of bornCountries associated with each prize category.
- Project out the size of each category's set of bornCountries.

'''

pipeline = [
    # Unwind the laureates array
    {'$unwind': "$laureates"},
    {"$lookup": {
        "from": "laureates", "foreignField": "id",
        "localField": "laureates.id", "as": "laureate_bios"}},

    # Unwind the new laureate_bios array
    {"$unwind": "$laureate_bios"},
    {"$project": {"category": 1,
                  "bornCountry": "$laureate_bios.bornCountry"}},

    # Collect bornCountry values associated with each prize category
    {"$group": {"_id": "$category",
                "bornCountries": {"$addToSet": "$bornCountry"}}},

    # Project out the size of each category's (set of) bornCountries
    {"$project": {"category": 1,
                  "nBornCountries": {"$size": "$bornCountries"}}},
    {"$sort": {"nBornCountries": -1}},
]
for doc in db.prizes.aggregate(pipeline):
    print(doc)
