'''
Organizations and prizes over time


How many organizations won prizes before 1945 versus in or after 1945?

Instructions
100 XP

- You won't need the $elemMatch operator at all for this exercise.
- Save a filter before to count organization laureates with prizes won before 1945. Recall that organization status is encoded with the "gender" field, and that dot notation is needed to access a laureate's "year" field within its "prizes" array.
- Save a filter in_or_after to count organization laureates with prizes won in or after 1945.

'''

# Save a filter for organization laureates with prizes won before 1945
before = {
    "gender": "org",
    "prizes.year": {"$lt": "1945"},
}

# Save a filter for organization laureates with prizes won in or after 1945
in_or_after = {
    'gender': 'org',
    'prizes.year': {'$gte': "1945"},
}

n_before = db.laureates.count_documents(before)
n_in_or_after = db.laureates.count_documents(in_or_after)
ratio = n_in_or_after / (n_in_or_after + n_before)
print(ratio)
