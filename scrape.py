from bs4 import BeautifulSoup
import requests

headers = {'Content-Type': 'text/html', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

reponse = requests.get('https://internshala.com/internships/', headers=headers)

html = reponse.text

soup = BeautifulSoup(html, 'html.parser')

## <p> Tag + Class Name & Id
internships = soup.findAll('div', attrs={"class": "individual_internship"})

for item in internships:
    internship_meta = item.find('div', attrs={'class': 'internship_meta'})

    company_header_section = internship_meta.find('div', attrs={'class': 'individual_internship_header'}).find('div', attrs={'class': 'company'})

    role = company_header_section.find('h3', attrs={'class': 'profile'}).get_text().strip()
    company_name = company_header_section.find('h4', attrs={'class': 'company_name'}).get_text().strip()

    print(company_name, role)
