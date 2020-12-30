'''
The data catalog


To navigate a data lake, a data catalog is typically provided. It abstracts the details of where to find the data and in what format it is stored. Some catalogs hold even more metadata.

For developers, referencing a data catalog removes hardcoded parts from code. Generally you’re not interested in the details of loading the data, you just want to do useful things with it.

A very simple data catalog, named catalog, has been prepared for you. It’s a Python dictionary mapping names of datasets to subclasses of DataLinks, a class that you will be unfamiliar with. In the real world, you will often come across classes that you haven’t encountered before. A DataLink is a custom class that simply encapsulates some metadata (like location, file type and presence of headers). Call the .read() method of the catalog’s diaper_reviews to retrieve the actual dataset (so not the metadata stored in the catalog) and inspect this returned object. What type is it?

Instructions
50 XP

Possible Answers

    - A list

    - A Pandas DataFrame

    - A Spark DataFrame

    - A dictionary

    - A FileSystemDataLink

Answer : A Spark DataFrame

'''
