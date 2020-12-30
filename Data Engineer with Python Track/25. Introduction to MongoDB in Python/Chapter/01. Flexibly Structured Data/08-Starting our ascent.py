'''
Starting our ascent


Throughout this course, we will gradually build up a set of tools to examine the proportion of Nobel prizes that were awarded to immigrants. In this exercise, you will answer a limited but related question using tools we have introduced so far.

We saw from his laureate document that Walter Kohn's country of birth was "Austria" and that his prize affiliation country was "USA". Count the number of laureates born in Austria with a prize affiliation country that is not also Austria.

Instructions
100 XP

- Save a filter criteria for laureates born in (bornCountry) "Austria" with a non-Austria prizes.affiliations.country.
- Save your count of laureates as count.

'''

# Filter for laureates born in Austria with non-Austria prize affiliation
criteria = {'bornCountry': 'Austria',
            'prizes.affiliations.country': {"$ne": 'Austria'}}

# Count the number of such laureates
count = db.laureates.count_documents(criteria)
print(count)
