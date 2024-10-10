import requests 
from bs4 import BeautifulSoup
import csv 

#list of user agents
userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0'
file = open('cigarlinks.txt','r')
cigarreview_csv  = 'cigarreview.csv'
lines = file.readlines()
#Yelaman Zhenis
count = 1
field_names = ['Cigar Name','Cigar Score','Cigar Length','Cigar Gauge','Cigar Strength','Cigar Size','Cigar Review']

with open(cigarreview_csv, 'a',encoding='utf-8') as f:
    writer = csv.writer(f,lineterminator='\n' )
    for line in lines:
        count +=1
        data = {}
        # Making a GET request
        r = requests.get('https://www.cigaraficionado.com'+str(line), headers={'User-Agent': userAgent})


          
        # Parsing the HTML 
        soup = BeautifulSoup(r.content, 'html.parser')

        cigar_name = soup.find('div', class_='col-9 col-md-10 ml-auto order-1 cigar-detail_title')
        cigar_name = cigar_name.find('div', class_ = 'row')
        cigar_name = cigar_name.find('div', class_ = 'col')
        #cigar_name = cigar_name.find('h1')
        cigar_name = cigar_name.h1.get_text()
        print(cigar_name)

        cigar_attr = soup.findAll('div', class_='col-6 col-md-3 col-lg-3 attributes-item pr-lg-24 pr-xl-49')
        cigar_score = soup.find('div', class_='col-9 col-md-10 ml-auto order-2 order-md-3 cigar-detail_attributes')
        cigar_score = cigar_score.find('div', class_ = 'attributes-item_scorebox')
        cigar_score = cigar_score.div.get_text()
        

        #cigar_score = cigar_score.find('div', class_ = '')
        #cigar_score = cigar_score.find('div', class_ = '')\

        cigar_length = cigar_attr[0]
        cigar_length = cigar_length.find('div', class_ = 'attributes-item_label')
        cigar_length = cigar_length.strong.get_text()


        cigar_gauge = soup.find('div', class_ = 'ring-gauge')
        cigar_gauge = cigar_gauge.strong.get_text()

        cigar_strength = cigar_attr[1]
        cigar_strength = cigar_strength.find('div', class_='attributes-item_label')
        cigar_strength = cigar_strength.strong.get_text()


        cigar_detail = soup.findAll('div', class_='col-12 col-md-6 col-lg-12')
        cigar_size = cigar_detail[0]
        cigar_size.find('strong',class_='cigar-detail_heading').decompose()
        cigar_size = cigar_size.find('p').get_text()
        cigar_size = cigar_size.strip()
        print(cigar_size)

        cigar_review = soup.find('div', class_='col-md-10 ml-auto order-3 order-md-2 cigar-detail_tastingnote')
        cigar_review.find('h3', class_ = 'd-md-none').decompose()
        cigar_review = cigar_review.find('p')
        cigar_review = cigar_review.get_text()

        cigar_issue_date = cigar_detail[1]
        cigar_price_date = cigar_issue_date.findAll('p', class_='mb-0')
        if len(cigar_price_date) < 4 and len(cigar_price_date)>2:
            cigar_date = cigar_price_date[2]
        elif len(cigar_price_date)<=2:
            cigar_date = cigar_price_date[1]
        else:
            cigar_date = cigar_price_date[3]
        cigar_date.find('strong',class_='cigar-detail_heading').decompose()
        cigar_date = cigar_date.get_text()
        cigar_date = cigar_date.split('–',1)[-1]
        cigar_date = cigar_date.strip()
        print(cigar_date)

        cigar_all = [cigar_name + cigar_date, cigar_score, cigar_length,cigar_gauge,cigar_strength,cigar_size,cigar_review]
        writer.writerow(cigar_all)
    f.close()
    
    

    
    
        

        
      
