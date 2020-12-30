'''
Communicating with an API


Before diving into this third lesson’s concepts, make sure you remember how URLs are constructed and how to interact with web APIs, from the prerequisite course Importing Data in Python, Part 2.

The marketing team you are collaborating with has been scraping several websites for customer reviews on consumer products. The dataset is only exposed to you through an internal REST API. You would like to add that data in its entirety to the data lake and store it in a convenient way, say csv. While the data is available over the company’s internal network, you still need to supply the API key that the marketing team has created for your exploration use case: api_key: scientist007.

For technical reasons, the endpoint has been made available to you on localhost:5000. You can “browse” to it, using the well-known requests module, by calling requests.get(SOME_URL). You can authenticate to the API using your API key. Simply fill in the template URL <endpoint>/<api_key>/.

Instructions 1/3
35 XP

- Fill in the correct API key.
- Create the URL of the web API by completing the template URL above. You need to pass the endpoint first and then the API key.
- Use that URL in the call to requests.get() so that you may see what more the API can tell you about itself.

'''
endpoint = "http://localhost:5000"

# Fill in the correct API key
api_key = "scientist007"

# Create the web API’s URL
authenticated_endpoint = "{}/{}".format(endpoint, api_key)

# Get the web API’s reply to the endpoint
api_response = requests.get(authenticated_endpoint).json()
pprint.pprint(api_response)

'''
Instructions 2/3
35 XP

- Take a look at the output in the console from the previous step. Notice that it is a list of endpoints, each containing a description of the content found at the endpoint and the template for the URL to access it. The template can be filled in, like you did in the previous step.

Complete the URL that should give you back a list of all shops that were scraped by the marketing team.

'''
endpoint = "http://localhost:5000"

# Fill in the correct API key
api_key = "scientist007"

# Create the web API’s URL
authenticated_endpoint = "{}/{}".format(endpoint, api_key)

# Get the web API’s reply to the endpoint
api_response = requests.get(authenticated_endpoint).json()
pprint.pprint(api_response)

# Create the API’s endpoint for the shops
shops_endpoint = "{}/{}/{}/{}".format(endpoint,
                                      api_key, "diaper/api/v1.0", "shops")
shops = requests.get(shops_endpoint).json()
print(shops)

'''
Instructions 3/3
30 XP

Take a look at the output in the console from the previous step. The shops variable contains the list of all shops known by the web API.

From the shops variable, find the one that starts with the letter “D”. Use it in the second (templated) url that was shown by the call to pprint.pprint(api_response), to list the items of this specific shop. You must use the appropriate url endpoint, combined with the http://localhost:5000, similar to how you completed the previous step.

'''
endpoint = "http://localhost:5000"

# Fill in the correct API key
api_key = "scientist007"

# Create the web API’s URL
authenticated_endpoint = "{}/{}".format(endpoint, api_key)

# Get the web API’s reply to the endpoint
api_response = requests.get(authenticated_endpoint).json()
pprint.pprint(api_response)

# Create the API’s endpoint for the shops
shops_endpoint = "{}/{}/{}/{}".format(endpoint,
                                      api_key, "diaper/api/v1.0", "shops")
shops = requests.get(shops_endpoint).json()
print(shops)

# Create the API’s endpoint for items of the shop starting with a "D"
items_of_specific_shop_URL = "{}/{}/{}/{}/{}".format(
    endpoint, api_key, "diaper/api/v1.0", "items", "DM")
products_of_shop = requests.get(items_of_specific_shop_URL).json()
pprint.pprint(products_of_shop)
