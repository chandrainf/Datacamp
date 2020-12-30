'''
The prized transistor


Three people shared a Nobel prize "for their researches on semiconductors and their discovery of the transistor effect". We can filter on "transistor" as a substring of a laureate's "prizes.motivation" field value to find these laureates.

Instructions
100 XP

- Save a filter criteria that finds laureates with prizes.motivation values containing "transistor" as a substring. The substring can appear anywhere within the value, so no anchoring characters are needed.
- Save to first and last the field names corresponding to a laureate's first name and last name (i.e. "surname") so that we can print out the names of these laureates.

'''

from bson.regex import Regex

# Save a filter for laureates with prize motivation values containing "transistor" as a substring
criteria = {'prizes.motivation': Regex('transistor')}

# Save the field names corresponding to a laureate's first name and last name
first, last = 'firstname', 'surname'
print([(laureate[first], laureate[last])
       for laureate in db.laureates.find(criteria)])
