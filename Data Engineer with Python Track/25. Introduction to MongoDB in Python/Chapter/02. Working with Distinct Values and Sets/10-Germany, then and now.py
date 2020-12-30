'''
Germany, then and now


Just as we saw with Poland, there are laureates who were born somewhere that was in Germany at the time but is now not, and others born somewhere that was not in Germany at the time but now is.

Instructions 1/4
25 XP

- Use a regular expression object to filter for laureates with "Germany" in their "bornCountry" value.

'''

from bson.regex import Regex

# Filter for laureates with "Germany" in their "bornCountry" value
criteria = {"bornCountry": Regex("Germany")}
print(set(db.laureates.distinct("bornCountry", criteria)))


'''
Instructions 2/4
25 XP

- Use a regular expression object to filter for laureates with a "bornCountry" value starting with "Germany".
'''


# Filter for laureates with a "bornCountry" value starting with "Germany"
criteria = {"bornCountry": Regex("^Germany")}
print(set(db.laureates.distinct("bornCountry", criteria)))


'''
Instructions 3/4
25 XP

- Use a regular expression object to filter for laureates born in what was at the time Germany but is now another country.

'''

# Fill in a string value to be sandwiched between the strings "^Germany " and "now"
criteria = {"bornCountry": Regex("^" + "Germany \(" + "now")}
print(set(db.laureates.distinct("bornCountry", criteria)))


'''
Instructions 4/4
25 XP

- Use a regular expression object to filter for laureates born in what is now Germany but at the time was another country.

'''

# Filter for currently-Germany countries of birth. Fill in a string value to be sandwiched between the strings "now" and "$"
criteria = {"bornCountry": Regex("now" + " Germany\)" + "$")}
print(set(db.laureates.distinct("bornCountry", criteria)))
