import requests
from bs4 import BeautifulSoup
from CTkMessagebox import CTkMessagebox
import pandas as pd

def arzdigital_scraper(url, pages, scrap_name, scrap_price, scrap_market, scrap_volume, direction, format):
    all_data = []
    for page in range(1, pages+1):
        if page == 1:
            url = "https://arzdigital.com/coins/"
        else:
            url = f"https://arzdigital.com/coins/page-{page}/"

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers= headers)
        soup = BeautifulSoup(response.text, "html.parser")
        tbody = soup.find("tbody")
        rows = tbody.find_all("tr")

        for r in rows:
            row_data= {}
            try:
                if scrap_name:
                    name = r.find_all("span", class_=False)[1].get_text()
                    row_data["Coin's name"]= name.strip()
                if scrap_price:
                    price = r.find_all("span")[2].get_text()
                    row_data["Price($)"]= price.strip()
                if scrap_market:
                    market_cap = r.find("td", attrs={"class": "arz-coin-table__marketcap-td"}).find("span", class_= False).get_text()
                    row_data["Market Cap"]= market_cap.strip()
                if scrap_volume:
                    volume = r.find("td", attrs={"class": "arz-coin-table__volume-td"}).find("span", class_= False).get_text()
                    row_data["Volume"]= volume.strip()
                if row_data:
                    all_data.append(row_data)
                
                
            except Exception as e:
                print(f"Error while processing row: {str(e)}")


    if all_data:
        df = pd.DataFrame(all_data)
        try:
            if format == "xlsx":
                df.to_excel(f"{direction}", index=False, engine="openpyxl")

            elif format == "csv":
                df.to_csv(f"{direction}", index=False, encoding="utf-8-sig")
            CTkMessagebox(title="Success", message=f"{len(df)} coins saved!")
        except Exception as e:
            CTkMessagebox(title="Error", message=f"Could not save file: {str(e)}")
