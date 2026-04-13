import requests
from bs4 import BeautifulSoup
import json

urls =[]
base_url = "https://www.scrapethissite.com/pages/forms/"
Hockey_Teams= []
def scrap(url):
    Teams={}
    response = requests.get(url)
    # print(url)
    # print(response.status_code)
    soup = BeautifulSoup(response.content,"html.parser")
    # print(soup.prettify())

    tble = soup.find("table", class_="table")
    tr = tble.find_all("tr", class_="team")
    for i in tr:
        name = i.find("td", class_="name").get_text(strip=True)
        yr = i.find("td", class_="year").get_text(strip=True)
        win = i.find("td", class_="wins").get_text(strip=True)
        lose = i.find("td", class_="losses").get_text(strip=True)
        ot = i.find("td", class_="ot-losses").get_text(strip=True)
        winper = i.find("td", class_="pct").get_text(strip=True)
        gf = i.find("td", class_="gf").get_text(strip=True)
        ga= i.find("td", class_="ga").get_text(strip=True)
        diff = i.find("td", class_="diff").get_text(strip=True)
        Teams = {
            "name": name,
            "Year" : yr,
            "wins" :  win,
            "Loses" : lose,
            "Ot Loses" : ot,
            "Win %" : winper,
            "Goal For" : gf,
            "Gaol Against" : ga,
            "+/-" : diff  
        }
        Hockey_Teams.append(Teams)

for page in range(1, 25):
    url = f"{base_url}?page_num={page}"
    scrap(url)
    print(f"Scraped page {page}")

with open("teams.json", "w") as f:
    json.dump(Hockey_Teams, f, indent=4)







# for page_no in range(1,25):
#     url = f"{base_url}+{list_url}?page_num={page_no}"
#     page_num.append(url)
# print(page_num)

