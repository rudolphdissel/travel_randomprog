from requests import get
from bs4 import BeautifulSoup
import random

def extract_travel():
    url="https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EA%B8%B0%EC%B4%88%EC%9E%90%EC%B9%98%EB%8B%A8%EC%B2%B4_%EB%AA%A9%EB%A1%9D"
    response = get(url)
    if response.status_code != 200:
        print("웹 페이지에 오류가 있어서 지금은 안 되요 ㅠㅠ")
    else:
        print("프로그램 실행중...")
        result=[]
        soup = BeautifulSoup(response.text,"html.parser")
        citytable= soup.find('table', class_='wikitable')
        cityname= citytable.find_all('span',class_='flagicon')
        for city in cityname:
            anchors=city.find('a')
            cci=anchors['title']
            result.append(cci)
    return result