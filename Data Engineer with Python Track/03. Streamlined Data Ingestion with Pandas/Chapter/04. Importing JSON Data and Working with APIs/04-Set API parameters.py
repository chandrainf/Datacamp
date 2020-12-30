'''
Set API parameters


Formatting parameters to get the data you need is an integral part of working with APIs. These parameters can be passed to the get() function's params keyword argument as a dictionary.

The Yelp API requires the location parameter be set. It also lets users supply a term to search for. You'll use these parameters to get data about cafes in NYC, then process the result to create a data frame.

pandas (as pd) and requests have been loaded. The API endpoint is stored in the variable api_url. Authorization data is stored in the dictionary headers.

Instructions
100 XP

- Create a dictionary, parameters, with the term and location parameters set to search for "cafe"s in "NYC".
- Query the Yelp API (api_url) with requests's get() function and the headers and params keyword arguments set. Save the result as response.
- Extract the JSON data from response with the appropriate method. Save the result as data.
- Load the "businesses" values in data to the data frame cafes and print the head

'''

# Create dictionary to query API for cafes in NYC
parameters = {"term": "cafe",
              "location": "NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                        headers=headers,
                        params=parameters)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())
