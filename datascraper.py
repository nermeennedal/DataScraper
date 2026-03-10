import requests 
from bs4 import BeautifulSoup
import csv 


date = input("Please enter the date in the following format DD/MM/YYYY : ")

Datapage= requests.get(f"https://www.yallakora.com/match-center?date={date}#days")

def work(Datapage):
    beautifulsoup=BeautifulSoup(Datapage.content,"lxml")
    print(beautifulsoup)
work(Datapage)