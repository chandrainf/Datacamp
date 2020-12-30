'''
"born" approximation


The "born" field in a laureate collection document records the date of birth of that laureate. "born" values are of the form "YYYY-MM-DD", also known as ISO 8601 format. An example value is "1937-02-01", for February 1st, 1937. This format is convenient for lexicographic comparison. For example, the query

db.laureates.count_documents({"born": {"$lt": "1900"}})
returns the number of laureates with recorded dates of birth earlier than the year 1900 ("$lt" is for "less than"). Using the query format above, what is the number of laureates born prior to 1800? What about prior to 1700?

Instructions
50 XP

Possible Answers

    - 38 prior to 1800, and 0 prior to 1700

    - 324 prior to 1800, and 35 prior to 1700

    - 38 prior to 1800, and 38 prior to 1700

Answer : 38 prior to 1800, and 38 prior to 1700

'''
