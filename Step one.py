#-------------------------------------------------------------------------------
# Name:        downloader
# Purpose:
#
# Author:      Kenny Passenier
#
# Created:     22/07/2014
# Updated:     10/02/2021
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote

# Define global variables
storageFolder = "\images"
comicNr = 15 # Comics start at nr 15
upperLimit = 10000 # This magic number could probably be inferred from info on explosm.net

for _ in range(comicNr, upperLimit):
    url = f"http://explosm.net/comics/{str(comicNr)}/"
    try:
        # GET info from URL
        content = urlopen(url).read()
        # Parse the info as HTML
        soup = BeautifulSoup(content, "html.parser")
        # Find the src tag of the image
        encodedUrl = f"http:{quote(soup.find('img', {'id': 'main-comic'}).get('src'))}"
        # Some images have text after the MIMEtype, so we get rid of that first
        # The text always starts with a ?, which looks like "%3F" when encoded
        endIndex = encodedUrl.find("%3F")
        encodedUrl = encodedUrl[:endIndex]
        # Now we can extract the MIMEtype and save it to disk
        mime = encodedUrl[-4:]
        # Download the image as a file
        urlretrieve(encodedUrl, f"Comic - {str(comicNr)}{mime}")
    except:
        print("Error, URL might not exist")

    comicNr = comicNr + 1
    print(f"{upperLimit - comicNr} iterations left")

"""
# Read the file and iterate over the items (this could have been done by just iterating 
f = open('URLLIST.txt', 'r')
fileString = []
counter = 0
for line in f:
    fileString.append(line)
for item in fileString:
    counter = counter + 1
    try:
        print(item)
        print(item.endswith('.jpg\n') or item.endswith('.JPG\n'))
        '''
        if item.endswith('.jpg\n') or item.endswith('.JPG\n'):
            urlretrieve(item, "Number " + str(counter) + ".jpg")
        elif item.endswith('.png\n') or item.endswith('.PNG\n'):
            urlretrieve(item, "Number " + str(counter) + ".png")
        elif item.endswith('.gif\n') or item.endswith('.GIF\n'):
            urlretrieve(item, "Number " + str(counter) + ".gif")
        '''
    except:
        print('Your program sucks\n')
f.close


"""


# Example url
#<img id="main-comic" src="//files.explosm.net/comics/Kris/scrubs.png?t=A87A41">

