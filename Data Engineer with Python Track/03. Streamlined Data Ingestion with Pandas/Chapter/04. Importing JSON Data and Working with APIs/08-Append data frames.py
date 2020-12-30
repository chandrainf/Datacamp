'''
Append data frames


In this exercise, you’ll practice appending records by creating a dataset of the 100 highest-rated cafes in New York City according to Yelp.

APIs often limit the amount of data returned, since sending large datasets can be time- and resource-intensive. The Yelp Business Search API limits the results returned in a call to 50 records. However, the offset parameter lets a user retrieve results starting after a specified number. By modifying the offset, we can get results 1-50 in one call and 51-100 in another. Then, we can append the data frames.

pandas (as pd), requests, and json_normalize() have been imported. The 50 top-rated cafes are already in a data frame, top_50_cafes.

Instructions
100 XP

- Add an "offset" parameter to params so that the Yelp API call will get cafes 51-100.
- Append the results of the API call to top_50_cafes, setting ignore_index so rows will be renumbered.
- Print the shape of the resulting data frame, cafes, to confirm there are 100 records.

'''
# Add an offset parameter to get cafes 51-100
params = {"term": "cafe",
          "location": "NYC",
          "sort_by": "rating",
          "limit": 50,
          "offset": 50}

result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])

# Append the results, setting ignore_index to renumber rows
cafes = top_50_cafes.append(next_50_cafes, ignore_index=True)

# Print shape of cafes
print(cafes.shape)
