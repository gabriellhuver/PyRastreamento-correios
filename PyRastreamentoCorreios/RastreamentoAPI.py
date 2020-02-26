import requests
from bs4 import BeautifulSoup
import time

BASEURL = "https://www.linkcorreios.com.br/"


def rastrear(codigo):
    page = requests.get(BASEURL + codigo)
    soup = BeautifulSoup(page.text, "html.parser")
    singlepost = soup.find("div", {"class": "singlepost"})
    statusList = []
    if singlepost:
        for status in singlepost.findAll("ul"):
            stsObject = {}
            sts = status.findAll("li")
            stsObject['status'] = sts[0].getText()
            stsObject['data'] = sts[1].getText()
            if "Local" in sts[2].getText():
                stsObject['local'] = sts[2].getText()
            elif "Origem" in sts[2].getText() and "Destino" in sts[3].getText():
                stsObject['origem'] = sts[2].getText()
                stsObject['destino'] = sts[3].getText()
            statusList.append(stsObject)
    returnStatus = {}
    returnStatus['status_list'] = statusList
    returnStatus['status_code'] = page.status_code
    return returnStatus
