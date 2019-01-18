#Parsing HTML with BeautifulSoup

#In this interactive exercise, 
#you'll learn how to use the BeautifulSoup package to parse, prettify and extract information from HTML. 
#You'll scrape the data from the webpage of Guido van Rossum, Python's very own Benevolent Dictator for Life. 
#In the following exercises, you'll prettify the HTML and then extract the text and the hyperlinks.

#The URL of interest is url = 'https://www.python.org/~guido/'.





from bs4 import BeautifulSoup

# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()
# Print the response
print(pretty_soup)
