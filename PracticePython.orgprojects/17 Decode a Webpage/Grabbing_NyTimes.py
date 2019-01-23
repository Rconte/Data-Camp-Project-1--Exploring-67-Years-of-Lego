#Decode A Web Page 

#Exercise 17 

#Use the BeautifulSoup and requests 
#Python packages to print out a list of all the article titles on the New York Times homepage.


import requests
from bs4 import BeautifulSoup

# 1. P A R S I N G
#grabbed url and stored it in variable url
url = 'https://www.nytimes.com/'
#send requests and get response 
req = requests.get(url)
#Grabbing text from the reqeust
html_doc = req.text

# 2 . M A K I N G  I T  B E A U T I F U L

soup = BeautifulSoup(html_doc,features="lxml")

for story_heading in soup.find_all(class_="story-heading"): 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())
