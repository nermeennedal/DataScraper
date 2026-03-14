import requests 
from bs4 import BeautifulSoup
import csv 


date = input("Please enter the date in the following format DD/MM/YYYY : ")

Datapage= requests.get(f"https://www.yallakora.com/match-center?date={date}#days")

def Soup(data):
    cont = data.content
    contentsoup = BeautifulSoup(cont,"lxml")
    print(f"Contents before find all {contentsoup}")
    print("##########################################################################################################################")
    champoions= contentsoup.find_all("div",{'class':'matchCard'})
    print(f"Champions after find all : {champoions}")
    print("########################################################################################################################")
    return champoions

def get_match_info(champoions):
    champoions=Soup(champoions)
    champion=champoions[0].contents[0]
    return champion

Soup(Datapage)

































# def work(Datapage):
#     soup=BeautifulSoup(Datapage.content,"lxml")
#     champoions =soup.find_all("div",{'class':'matchCard'}) 
#     Matches=[]
#     x=champoions[0].contents[0].find('h2').text
#     return x

# print(work(Datapage))


# def content(Datapage):
#     dictionary=work(Datapage)
#     list1 = dictionary.contents[0]
#     return list1

# def work2():
#     print(content(Datapage))


