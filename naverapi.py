# 따라한 참고 사이트 : https://m.blog.naver.com/PostView.nhn?blogId=pearl097&logNo=221529275979&proxyReferer=https:%2F%2Fwww.google.com%2F
# 참고 했으나 이해못함 :  https://jeongwookie.github.io/2019/03/20/190320-collect-data-using-naver-search-api/

import requests
from urllib.parse import urlparse
import json

def blog_response(keyword, display, page) :
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword +  "&display=" + str(display) + "&start="+ str(page)
    #str 숫자에 따라 display 숫자 변경됨 & start는 시작 페이지 지정
    response = requests.get(urlparse(url).geturl(), headers = {"X-Naver-Client-Id": "QgFhALP0ksVRg5GeQSWe", "X-Naver-Client-Secret":"UC2Ji2K2ak"})
    return response.json()

keyword = "식기세척기"

data = blog_response(keyword, 10, 3)
# print(data)

for i in data['items'] :
    # print(i['title']) ★★★★★★★왜 10개씩 3페이지, 총 30개인데 10개만 표시되는거지?? 앞에 print data는 전체 데이터 다 보여줌

    title=i['title'].replace("<b>","").replace("</b>","")
    link=i['link']
    description=i['description'].replace("<b>","").replace("</b>","")
    bloggername=i['bloggername']
    bloggerlink=i['bloggerlink']
    postdate_year=i['postdate'][0:4]
    postdate_month=i['postdate'][4:6]
    postdate_data=i['postdate'][6:8]
    # print(postdate_month) ★★★★★★★왜 10개씩 3페이지, 총 30개인데 10개만 표시되는거지??
    blogreview=[title,link,description,postdate_year, postdate_month, postdate_data] 
    # print(blogreview) ★★★★★★★왜 10개씩 3페이지, 총 30개인데 10개만 표시되는거지?? 

# ★★★★★★★ 아래와 같은 메세지가 터미널에 뜨는데, json 파일 저장법 관련 참고 자료 추천해주세요. 제가 찾은건 봐도...ㅠㅠ
# 그리고 위에 print(blogreview)의 출력물이 10개만 보이면, json파일에도 10개만 저장되나요? 30개 다 저장하려면 어떻게 해야하나요?
file=open(".blogreview.json", "w+")
file.json(json.dumps(blogreview))
print(json.dumps(blogreview))



# 추가로 할 일 : DB에 저장해보기




# --------------------------네이버 제공 api--------------------------
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

