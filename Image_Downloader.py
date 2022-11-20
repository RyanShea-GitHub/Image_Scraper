import os
from bs4 import BeautifulSoup
import requests

# Enter the URL for your Target Site
# Response library will use the .get command to scrape all of the website information
url = 'https://www.thewrap.com/celebrity-mugshots-locklear-downey-jr-photos/'


# Beautiful soup will take all of the text information from the target website and parse all of the HTML and save it to a new variable


# For loop to go through all of the parsed HTML and identify the image tags
# when it finds an image tag it will make sure that there is a "source" tag to ensure that we are getting only results with downloadable images
# Strips all other HTML found in the text and only prints the links to the images fromt he website.



def image_Downloader(url, folder):
    
    os.makedirs(os.path.join(os.getcwd(), folder))

    r = requests.get(url)
    soup = BeautifulSoup( r.text, "html.parser")
    images = soup.find_all('img',{"src":True})
    
    os.chdir(os.path.join(os.getcwd(), folder))
    for image in images:                 
        link = image['src']
        name = image.get('alt')

        if link.endswith('.jpg'):
            with open(name.replace(' ', '_') + '.jpg', 'wb') as output_file:
                img = requests.get(link)
                output_file.write(img.content)


image_Downloader(url, 'images')

