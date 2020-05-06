from PyQt5.QtNetwork import *
from bs4 import BeautifulSoup
import urllib.request
from os import path
import os

class missionDetails:
    def __init__(self, data):
        self.data = data

    def getDetails(self, row):
        details = []
        index = 0
        for name, mission in self.data.items():
            if name == "timestamp":
                continue

            if index == row:
                details = self.data[name]["completeSite"]
                imageCount = 0
                for headline, content in mission.items():
                    if "https:" in str(content):
                        soup = BeautifulSoup(str(content), "html.parser")
                        soup2 = BeautifulSoup(details, "html.parser")

                        linksToImages = soup.findAll("img")

                        for link in linksToImages:
                            #print(link)
                            if hasattr(link, "src"):
                                imageCount += 1
                                self.systemLink = self.downloadImage(link.attrs["src"], name, imageCount)

                                allImgs = soup2.findAll("img")
                                allImgs[imageCount - 1].attrs["src"] = self.systemLink
                                details = str(soup2)
                                #print(allImgs[imageCount - 1].attrs["src"])

            index += 1
        return details

    def downloadImage(self, link, name, imageCount):
        cwd = os.getcwd()

        name = name.replace(' -', '')
        name = name.replace('"', '')


        if not path.exists(cwd + '/data/missionImages/' + name):
            os.makedirs(cwd + '/data/missionImages/' + name)

        if not path.exists(cwd + '/data/missionImages/' + name + '/' + str(imageCount) + ".jpg"):
            urllib.request.urlretrieve(link, cwd + '/data/missionImages/' + name + '/' + str(imageCount) + ".jpg")
            #print("DOWNLOAD " + str(imageCount))

        else:
            #print("CACHE " + str(imageCount))
            pass

        return cwd + '/data/missionImages/' + name + '/' + str(imageCount) + ".jpg"