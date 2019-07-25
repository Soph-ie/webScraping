from urllib.request import urlopen as uReq #grab the url text
from bs4 import BeautifulSoup as soup # parse the url text

my_url= 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#opens uo connection and grabs the page
uClient= uReq(my_url)
page_html=uClient.read()
#close the client
uClient.close()
#parse the webpage
page_soup=soup(page_html, "html.parser")

 #grabs
containers = page_soup.findAll("div", {"class": "item-container"})

filename = 'products.csv'

f= open (filename, 'w')
headers = "product_name, shiping \n"
f.write (headers)

#LOOPING TO GET THE BRAND OF THE GRAPHICS CARD
for container in containers:
	#brand= container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name= title_container[0].text

	shipping_cotainer = container.findAll ("li", {"class": "price-ship"})
	shiping= shipping_cotainer[0].text.strip()


	#print("brand"+ brand)
	print("product_name"+ product_name)
	print("shiping"+ shiping)

	f.write(product_name.replace(',','|')+ ',' + shiping +'\n')

f.close()