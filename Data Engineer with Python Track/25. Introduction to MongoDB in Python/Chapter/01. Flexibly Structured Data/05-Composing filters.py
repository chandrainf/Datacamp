'''
Composing filters


It is often useful to incrementally build up a filter document in order to see the effect of adding constraints one at a time. In this exercise, we will count the number of laureate documents matching some criteria, and we will gradually add criteria.

Instructions 1/3
35 XP

- Create a filter criteria to count laureates who died ("diedCountry") in the USA ("USA"). Save the document count as count.

'''
# Create a filter for laureates who died in the USA
criteria = {'diedCountry': 'USA'}

# Save the count of these laureates
count = db.laureates.count_documents(criteria)
print(count)


'''
Instructions 2/3
35 XP

- Create a filter to count laureates who died in the United States but were born ("bornCountry") in Germany.
'''

# Create a filter for laureates who died in the USA but were born in Germany
criteria = {'diedCountry': 'USA',
            'bornCountry': 'Germany'}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)


'''
Instructions 3/3
30 XP

- Count laureates who died in the USA, were born in Germany, and whose first name ("firstname") was "Albert".

'''
# Create a filter for Germany-born laureates who died in the USA and with the first name "Albert"
criteria = {'bornCountry': 'Germany',
            'diedCountry': 'USA',
            'firstname': 'Albert'}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)
