#Checking out the Wikipedia API
#You're doing so well and having so much fun that we're going to throw one more API at you:
# the Wikipedia API (documented here). You'll figure out how to find and extract information from the Wikipedia page for Pizza. 
# What gets a bit wild here is that your query will return nested JSONs, that is, JSONs with JSONs, but Python can handle that because 
# it will translate them into dictionaries within dictionaries.

#The URL that requests the relevant query from the Wikipedia API is

#https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza


# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
