'''
Listing databases and collections


Our MongoClient object is not actually a dictionary, so we can't call keys() to list the names of accessible databases. The same is true for listing collections of a database. Instead, we can list database names by calling .list_database_names() on a client instance, and we can list collection names by calling .list_collection_names() on a database instance.

Instructions
100 XP

- Save a list, called db_names, of the names of the databases managed by our connected client.
- Similarly, save a list, called nobel_coll_names, of the names of the collections managed by the "nobel" database.

'''
# Save a list of names of the databases managed by client
db_names = client.list_database_names()
print(db_names)

# Save a list of names of the collections managed by the "nobel" database
nobel_coll_names = client.nobel.list_collection_names()
print(nobel_coll_names)
