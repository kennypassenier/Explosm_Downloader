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
        # Some images have text after the file extension, so we get rid of that first
        # The text always starts with a ?, which looks like "%3F" when encoded
        endIndex = encodedUrl.find("%3F")
        if(endIndex != -1):
            encodedUrl = encodedUrl[:endIndex]
        # Now we can extract the file extension and save it to disk
        extension = encodedUrl[-4:]
        # Download the image as a file
        urlretrieve(encodedUrl, f"Comic - {str(comicNr)}{extension}")
    except:
        print("Error, URL might not exist")

    comicNr = comicNr + 1
    print(f"{upperLimit - comicNr} iterations left")
