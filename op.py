from  collections import defaultdict
from bs4 import BeautifulSoup
import requests
key  =  input("Enter the product name : ")
key  = key.replace(" ", "+")


def flipkart(key):
    url_flip = "https://www.flipkart.com/search?q=" + key+"10&page=1"
    
    map = defaultdict(list)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    source_code = requests.get(url_flip, headers=headers)
    soup = BeautifulSoup(source_code.text, "html.parser")
    home = 'https://www.flipkart.com'
    for block in soup.find_all('div', {'class': '_2kHMtA'}):
            title, price, link, rating  = None, 'Currently Unavailable', None, None
            for heading in block.find_all('div', {'class': '_4rR01T'}):
                title = heading.text
            for p in block.find_all('div', {'class': '_30jeq3 _1_WHN1'}):
                price = p.text[1:]
            for rate in block.find_all('div', {'class':'_3LWZlK'}):
                rating  = rate.text
            for l in block.find_all('a', {'class': '_1fQZEK'}):
                link = home + l.get('href')
            map[title] = [price, link, rating]
    return map
def amazon(key):
   
    url_amzn ='https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' +str(key)
    map = defaultdict(list)
    headers = {
            'authority': 'www.amazon.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

    source_code = requests.get(url_amzn, headers=headers)
    soup = BeautifulSoup(source_code.text, "html.parser")
    home = 'https://www.amazon.in'
    map  = defaultdict(list) 

    for html in soup.find_all('div', {'class': 'sg-col-inner'}):
            title, link,price, rating = None, None,None, None 
            for heading in html.find_all('span', {'class': 'a-size-medium a-color-base a-text-normal'}):
                title = heading.text
            for p in html.find_all('span', {'class': 'a-price-whole'}):
                price = p.text
            for l in html.find_all('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}):
                link = home + l.get('href')
            for rate  in  html.find_all("span", {'class':'a-icon-alt'}):
                # split = rate.split("a-icon a-icon-star-small")
                split  = rate.text.split(" ")[0]
                rating  =  split
                
                
            if title and link:
                map[title] = [price, link, rating]
    return map 

def croma(key):
    url_croma  =  "https://www.croma.com/search/?q="+key
    map  = defaultdict(list)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    source_code  = requests.get(url_croma)
    soup = BeautifulSoup(source_code.text, "html.parser")
    home  = 'https://www.croma.com'
    # print(source_code.text)
    print(soup.find_all('div',{'class':'cp-product typ-plp'} ))
    for html in soup.find_all('div', {'class':'cp-product typ-plp'}):
        print(html)
        
        
    
croma(key) 
# print(amazon(key))
    
