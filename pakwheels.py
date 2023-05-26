import requests
from bs4 import BeautifulSoup

url = "https://www.pakwheels.com/used-cars/search/-/ct_lahore/?page=1"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

car_listings = soup.find_all('div', class_="col-md-9 grid-style")
# print(car_listings)

for listing in car_listings:
    name = listing.find('a', class_='car-name ad-detail-path')
    name = name['title']
    location_list = listing.find('div', class_='col-md-12 grid-date').text.strip()
    location_list = location_list.split('\n')
    # location_list = location_list[1]
    
    # if location_list:
    #     location = location_list[0].find_all('li')[0].text.strip()
    # else:
    #     location = "N/A"
    # last_update = listing.find('div', class_='pull-left dated').text.strip()
    # print("Name:", name)
    print("Location:", location_list[0])
    # print("Last Update:", last_update)
    # print("-----------------------")
