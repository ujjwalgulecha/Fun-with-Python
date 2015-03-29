import requests
from bs4 import BeautifulSoup

admit=0
reject=0
print 'Decisions 2015 for your University'
for numb in range(1,17):
	
	url = "http://thegradcafe.com/survey/index.php?q=computer+science&t=a&pp=250&o=&p=" + str(numb)
	r=requests.get(url)

	soup = BeautifulSoup(r.content)

	p_data = soup.find_all("tr")


	for item in p_data:
		va = (item.contents[2].text)
		ga = (item.contents[0].text)
		if "USC" in ga or "usc" in ga or "University Of Southern California" in ga:
			if '2015' in item.contents[2].text:
				
						
				if 'Masters' in item.contents[1].text:
				
					if 'Rejected' in item.contents[2].text:
						print va
						reject=reject+1
				
					if 'Accepted' in item.contents[2].text:
						admit=admit+1
				
print("Admits: %d" % (admit))
print("Rejects: %d" % (reject))
print("Total: %d" % (admit+reject))

