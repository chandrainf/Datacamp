'''
The first five prizes with quarter shares


Find the first five prizes with one or more laureates sharing 1/4 of the prize. Project our prize category, year, and laureates' motivations.

Instructions
100 XP

- Save to filter_ the filter document to fetch only prizes with one or more quarter-share laureates, i.e. with a "laureates.share" of "4".
- Save to projection the list of field names so that prize category, year and laureates' motivations ("laureates.motivation") may be fetched for inspection.
- Save to cursor a cursor that will yield prizes, sorted by ascending year. Limit this to five prizes, and sort using the most concise specification.

'''

from pprint import pprint

# Fetch prizes with quarter-share laureate(s)
filter_ = {'laureates.share': '4'}

# Save the list of field names
projection = ['category', 'year', 'laureates.motivation']

# Save a cursor to yield the first five prizes
cursor = db.prizes.find(filter_, projection).sort('year').limit(5)
pprint(list(cursor))
