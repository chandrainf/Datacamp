'''
Flatten nested JSONs


A feature of JSON data is that it can be nested: an attribute's value can consist of attribute-value pairs. This nested data is more useful unpacked, or flattened, into its own data frame columns. The pandas.io.json submodule has a function, json_normalize(), that does exactly this.

The Yelp API response data is nested. Your job is to flatten out the next level of data in the coordinates and location columns.

pandas (as pd) and requests have been imported. The results of the API call are stored as response.

Instructions
100 XP

- Load the json_normalize() function from pandas' io.json submodule.
- Isolate the JSON data from response and assign it to data.
- Use json_normalize() to flatten and load the businesses data to a data frame, cafes. Set the sep argument to use underscores (_), rather than periods.
- Show the data head.

'''
# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a data frame, replace separator
cafes = json_normalize(data["businesses"],
                       sep="_")

# View data
print(cafes.head())
