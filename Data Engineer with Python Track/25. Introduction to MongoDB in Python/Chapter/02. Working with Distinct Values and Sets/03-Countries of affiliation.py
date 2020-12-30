'''
Countries of affiliation


We saw in the last exercise that countries can be associated with a laureate as their country of birth and as their country of death. For each prize a laureate received, they may also have been affiliated with an institution at the time, located in a country.

Instructions
100 XP

- Determine the number of distinct countries recorded as part of an affiliation for laureates' prizes. Save this as count.

'''
# The number of distinct countries of laureate affiliation for prizes
count = len(db.laureates.distinct('prizes.affiliations.country'))
print(count)
