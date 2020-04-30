import sys
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Data:
    __res1 = ""
    __res2 = ""
    def __init__(self):
        self.completeSite = ""
        try:
            self.__res1 = requests.get('https://escapefromtarkov.gamepedia.com/Category:Quests')
            self.__res2 = requests.get('https://escapefromtarkov.gamepedia.com/index.php?title=Category:Quests&pagefrom=What%27s+on+the+flash+drive%3F#mw-pages')
        
        except:
            print("Error rerading quests")
        #print(res.status_code)
        #print(res.text)

    def __getAllMissions(self, res):
        res = BeautifulSoup(res.text, "html.parser")
        #print(res)
        
        for allMissions in res.select(".mw-category-generated"):
            allMissions = allMissions.findAll("a")

        linksToMissions = {}
        for mission in allMissions:
            if "/ko" not in mission.text:
                linksToMissions[mission.text] = mission.attrs["href"]
        
        nextPage = ""
        if "next page" in linksToMissions:
            nextPage = linksToMissions.pop("next page")
        elif "previous page" in linksToMissions:
            del linksToMissions["previous page"]

        #print(nextPage)
        #print(linksToMissions)
        return linksToMissions
        

    def transformMissions(self):
        links1 = self.__getAllMissions(self.__res1)
        links2 = self.__getAllMissions(self.__res2)

        links = links1.copy()
        links.update(links2)
        #print(links)

        count = 0
        transformedMissions = {}
        transformedMissions["timestamp"] = {"date": datetime.now().strftime("%d-%m-%y"), "time": datetime.now().strftime("%H-%M-%S")}

        for name, link in links.items():
            count += 1

            try:
                #print("---------------------------" +link+ "---------------------------")
                time.sleep(0.5)
                mission = requests.get('https://escapefromtarkov.gamepedia.com' + link)
                mission = BeautifulSoup(mission.text, "html.parser")
                

            except requests.exceptions.SSLError as e:
                print("Error reading mission")
                #mission = "<h1> Error </h1>"

            name = mission.select_one("h1").text
            if name == "Quests" or name == "Quests/zh":
                continue

            transformedMissions[name] = ({"favorite": 0})

            infoxbox = []
            for temp in mission.select(".va-infobox-content"):
                if "previous:" not in temp.text and "leads to:" not in temp.text:
                    infoxbox.append(temp.text)

            transformedMissions[name].update({"infobox": infoxbox})

            liste = []
            for headlines in mission.select("h2 span"):

                #print(headlines.next_sibling)
                #print(headlines.attrs)
                if "class" not in headlines.attrs:
                    continue

                if headlines.attrs["class"][0] == "mw-headline":
                
                    temp = headlines.parent
                
                    for tag in temp.next_siblings:       
                        if tag.name == "ul" or "table":
                            #print(tag.name)
                            if (tag.name == "h2") or (tag.name == "table" and "class" in tag.attrs and tag.attrs["class"][-1] == "va-navbox-bottom"):
                                transformedMissions[name].update({headlines.text: liste})
                                liste = []
                                break

                            if hasattr(tag, "text"):
                                liste.append(tag.text.strip())

                            if tag.name == "table" and "class" in tag.attrs or tag.name == "p" or tag.name == "li":
                                #print(tag.findAll("img"))
                                for image in tag.findAll("img"):
                                    #print(image.attrs["src"])
                                    liste.append(image.attrs["src"])

            completeSite = mission.find("div", {"id": "bodyContent"})
            #print(completeSite.findAll("img"))
            for editSpan in completeSite.select("span[class='mw-editsection']"):
                editSpan.extract()

            for questList in completeSite.select("table[class='va-navbox-border va-navbox-bottom']"):
                questList.extract()

            for questHeader in completeSite.select("div[class='catlinks']"):
                questHeader.extract()

            for infoxbox in completeSite.select("table[class='va-infobox']"):
                infoxbox.extract()

            for jumper in completeSite.select("div[class='mw-jump']"):
                jumper.extract()

            for hidden in completeSite.select("div[class='noprint']"):
                hidden.extract()

            for image in completeSite.select("a[class='image']"):
                image.attrs["href"] = image.contents[0].attrs["src"]
                #print(image.attrs["href"])

            for aLink in completeSite.select("a"):
                try:
                    if "class" in aLink.attrs.keys():
                        for attr in aLink.attrs["class"]:
                            if attr == "image":
                                #print(aLink.contents[0])
                                pass

                            else:
                                newTag = BeautifulSoup(features="html.parser").new_tag("b")
                                newTag.string = aLink.text
                                aLink.replace_with(newTag)
                    else:
                        newTag = BeautifulSoup(features="html.parser").new_tag("b")
                        newTag.string = aLink.text
                        aLink.replace_with(newTag)

                except Exception as e:
                    print(e)

            #print(completeSite)
            # print(completeSite)

            transformedMissions[name].update({"completeSite": str(completeSite)})

            if (count % 10) == 0:
                print(count)

            #print(mission) 
            #if count == 8:
            #   break
        print(str(count) + " missions loaded")
        return transformedMissions

    def getCompleteSite(self):
        return self.completeSite
