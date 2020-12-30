'''
Here and elsewhere


What proportion of laureates won a prize while affiliated with an institution in their country of birth? Build an aggregation pipeline to get the count of laureates who either did or did not win a prize with an affiliation country that is a substring of their country of birth -- for example, the prize affiliation country "Germany" should match the country of birth "Prussia (now Germany)".

Instructions
100 XP

- Use $unwind stages to ensure a single prize affiliation country per pipeline document.
- Filter out prize-affiliation-country values that are "empty" (null, not present, etc.) -- ensure values are "$in" the list of known values.
- Produce a count of documents for each value of "affilCountrySameAsBorn" (a field we've projected for you using the $indexOfBytes operator) by adding 1 to the running sum.

'''

key_ac = "prizes.affiliations.country"
key_bc = "bornCountry"
pipeline = [
    {"$project": {key_bc: 1, key_ac: 1}},

    # Ensure a single prize affiliation country per pipeline document
    {'$unwind': "$prizes"},
    {'$unwind': "$prizes.affiliations"},

    # Ensure values in the list of distinct values (so not empty)
    {"$match": {key_ac: {'$in': db.laureates.distinct(key_ac)}}},
    {"$project": {"affilCountrySameAsBorn": {
        "$gte": [{"$indexOfBytes": ["$"+key_ac, "$"+key_bc]}, 0]}}},

    # Count by "$affilCountrySameAsBorn" value (True or False)
    {"$group": {"_id": "$affilCountrySameAsBorn",
                "count": {"$sum": 1}}},
]
for doc in db.laureates.aggregate(pipeline):
    print(doc)
