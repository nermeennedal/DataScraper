import requests 
from bs4 import BeautifulSoup
import csv 


date = input("Please enter the date in the following format DD/MM/YYYY : ")

DATAPAGE= requests.get(f"https://www.yallakora.com/match-center?date={date}#days")
