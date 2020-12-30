'''
Born and affiliated


Some countries are, for one or more laureates, both their country of birth ("bornCountry") and a country of affiliation for one or more of their prizes ("prizes.affiliations.country"). You will find the five countries of birth with the highest counts of such laureates.

Instructions
100 XP

- Create an index on country of birth ("bornCountry") for db.laureates to ensure efficient gathering of distinct values and counting of documents
- Complete the skeleton dictionary comprehension to construct n_born_and_affiliated, the count of laureates as described above for each distinct country of birth. For each call to count_documents, ensure that you use the value of country to filter documents properly.

'''

from collections import Counter

# Ensure an index on country of birth
db.laureates.create_index([('bornCountry', 1)])

# Collect a count of laureates for each country of birth
n_born_and_affiliated = {
    country: db.laureates.count_documents({
        'bornCountry': country,
        "prizes.affiliations.country": country
    })
    for country in db.laureates.distinct("bornCountry")
}

five_most_common = Counter(n_born_and_affiliated).most_common(5)
print(five_most_common)
