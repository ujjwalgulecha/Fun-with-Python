import requests
from bs4 import BeautifulSoup

admit=0
reject=0
print 'UCSD Decisions 2015'
for numb in range(1,17):
	url = "http://thegradcafe.com/survey/index.php?q=computer+science&t=a&pp=250&o=&p=" + str(numb)
	#url ="http://thegradcafe.com/survey/index.php?q=ucsd+computer+science&t=a&pp=50&o=&p=1"
	r=requests.get(url)

	soup = BeautifulSoup(r.content)

	p_data = soup.find_all("tr",{"class":"row1"})



	ga = 'UCSD'
	#ga3 = 'Gatech'


	for item in p_data:
		va = (item.contents[0].text)
		if ga in va:
			if 'Rejected' in item.contents[2].text:
				reject=reject+1
	
			if 'Accepted' in item.contents[2].text:
				admit=admit+1
	
	#if ga2 in va:
	#	if 'Rejected' in item.contents[2].text:
	#		reject=reject+1
	#
	#	if 'Accepted' in item.contents[2].text:
	#		admit=admit+1
		
	#if ga3 in va:	
	#	if 'Rejected' in item.contents[2].text:
	#		reject=reject+1
	#
	#	if 'Accepted' in item.contents[2].text:
	#		admit=admit+1			

print("Admits: %d" % (admit))
print("Rejects: %d" % (reject))
print("Total: %d" % (admit+reject))

