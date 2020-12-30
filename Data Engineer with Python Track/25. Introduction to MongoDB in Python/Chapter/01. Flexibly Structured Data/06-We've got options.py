'''
We've got options


Sometimes, we wish to find documents where a field's value matches any of a set of options. We saw that the $in query operator can be used for this purpose. For example, how many laureates were born in any of "Canada", "Mexico", or "USA"?

If we wish to accept all but one option as a value for a field, we can use the $ne (not equal) operator. For example, how many laureates died in the USA but were not born in the USA?

Instructions 1/2
50 XP

-How many laureates were born in "USA", "Canada", or "Mexico"? Save a filter as criteria and your count as count.


'''
# Save a filter for laureates born in the USA, Canada, or Mexico
criteria = {'bornCountry':
            {"$in": ['USA', 'Canada', 'Mexico']}
            }

# Count them and save the count
count = db.laureates.count_documents(criteria)
print(count)


'''
Instructions 2/2
50 XP

- How many laureates died in the USA but were not born there? Save your filter as criteria and your count as count.

'''

# Save a filter for laureates who died in the USA and were not born there
criteria = {'diedCountry': 'USA',
            'bornCountry': {"$ne": 'USA'},
            }
# -- $ne is great when you don't want to have to list all other options to $in.

# Count them
count = db.laureates.count_documents(criteria)
print(count)
