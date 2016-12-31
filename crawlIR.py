from ../crawler import QueueADT

class Crawler:
    def __init__(self):
        pass

    def crawl(self,url,npages):
        # Take a url
        # Request the page using the requests library
        # http://docs.python-requests.org/en/master/


        # Go through and find the links
        # BeautifulSoup Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

        # Create a queue
        # loop on the queue

        # how to loop:
        # 1.) Process every item in the queue
        url = ""
        result = processURL(url)
        # 2.) If we hit npages then break loop


        pass

    def normalizeURL(self,url):
        pass

    def processURL(self, url):
        # Use requests to pull html

        # Use BeautifulSoup to extract texts in links

        # Return the result
        pass





if __name__ == '__main__':
    print("Did you mean to do that?")
