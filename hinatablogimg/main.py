# vi: set et sw=4 ts=4 softtabstop=4 :
import re
import requests
import datetime
from bs4 import BeautifulSoup


Key = re.compile(r'(?<=src=")https://cdn.hinatazaka46.com.*?14.*?g(?=")')

def main():
    for x in range(1,10):
        Yesterday = GetYesterday(x)
        if Yesterday == "20210105":
            break
        else:
            print(Yesterday)
            hinata_url = "https://www.hinatazaka46.com/s/official/diary/member/list?ima=0000&dy=" +Yesterday
            hinata_html = requests.get(hinata_url)
            soup = BeautifulSoup(hinata_html.content, "html.parser")
            Body = soup.find_all("body")
            Bodystr = str(Body)
            #m = "https://cdn.hinatazaka46.com/images/14/0f9/6ed736aa794c59be511fbe3d3303e.jpg"
            ImageURL_List = re.findall(Key,Bodystr)
            del ImageURL_List[-8:]
            del ImageURL_List[:2]
            for Index,ImageURL in enumerate(ImageURL_List):
                indexNumber = str(Index)
                lmg = requests.get(ImageURL)
                with open("./img/hinatablog/"+Yesterday+"["+indexNumber+"].jpg",'wb') as file:
                    file.write(lmg.content)

def GetYesterday(x):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=x)
    yestey = today - oneday
    newyesteyday = str(yestey)
    lastyesteyday = newyesteyday.replace("-","")
    return lastyesteyday

main()
