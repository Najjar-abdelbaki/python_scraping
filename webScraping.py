import requests 
from bs4 import BeautifulSoup
import csv

url = 'https://www.tunisiepara.com/'
#get the data
data = requests.get(url)

def scraper(data):
    src = data.content
    soup = BeautifulSoup(src, 'lxml')
    prdetails = []
    
    produits = soup.find_all('div', {'class': 'product-warp-item columns large-3 medium-4 small-6 nasa-ver-buttons'})
    numPrd = len(produits)
    
    
    def get_name_produit(produits):
        nameProd = produits.contents[0].find('a', {'class': 'name woocommerce-loop-product__title nasa-show-one-line'}).text.strip()
        #print(nameProd)
        pric = produits.contents[0].find_all('span', {'class': 'woocommerce-Price-amount amount'})
        price = pric[1].text.strip()
        #print(price)
        img = produits.contents[0].find('img', {'class': 'attachment-woocommerce_thumbnail size-woocommerce_thumbnail'})
        src = img.get('src')
        #print(src)
            
        #add produit to prdetails
        prdetails.append({'nom_produit':nameProd, 'prix':price, 'img':src})
        
    for pr in range(numPrd):
        get_name_produit(produits[pr])
        
        
    
    keys = prdetails[0].keys()
    
    with open('C:\\Users\\Administrator\\Desktop\\miniProjet\\projectPortfolio\\projetPortfolioEnPython\\prouduiSCR.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(prdetails)
        print("file created")
    
    
scraper(data)
#load data into bs4(html)
# soup = BeautifulSoup(data.text, 'html.parser')
# produits = soup.find_all('div',{'class': 'product-info-wrap info'})


#print(soup.get_text())
#get data simply
#soup.select('div', {'class': 'main-img'})