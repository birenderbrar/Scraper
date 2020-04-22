import requests 
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


res = requests.get('https://www.worldometers.info/coronavirus/')
# # Creation of bs4 object, which has all the methods
soup = BeautifulSoup(res.text, "html.parser", parse_only=SoupStrainer(id="main_table_countries_today"))

#getiing all the data in covid_data
covid_data = []   
def get_all_table(url): 
    table_body = url.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        covid_data.append([i.text.strip() for i in cols])
    return covid_data    


country = {}
def get_country_data(table):
    for each_country in table: 
        country_name = each_country[0]
        country_total_number = each_country[1]
        country[country_name] = country_total_number
    print(country)    
    return country
if __name__ == '__main__':
    get_all_table(soup)
    get_country_data(covid_data)
