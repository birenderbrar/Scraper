from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests 
import json
import time


app = Flask(__name__)
ask = Ask(app, "/")

res = requests.get('https://www.worldometers.info/coronavirus/')
soup = BeautifulSoup(res.text, "html.parser", parse_only=SoupStrainer(id="main_table_countries_today"))
covid_data = []
country = {}   

def get_all_table(soup_object): 
    table_body = soup_object.find('tbody')
    rows = table_body.find_all('tr')


    for row in rows:
        cols = row.find_all('td')
        covid_data.append([i.text.strip() for i in cols])
    for each_country in covid_data: 
        country_name = each_country[0]
        country_total_number = each_country[1]
        country[country_name] = country_total_number
    print(country['India'])    
    return country
@ask.launch
def start_skill():
    welcome_msg = render_template('welcome')
    reprompt = render_template('reprompt')
    return question(welcome_msg).reprompt(reprompt)
 
@ask.intent("YesIntent", convert={'Country': str})
def share_data():
    data = get_all_table(soup)
    response = render_template("no_of_cases", country = Country, Data = data)
    return statement(response)


@ask.intent("NoIntent")
def no_intent():
    out = render_template('out_message')
    return statement(out)

if __name__ == '__main__':
    app.run(debug=True)        
