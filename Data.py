from requests import get
from bs4 import BeautifulSoup
from numpy import array

def pi():
    pis = BeautifulSoup(
        get("https://math.tools/numbers/pi/10000").text, 
        "html.parser"
    ).find("div", {"class": "pidata"}).text[3:].replace("\n", "")

    pil = [int(piv) for piv in pis]

    return array(pil)