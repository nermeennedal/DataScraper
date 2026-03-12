import requests 
from bs4 import BeautifulSoup
import csv 


date = input("Please enter the date in the following format DD/MM/YYYY : ")

Datapage= requests.get(f"https://www.yallakora.com/match-center?date={date}#days")

def work(Datapage):
    soup=BeautifulSoup(Datapage.content,"lxml")
    champoion =soup.find_all("div",{'class':'matchCard'}) 
    Matches=[]
    print(champoion)
work(Datapage)