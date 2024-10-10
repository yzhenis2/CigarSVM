#Yelaman Zhenis
import requests 
from bs4 import BeautifulSoup
import csv 

#list of user agents
userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'


for page in range(1,304):
    # Making a GET request 
    r = requests.get('https://www.cigaraficionado.com/ratings/search?brand=&countries[0]=+Cuba&q=&taste_date=&page='+str(page), headers={'User-Agent': userAgent})


      
    # Parsing the HTML 
    soup = BeautifulSoup(r.content, 'html.parser')

    cigar_class = soup.find('div', class_='content-cigarcard')
      
    # find all the anchor tags with "href"  
    for link in cigar_class.find_all('a', class_="col order-md-last"): 
        print(link.get('href'))
