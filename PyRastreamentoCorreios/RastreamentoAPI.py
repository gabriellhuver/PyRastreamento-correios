import requests
from bs4 import BeautifulSoup
import time

BASEURL = "https://www.linkcorreios.com.br/"


def rastrear(codigo):
        page = requests.get(BASEURL + codigo)
        soup = BeautifulSoup(page.text, "html.parser")
        tdList = soup.find_all("td")
        statusList = []
        for i in range(len(tdList)):
            try:
                time.strptime(tdList[i].getText(), "%d/%m/%Y %H:%S")
                data = tdList[i].getText()
                status = tdList[i + 1].getText()
                try:
                    if "Local:" in tdList[i + 2].getText():
                        local = tdList[i + 2].getText()
                    else:
                        local = ""
                except:
                    local = ""
                try:
                    if "Origem:" in tdList[i + 2].getText():
                        origem = tdList[i + 2].getText()
                    else:
                        origem = ""
                except:
                    origem = ""
                try:
                    if "Destino:" in tdList[i + 3].getText():
                        destino = tdList[i + 3].getText()
                    else:
                        destino = ""
                except:
                    destino = ""
                statusList.append(
                    {
                        "data": data,
                        "status": status,
                        "local": local,
                        "origem": origem,
                        "destino": destino,
                    }
                )
            except:
                pass
        return reversed(statusList)
    

