'''
How many prizes were awarded to immigrants?


How many prizes were awarded to people who had no affiliation in their country of birth at the time of the award?

Instructions
100 XP

- In your aggregation pipeline pipeline, use the "gender" field to limit results to people (that is, not organizations).
- Count prizes for which the laureate's "bornCountry" is not also the "country" of any of their affiliations for the prize. Be sure to use field paths (precede a field name with "$") when appropriate.

'''

pipeline = [
    # Limit results to people; project needed fields; unwind prizes
    {"$match": {"gender": {"$ne": "org"}}},
    {"$project": {"bornCountry": 1, "prizes.affiliations.country": 1}},
    {"$unwind": "$prizes"},

    # Count prizes with no country-of-birth affiliation
    {"$addFields": {"bornCountryInAffiliations": {
        "$in": ["$bornCountry", "$prizes.affiliations.country"]}}},
    {"$match": {"bornCountryInAffiliations": False}},
    {"$count": "awardedElsewhere"},
]

print(list(db.laureates.aggregate(pipeline)))
