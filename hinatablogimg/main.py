# vi: set et sw=4 ts=4 softtabstop=4 :
import re
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathlib import Path

from . import member
from .exceptions import HinatablogimgError

load_dotenv()

HINATADIR = os.environ.get("HINATABLOGIMG_HINATADIR", "./img")
CREATEDIR = True

def main():
    maxpage = 1
    for i in range(maxpage):
        fetch_one_page(i, HINATADIR)


def fetch_one_page(page, download_path):
    '''
    特定のページの画像をすべて保存する関数
    '''
    pageurl = "https://www.hinatazaka46.com/s/official/diary/member/list"
    query = {'ima': '0000',
             'cd': 'member',
             'page': page}
    res = requests.get(pageurl, params=query)

    if res.status_code != 200:
        errmsg = f'return code: {res.status_code} page: {page}'
        raise HinatablogimgError(errmsg)

    article_list = find_article(res.text)
    for article in article_list:
        fetch_one_article(article, download_path)


def find_article(htmltext):
    '''
    htmlテキストから記事データを抽出してリストで返す
    '''
    soup = BeautifulSoup(htmltext, 'html.parser')
    article_els = soup.find_all('div', class_='p-blog-article')
    return article_els[:6]


def fetch_one_article(article_data, download_path):
    '''
    article_dataで指定された記事の画像をすべて保存する関数
    '''
    memberstr = find_memberstr(article_data)
    datestr = find_datestr(article_data)
    imgurls = find_imgurllist(article_data)
    for index, imgurl in enumerate(imgurls):
        suffix = imgurl.split('.')[-1]
        imgname = f'{memberstr}_{datestr}_{index:0>2}.{suffix}'
        memberdir = Path(download_path, memberstr)
        if CREATEDIR is False:
            memberdir = download_path
        register_img(imgurl, imgname, memberdir)


def find_memberstr(htmltext):
    '''
    記事情報からメンバー名を抽出する関数
    '''
    memberstr_el = htmltext.find('div', class_='c-blog-article__name')
    memberstr_ja = memberstr_el.text.strip()
    memberstr = member.get(memberstr_ja, 'unknown')
    return memberstr


def find_datestr(htmltext):
    '''
    記事情報から日付の部分を抽出する関数
    '''
    datestr_el = htmltext.find('div', class_='c-blog-article__date')
    datestr = datestr_el.text.strip()
    # 2021.1.9 09:00
    articledate = datetime.strptime(datestr, '%Y.%m.%d %H:%M')
    # 20210109
    filenamestr = articledate.strftime('%Y%m%d%H%M%S')
    return filenamestr


def find_imgurllist(htmltext):
    '''
    記事情報から画像のURLを抽出してリストで返す
    '''
    article_body = htmltext.find('div', class_='c-blog-article__text')
    img_els = article_body.find_all('img')
    # バグってるimg要素を探す
    for img_el in img_els:
        if len(img_el.text) > 0:
            return find_imgurllist_bug(htmltext)
    imgurls = [img_el.attrs['src'] for img_el in img_els
               if 'src' in img_el.attrs]
    return imgurls


def find_imgurllist_bug(htmltext):
    '''
    imgタグがバグって取得できない記事に対して正規表現を用いてimgurlを取得する
    '''
    searchimg = re.compile(r'<img [^>]*>')
    searchsrc = re.compile(r'src="([^"]*)"')
    matchimg = re.findall(searchimg, str(htmltext))
    imgurls = []
    for imgstr in matchimg:
        matchurl = re.search(searchsrc, imgstr)
        if matchurl:
            imgurls.append(matchurl.group(1))
    return imgurls


def register_img(imgurl, imgname, download_dir):
    '''
    画像URLから画像を取得してdownload_pathに保存する関数
    '''
    download_path = Path(download_dir)
    if not download_path.exists():
        download_path.mkdir(mode=0o755, parents=True)
    res = requests.get(imgurl)
    imgpath = Path(download_path, imgname)
    print(imgpath)
    with imgpath.open('wb') as fd:
        fd.write(res.content)
