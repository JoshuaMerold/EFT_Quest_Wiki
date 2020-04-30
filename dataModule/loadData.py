from bs4 import BeautifulSoup
from dataModule import requestData
import json

class loadData:
    def load(self):
        try:
            with open('data/savedMissions.json', 'r', encoding = "utf-8") as inputFile:
                data = json.load(inputFile)
                print(len(data))
                print("Data loaded successfully")
                return data

        except Exception as e:
            print("Error while loading")
            print(e)