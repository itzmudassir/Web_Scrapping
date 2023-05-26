from bs4 import BeautifulSoup
import requests
import smtplib
import time
from csv import writer
for i in range(1,440):
    lahore =f"https://www.pakwheels.com/used-cars/search/-/ct_lahore/?page={i}"
    page_lahore=requests.get(lahore)
    soup_lahore=BeautifulSoup(page_lahore.content,"html.parser")
    car_lahore=soup_lahore.find_all('div',class_="col-md-9 grid-style")
    with open("cars.csv","a",newline="") as f:
        thewter=writer(f)
        header=["Name","Price","Update"]
        thewter.writerow(header)
        for cars in car_lahore:
            name=cars.find("a",class_="car-name ad-detail-path")
            name=name["title"]
            price = cars.find("div",class_="price-details generic-dark-grey").text.replace("\n\n", "").replace("\n","").replace(" ", "")
            
            update = cars.find("div",class_="pull-left dated").text
            info=[name,price,update]
            print(info)
            thewter.writerow(info)