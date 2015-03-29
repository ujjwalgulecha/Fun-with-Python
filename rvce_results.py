import requests
from bs4 import BeautifulSoup

formData = {'usn':'1RV11IS001',"get_result":"Get_Result"}
r = requests.post("http://www.rvce.edu.in/results/result_view.php?result_id=42", data = formData)
soup = BeautifulSoup(r.content)
p_data = soup.find_all("html")

print p_data
