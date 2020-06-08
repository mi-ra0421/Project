# 아래는 구글링한 심플코드 &참고 사이트
# : https://www.fun-coding.org/crawl_basic3.html 
# https://m.blog.naver.com/PostView.nhn?blogId=pearl097&logNo=221529275979&proxyReferer=https:%2F%2Fwww.google.com%2F

import requests
from urllib.parse import urlparse
import json

def blog_response(keyword, display, page) :
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword +  "&display=" + str(display) + "&start="+ str(page)
    #str 숫자에 따라 display 숫자 변경됨 & start는 시작 페이지 지정
    response = requests.get(urlparse(url).geturl(), headers = {"X-Naver-Client-Id": "QgFhALP0ksVRg5GeQSWe", "X-Naver-Client-Secret":"UC2Ji2K2ak"})
    return response.json()

keyword = "식기세척기"

data = blog_response(keyword, 10, 2)
# print(data)

title=data['items']['tile']
# print(title)
link=data['items']['link']
description=data['items']['description']
bloggername=data['items']['bloggername']
bloggerlink=data['items']['bloggerlink']
postdate=data['items']['postdate']

#★★★★질문★★★★★
# 20번쨰줄 print(title) 실행 시, 'title=data['items']['title'] 
# TypeError: list indices must be integers or slices, not str
# (venv)''라고 뜸. 몇번째 title부터 print해야하는지 지정되지 않아
# 에러가 나는 것 같은데... 전체 title 리스트를 터미널에서 뜨게 하려면 어떻게 해야하나요?
# https://jhnoru.tistory.com/19 참고해서 아래처럼 반복문 썼는데.. 어디가 잘못된건지...
# for i in data : 
#     title=list.append[i[data['items']['title']]]
# print(title)


# ★할일1. Json 파일로 저장할 내용 및 형태 지정?
# for blogreview in blogreviews
# blogreviews=[title,link,description,postdate]

# ★할일2. json파일로 저장하기
# file=open(".blogreview.json", "w+")
# file.json(json.dumps(blogreviews))

# ★할일3. DB에 저장?




# --------------------------




# 아래 참조 : 네이버 제공 api
# import os
# import sys
# import urllib.request
# from urllib.parse import quote

# client_id = "QgFhALP0ksVRg5GeQSWe"
# client_secret = "UC2Ji2K2ak"
# encText = urllib.parse.quote("식기세척기")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     #추가:result 저의
#     result=response_body.decode('utf-8')
#     print(result)
# else:
#     print("Error Code:" + rescode)

