'''
Refinement: filter out "unaffiliated" people


In the previous exercise, we counted prizes awarded to people without an affiliation in their "bornCountry". However, hundreds of prizes were awarded to people without recorded affiliations; sure, their "bornCountry" is technically not the "country" of any of their affiliations, but there are no "country" values to compare against!

Instructions
100 XP

- Construct a stage added_stage that filters for laureate "prizes.affiliations.country" values that are non-empty, that is, are $in a list of the distinct values that the field takes in the collection.
- Insert this stage into the pipeline so that it filters out single prizes (not arrays) and precedes any test for membership in an array of countries. Recall that the first parameter to <list>.insert is the (zero-based) index for insertion.

'''
pipeline = [
    {"$match": {"gender": {"$ne": "org"}}},
    {"$project": {"bornCountry": 1, "prizes.affiliations.country": 1}},
    {"$unwind": "$prizes"},
    {"$addFields": {"bornCountryInAffiliations": {
        "$in": ["$bornCountry", "$prizes.affiliations.country"]}}},
    {"$match": {"bornCountryInAffiliations": False}},
    {"$count": "awardedElsewhere"},
]

# Construct the additional filter stage
added_stage = {"$match": {"prizes.affiliations.country": {
    '$in': db.laureates.distinct("prizes.affiliations.country")}}}

# Insert this stage into the pipeline
pipeline.insert(3, added_stage)
print(list(db.laureates.aggregate(pipeline)))
