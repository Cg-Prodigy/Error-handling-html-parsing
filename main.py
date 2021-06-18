from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
# http://www.pythonscraping.com/pages/page1.html
def errorHandler(url):
    try:
        urlObj=urlopen(url)
    except HTTPError as e:
        return "{e}. Server doesn't exist. Error retrieving the page"
    except URLError:
        return 'Mistyped URL or Server is currently down'
    try:
        bsObj=BeautifulSoup(urlObj.read(), 'html5lib')
        result=bsObj.body.h2
    except AttributeError as e:
        return "{e}. Element doesn't exist".format(e)
    else: 
        return result
    
my_url= 'http://www.pythonscraping.com/pages/page1.html'
trial=errorHandler(my_url)
if trial==None:
    print("Element doesn't exist")
print(trial)