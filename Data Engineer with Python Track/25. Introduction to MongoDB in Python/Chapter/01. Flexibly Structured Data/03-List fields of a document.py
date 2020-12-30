'''
List fields of a document


The .find_one() method of a collection can be used to retrieve a single document. This method accepts an optional filter argument that specifies the pattern that the document must match. You will learn more about filters in the next lesson, but for now, you can specify no filter or an empty document filter ({}), in which case MongoDB will return the document that is first in the internal order of the collection.

This method is useful when you want to learn the structure of documents in the collection.

In Python, the returned document takes the form of a dictionary:

    sample_doc = {'id' : 12345, 'name':'Donny Winston', 'instructor': True}

The keys of the dictionary are the (root-level) "fields" of the document, e.g. 'id', 'name','instructor'.

Instructions 1/3
35 XP

-Connect to the nobel database.

'''
# Connect to the "nobel" database
db = client.nobel


'''
Instructions 2/3
35 XP

- Fetch one document from each of the prizes and laureates collections, and then take a look at the output in the console to see the format and type of the documents in Python.

'''

# Connect to the "nobel" database
db = client.nobel

# Retrieve sample prize and laureate documents
prize = db.prizes.find_one()
laureate = db.laureates.find_one()

# Print the sample prize and laureate documents
print(prize)
print(laureate)
print(type(laureate))


'''
Instructions 3/3
30 XP

Since prize and laureate are dictionaries, you can use the .keys() method to return the keys (i.e. the field names). But it's often more convenient to work with lists of fields.

    - Use the list() constructor to save a list of the fields present in the prize and laureate documents.

'''
# Connect to the "nobel" database
db = client.nobel

# Retrieve sample prize and laureate documents
prize = db.prizes.find_one()
laureate = db.laureates.find_one()

# Print the sample prize and laureate documents
print(prize)
print(laureate)
print(type(laureate))

# Get the fields present in each type of document
prize_fields = list(prize.keys())
laureate_fields = list(laureate.keys())

print(prize_fields)
print(laureate_fields)
