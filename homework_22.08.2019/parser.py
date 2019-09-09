import urllib.request
import urllib.parse
from lxml.html import fromstring


class MyParser:
    def __init__(self, url="http://127.0.0.1:5000/"):
        self.my_site_url = url

    def par_site(self, xPath="/html/head/title"):
        response = urllib.request.urlopen(self.my_site_url).read().decode('utf8')
        page = fromstring(response)
        print(response)
        print(page)
        s = page.xpath(xPath)
        return s


myHeader = MyParser()
print(myHeader.par_site())
