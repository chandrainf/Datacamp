'''
Count documents in a collection


In the video, you learned that a MongoDB database can consist of several collections. Collections, in turn, consist of documents, which store the data.

You will be working with the Nobel laureates database which we have retrieved as nobel. The database has two collections, prizes and laureates. In the prizes collection, every document correspond to a single Nobel prize, and in the laureates collection - to a single Nobel laureate.

Recall that you can access databases by name as attributes of the client, like client.my_database (a connected client is already provided to you as client). Similarly, collections can be accessed by name as attributes of databases (my_database.my_collection).

Use the console on the right to compare the number of laureates and prizes using the .count_documents() method on a collection (don't forget to specify an empty filter document as the argument!), and pick a statement that is TRUE.

Instructions
50 XP

Possible Answers

    - The number of prizes and laureates are equal.

    - Prizes outnumber laureates.

    - Laureates outnumber prizes.

Answer : Laureates outnumber prizes.

'''
