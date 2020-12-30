'''
Our 'born' approximation, and a special laureate


We saw earlier that the laureates collection encodes uncertainty about birthdate in a special way. When a birthdate is unknown, the "born" field has the value "0000-00-00". Thus,

db.laureates.count_documents({"born": "0000-00-00"})
counts the number of such laureates. Or does it?

We also saw that the total number of laureate prizes is more than the number of laureates -- some were awarded more than one prize. There is one in particular with a whopping three prizes, and this laureate holds key information to aid our quest to determine the proportion of prizes awarded to immigrants.

Instructions 1/2
50 XP

- Use a filter document (criteria) to count the documents that don't have a "born" field.

'''
# Filter for documents without a "born" field
criteria = {'born': {"$exists": False}}

# Save count
count = db.laureates.count_documents(criteria)
print(count)


'''
Instructions 2/2
50 XP

- Use a filter document (criteria) to find a document for a laureate with at least three elements in its "prizes" array. In other words, does a third element exist for the array? Remember about the zero-based indexing!

'''
# Filter for laureates with at least three prizes
criteria = {'prizes.2': {"$exists": True}}

# Find one laureate with at least three prizes
doc = db.laureates.find_one(criteria)

# Print the document
print(doc)
