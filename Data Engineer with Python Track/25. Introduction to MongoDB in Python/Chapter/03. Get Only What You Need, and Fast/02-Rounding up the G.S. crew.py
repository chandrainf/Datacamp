'''
Rounding up the G.S. crew


In chapter 2, you used a regular expression object Regex to find values that follow a pattern. We can also use the regular expression operator $regex for the same purpose. For example, the following query:

    { "name": {$regex: "^Py"}    }
    will fetch documents where the field 'name' starts with "Py". Here the caret symbol ^ means "starts with".

In this exercise, you will use regular expressions, projection, and list comprehension to collect the full names of laureates whose initials are "G.S.".

Instructions 1/3
35 XP

- First, use regular expressions to fetch the documents for the laureates whose "firstname" starts with "G" and whose "surname" starts with "S".

'''

# Find laureates whose first name starts with "G" and last name starts with "S"
docs = db.laureates.find(
    filter={"firstname": {"$regex": "^G"},
            'surname': {"$regex": "^S"}})
# Print the first document
print(docs[0])


'''
Instructions 2/3
35 XP

In the previous step, we fetched all the data for all the laureates with initials G.S. This is unnecessary if we only want their full names!

Use projection and adjust the query to select only the "firstname" and "surname" fields.

'''
# Use projection to select only firstname and surname
docs = db.laureates.find(
    filter={"firstname": {"$regex": "^G"},
            "surname": {"$regex": "^S"}},
    projection=["firstname", "surname"])


# Print the first document
print(docs[0])


'''
Instructions 3/3
30 XP

- Now the documents you fetched contain only the relevant information!

    - Iterate over the documents, and for each document, concatenate the first name and the surname fields together with a space in between to obtain full names.

'''
# Use projection to select only firstname and surname
docs = db.laureates.find(
    filter={"firstname": {"$regex": "^G"},
            "surname": {"$regex": "^S"}},
    projection=["firstname", "surname"])

# Iterate over docs and concatenate first name and surname
full_names = [doc["firstname"] + " " + doc["surname"] for doc in docs]

# Print the full names
print(full_names)
