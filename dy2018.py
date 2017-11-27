# encoding:UTF-8
import urllib.request
from bs4 import BeautifulSoup

baseurl = "http://www.dy2018.com/"


def zhuaqu(url):
    data = urllib.request.urlopen(url).read()
    return BeautifulSoup(data, 'html.parser', from_encoding='gbk')


def getmovieinfo(href):
    mv_sp = zhuaqu(baseurl+href)
    mv_info = mv_sp.find('div', id='Zoom')
    print(mv_info)


if __name__ == "__main__":
    soup = zhuaqu(baseurl)
    tags = soup.find_all('div', class_="co_area2")
    for tag in tags:
        title_tag = tag.find_next('div', class_="title_all").find_next('span')
        movies = tag.find_all('li')
        for mv in movies:
            title_mv = mv.find_next('a').get_text()
            href_mv = mv.find_next('a')['href']
            time = mv.find_next("span").get_text()
            print(title_mv + "|" + href_mv + "|" + time)
            getmovieinfo(href_mv)
        break;
