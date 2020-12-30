'''
Get data from an API


In this exercise, you'll use requests.get() to query the Yelp Business Search API for cafes in New York City. requests.get() needs a URL to get data from. The Yelp API also needs search parameters and authorization headers passed to the params and headers keyword arguments, respectively.

You'll need to extract the data from the response with its json() method, and pass it to pandas's DataFrame() function to make a data frame. Note that the necessary data is under the dictionary key "businesses".

pandas (as pd) and requests have been loaded. Authorization data is in the dictionary headers, and the needed API parameters are stored as params.

Instructions
100 XP

- Get data about New York City cafes from the Yelp API (api_url) with requests.get(). The necessary params and headers information has been provided.
- Extract the JSON data from the response with its json() method, and assign it to data.
- Load the cafe listings to the data frame cafes with pandas's DataFrame() function. The listings are under the "businesses" key in data.
- Print the data frame's dtypes to see what information you're getting.

'''
api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url,
                        headers=headers,
                        params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a data frame
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)
