''''
Set request headers


Many APIs require users provide an API key, obtained by registering for the service. Keys typically are passed in the request header, rather than as parameters.

The Yelp API documentation says "To authenticate API calls with the API Key, set the Authorization HTTP header value as Bearer API_KEY."

You'll set up a dictionary to pass this information to get(), call the API for the highest-rated cafes in NYC, and parse the response.

pandas (as pd) and requests have been loaded. The API endpoint is stored as api_url, and the key is api_key. Parameters are in the dictionary params.

Instructions
100 XP

- Create a dictionary, headers, that passes the formatted key string to the "Authorization" header value.
- Query the Yelp API (api_url) with get() and the necessary headers and parameters. Save the result as response.
- Extract the JSON data from response. Save the result as data.
- Load the "businesses" values in data to the data frame cafes and print the names column.

'''
# Create dictionary that passes Authorization and key string
headers = {"Authorization": "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                        headers=headers,
                        params=params)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a data frame and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)
