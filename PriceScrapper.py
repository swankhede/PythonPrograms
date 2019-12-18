import bs4 
import requests
try:
    prod = input("enter product name")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    #url = "https://www.flipkart.com/search?q="+prod print(url)
    res = requests.get("https://www.flipkart.com/search?q="+prod)
    
    res1 = requests.get("https://www.amazon.in/s?k="+prod,headers=headers)
    print("res:",res1)
    print("res1:", res)
    soup1= bs4.BeautifulSoup(res1.text,'lxml')
    id1 = soup1.find('span',{"class":"a-price-whole"})
    soup = bs4.BeautifulSoup(res.text,'lxml')
    id = soup.find('div',{"class":"_1vC4OE"})
    print("flipkart:",id.text)
    print("amazon:",id1.text)
except OSError as e:
    print(e)
