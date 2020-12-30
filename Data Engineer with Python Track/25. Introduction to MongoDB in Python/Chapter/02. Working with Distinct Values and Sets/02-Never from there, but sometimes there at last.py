'''
Never from there, but sometimes there at last


There are some recorded countries of death ("diedCountry") that do not appear as a country of birth ("bornCountry") for laureates. One such country is "East Germany".

Instructions
100 XP

-Return a set of all such countries as countries.

'''

# Countries recorded as countries of death but not as countries of birth
countries = set(db.laureates.distinct("diedCountry")) - \
    set(db.laureates.distinct("bornCountry"))
print(countries)
