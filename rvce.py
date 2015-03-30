import json
import requests
import re
from bs4 import BeautifulSoup

for numb in range(10,63):
	# each url is different based on the department
	url = 'http://www.rvce.edu.in/results/result_view.php?result_id=42'
	# sample once on the browser and copy the request headers (except POST: )
	header_str = '''
	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
	Accept-Encoding: gzip, deflate
	Accept-Language: en-US,en;q=0.5
	Connection: keep-alive
	Cookie: __utma=50120421.1716657859.1415098806.1427618920.1427693196.5; __utmz=50120421.1415098806.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=50120421; PHPSESSID=c93df27247c91eb850eedf3daec45b03; mypets=0c; __utmb=50120421.2.10.1427693196; __utmt=1
	Host: www.rvce.edu.in
	Referer: http://www.rvce.edu.in/results/result_view.php?result_id=42
	User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0
	'''
	lines = [line.strip() for line in header_str.split("\n") if line.strip()]
	headers = dict(
	    [line.split(": ") for line in lines]
	)
	payload = {
	    'usn': '1RV11IS0'+str(numb), # the usn number
	    'get_result': 'Get+Result'}
	session = requests.Session()
	r = session.post(url, data=payload, headers=headers)
	# parse this html with lxml.etree later and get it out
	soup = BeautifulSoup(r.content)
	name = soup(text=re.compile('Name'))
	p_data = soup.find_all("strong")
	print name
	print p_data

