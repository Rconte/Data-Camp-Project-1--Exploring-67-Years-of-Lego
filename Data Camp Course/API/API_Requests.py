#API requests
#Now it's your turn to pull some movie data down from the Open Movie Database (OMDB) using their API. 
# The movie you'll query the API about is The Social Network. Recall that, in the video, to query the API about the movie Hackers, 
# Hugo's query string was 'http://www.omdbapi.com/?t=hackers' and had a single argument t=hackers.

#Note: recently, OMDB has changed their API: you now also have to specify an API key. 
# This means you'll have to add another argument to the URL: apikey=72bc447a.




# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)
