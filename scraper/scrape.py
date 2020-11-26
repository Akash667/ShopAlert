import requests
from bs4 import BeautifulSoup
import smtplib
import re

def extract_url(url):

    if url.find("www.amazon.in") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.in" + url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.in" + url[index:index2]
            else:
                url = None
    else:
        url = None
    return url

def get_converted_price(price):	

    converted_price = float(re.sub(r"[^\d.]", "", price)) 
    return converted_price



def get_product_details(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    details = {"name": "", "price": 0, "deal": True, "url": ""}
    _url = extract_url(url)
    if _url == "":
        details = None
    else:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        title = soup.find(id="productTitle")
        price = soup.find(id="priceblock_dealprice")
        if price is None:
            price = soup.find(id="priceblock_ourprice")
            details["deal"] = False
        if title is not None and price is not None:
            details["name"] = title.get_text().strip()
            details["price"] = get_converted_price(price.get_text())
            details["url"] = _url
        else:
            return None
    return details



print(get_product_details("https://www.amazon.in/Redmi-Note-Pro-Interstellar-Snapdragon/dp/B077PWBC78/ref=sxin_10?ascsubtag=amzn1.osa.459ba3bc-4058-48db-afc0-830536d942b4.A21TJRUUN4KGV.en_IN&creativeASIN=B077PWBC78&cv_ct_cx=phone&cv_ct_id=amzn1.osa.459ba3bc-4058-48db-afc0-830536d942b4.A21TJRUUN4KGV.en_IN&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-gl-ranking&dchild=1&keywords=phone&linkCode=oas&pd_rd_i=B077PWBC78&pd_rd_r=ca6096fe-444c-4a1f-90e3-be8e34122092&pd_rd_w=ZFIce&pd_rd_wg=8Z14t&pf_rd_p=e0ec3157-32a0-4197-a7f6-49f9023b486e&pf_rd_r=KAKZ18ZS2H5JMKN3255J&qid=1606379859&sr=1-1-5b72de9d-29e4-4d53-b588-61ea05f598f4&tag=technologytoday-21"))