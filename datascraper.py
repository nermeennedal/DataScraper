import requests 
from bs4 import BeautifulSoup
import csv 


date = input("Please enter the date in the following format DD/MM/YYYY : ")

Datapage= requests.get(f"https://www.yallakora.com/match-center?date={date}#days")

def work(Datapage):
    soup=BeautifulSoup(Datapage.content,"lxml")
    champoion =soup.find_all("div",{'class':'matchCard'}) 
    Matches=[]
    return champoion

def content(Datapage):
    dictionary=work(Datapage)
    list1 = dictionary.contents[0]
    return list1

def main():
    print(content(Datapage))

main()
