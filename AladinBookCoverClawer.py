# -*- coding: utf-8 -*-
"""
Author: Lukious
Member of BMCL
e-mail : zhsjzhsj@gmail.com
"""

from bs4 import BeautifulSoup
import urllib.request
import re
import os

categori_book =   [["인문학","https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=5&page=","&Stockstatus=1&PublishDay=84&CID=656&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax="],
                   ["중등참고서","https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=5&page=","&Stockstatus=1&PublishDay=84&CID=76000&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=#t"],
                   ["여행","https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=5&page=","&Stockstatus=1&PublishDay=84&CID=1196&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax="],
                   ["과학","https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=5&page=","&Stockstatus=1&PublishDay=84&CID=987&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax="],
                   ["대중예술","https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=5&page=","&Stockstatus=1&PublishDay=84&CID=517&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax="],
                   ["종교","https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=5&page=","&Stockstatus=1&PublishDay=84&CID=1237&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax="],
                   ["소설시","https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=5&page=","&Stockstatus=1&PublishDay=84&CID=1&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax="],
                   ["컴퓨터","https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=5&page=","&Stockstatus=1&PublishDay=84&CID=351&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=#"],
                   ["유아","https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=5&page=","&Stockstatus=1&PublishDay=84&CID=351&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=#"],
                   ["가정요리뷰티","https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=50&ViewType=Detail&PublishMonth=0&SortOrder=5&page=","&Stockstatus=1&PublishDay=84&CID=1230&CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=&PriceFilterMin=&PriceFilterMax=#"]]


def cleanText(readData):
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》()]', '', readData)
    return text

def get(max_cout = 1):
    count = 1
    
    DIR_NAME = str("./img/"+ categori_book[input_val][0])
    if not(os.path.isdir(DIR_NAME)):
        os.makedirs(os.path.join(DIR_NAME))
        
    while count <=max_cout:
        url = categori_book[input_val][1]+str(count)+categori_book[input_val][2]
        html = urllib.request.urlopen(url)
        source = html.read()
        soup = BeautifulSoup(source,"html.parser")
        tag = soup.findAll('div', attrs={'class': 'ss_book_box'})
        
        for i in range(len(tag)):
            name_tag_p2 = tag[i].find('div',attrs={'class':'ss_book_list'})
            name_tag_p1 = name_tag_p2.find('a',attrs={'class':'bo3'})
            name_tag = name_tag_p1.find('b')
            img_name = str(name_tag)[3:-4]
            img_name = cleanText(img_name)
            img_tag = tag[i].table.a.img
            image_url = img_tag.get("src")
            if image_url == "//image.aladin.co.kr/img/shop/19_150cover.png":
                pass
            else:
                urllib.request.urlretrieve(image_url,"./img/"+ categori_book[input_val][0]+"/"+img_name+".jpg")
        print("Number of images: " + str(count*50))
        count += 1
    else:
        print("Clawling Finished!")
        
        
for i in range(10):
    print(str(i) + " : "+categori_book[i][0]+'\n' )
input_val = int(input("input categori : "))
print("Clawling"+categori_book[input_val][0]+" book categori.")
amount = int(input("Amout of image? : "))
get(amount/50)
