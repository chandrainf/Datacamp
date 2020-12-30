'''
Fetch from an API


In the last video, you've seen that you can extract data from an API by sending a request to the API and parsing the response which was in JSON format. In this exercise, you'll be doing the same by using the requests library to send a request to the Hacker News API.

Hacker News is a social news aggregation website, specifically for articles related to computer science or the tech world in general. Each post on the website has a JSON representation, which you'll see in the response of the request in the exercise.

Instructions
100 XP

- Use the correct method of the requests module to get the Hacker News post's JSON object.
- Print out the response, parsed as a JSON.
- Assign the "score" key of the post to post_score.

'''

import requests

# Fetch the Hackernews post
resp = requests.get("https://hacker-news.firebaseio.com/v0/item/16222426.json")

# Print the response parsed as JSON
print(resp.json())

# Assign the score of the test to post_score
post_score = resp.json()['score']
print(post_score)
