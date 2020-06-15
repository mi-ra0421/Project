# 따라한 참고 사이트 : https://m.blog.naver.com/PostView.nhn?blogId=pearl097&logNo=221529275979&proxyReferer=https:%2F%2Fwww.google.com%2F
# 참고 했으나 list함수 이후부터 이해못함 :  https://jeongwookie.github.io/2019/03/20/190320-collect-data-using-naver-search-api/

import requests
from urllib.parse import urlparse
import json
import pandas as pd
import numpy as np
import re

#step1. 데이터불러오기

with open('config.json', 'r', encoding="UTF-8") as f:
    config = json.load(f)
    # print(config)

def blog_response(keyword, display, start) :
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword +  "&display=" + str(display) + "&start="+ str(start)
    #str 숫자에 따라 display 숫자 변경됨 & start는 시작 글의 위치 지정(페이지x)
    response = requests.get(urlparse(url).geturl(), headers = {"X-Naver-Client-Id": config['naver-API-keyvalue']['X-Naver-Client-Id'], "X-Naver-Client-Secret":config['naver-API-keyvalue']['X-Naver-Client-Secret']})
    return response.json()

keyword = "식기세척기"

data = blog_response(keyword, 10, 1)  #1부터 10개 불러오기
# print(data)
# print(data['display'])
# print(data['start'])

def data_100results(keyword): 
    list_a = []
    for num in range(0,10):
        list_a = list_a + blog_response(keyword, 10, num * 10 + 1)['items'] #10 개씩 나온 리스트 더하기
    return list_a

result = data_100results(keyword)   
# print(result)

items = []

# print(result[0])
for i in result :

    title=i['title'].replace("<b>","").replace("</b>","")
    link=i['link']
    description=i['description'].replace("<b>","").replace("</b>","")
    bloggername=i['bloggername']
    bloggerlink=i['bloggerlink']
    postdate_year=i['postdate'][0:4]
    postdate_month=i['postdate'][4:6]
    postdate_data=i['postdate'][6:8]
    blogreview={'title':title, 'description':description}
    items.append(blogreview)
# print(items)

#step2. 데이터 저장

with open(".blogreview.json", "w+", encoding="UTF-8") as file:
    file.write(json.dumps(items, ensure_ascii=False))

with open('.blogreview.json', encoding="UTF-8") as json_file:
    json_data = json.load(json_file)
    # print(json_data)


#step3. 토큰화  참고 :  https://linguistech.tistory.com/13
blog = pd.read_json('.blogreview.json')
# print(df.count())
# print(df['title'])


from soynlp.tokenizer import RegexTokenizer, LTokenizer, MaxScoreTokenizer

tokenizer = RegexTokenizer()

##토큰화 테스트##
sample_index=5
sample_title= blog['title'][sample_index]
sample_description = blog['description'][sample_index]
# print(sample_title)
# print(sample_description)
tokened_title = tokenizer.tokenize(sample_title)
tokened_description = tokenizer.tokenize(sample_description)
# print(tokened_description)


##개행문자 제거##
def preprocessing(text):
    text = re.sub('\\\\n', ' ', text)
    return text

##개행문자 제거##
title_sentences = blog['title'].apply(preprocessing)
description_sentences = blog['description'].apply(preprocessing)
# print(title_sentences)

description_tokens = description_sentences.apply(tokenizer.tokenize)
title_tokens =title_sentences.apply(tokenizer.tokenize)
# print(description_tokens[:5])



#step4. 시각화

# 표시하지 않을 단어 추가
# stopwords_kr = ['하지만', '그리고', '그런데']  그림 보고 판단

# 워드클라우드를 그리는 함수 만들기
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 나눔고딕 설치 ★★★★★★★일단 실행을 위해 가져오고, 어떻게 하는건지 더 스터디하기

import matplotlib.font_manager as fm
fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf' 
font = fm.FontProperties(fname=fontpath, size=9)
get_ipython().run_line_magic('matplotlib', 'inline') 

# def displayWordCloud(data = None, backgroundcolor = 'white', width=800, height=600 ):
#     wordcloud = WordCloud(
#                         font_path = fontpath,
#                         stopwords = STOPWORDS, #★★★★★★★한국어는 불가? 다시 찾아보기
#                         background_color = backgroundcolor, 
#                          width = width, height = height).generate(data)
#     plt.figure(figsize = (15 , 10)) # figure 사이즈 변경
#     plt.imshow(wordcloud) # imshow : 이미지 출력
#     plt.axis("off")  # 축 표시 생략
#     plt.show() # 부가 정보 출력 생략

# displayWordCloud(' '.join(description_sentences))

#######추가로 할 일 : 불용어 제거 / 이미지 모양 바꾸기

