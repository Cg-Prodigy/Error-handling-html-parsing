from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def errorHandler(url):
    try:
        urlObj=urlopen(url)
    except HTTPError as e:
        return e
    except URLError:
        return 'Mistyped URL. Server is currently down'
    try:
        bsObj=BeautifulSoup(urlObj.read(), 'html5lib')
    except AttributeError:
        return 'Element is not present'
    return bsObj
    