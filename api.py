#의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

from tkinter import * 
from urllib.parse import urlencode, unquote, quote_plus
import requests
import json
import tkinter.messagebox

##### api를 불러오는 코드는 api 명세서를 참고. #####

# 인자로 입력받은 지역명을 받아왔음 
def api(sido) : 
    # 오류 없이 작동 된다면 아래의 코드 실행. 
    try: 
        url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtrvnRltmMesureDnsty'

        # 시크릿 키 들어있는 secret.json 파일 열기 
        with open ("secret.json") as file : 
            # secret 에 json 내용을 저장 
            secret = json.loads(file.read())

        # 전송할 파라미터 입력 
        # quote_plus : 한글은 url 이 들어가면 깨지기 때문에 안 깨지도록 quote_plus 사용
        params = "?" + urlencode({
            quote_plus('serviceKey'): secret["SECRET"], # 시크릿 키를 json 파일에서 불러오기
            quote_plus('returnType'): 'json', # 받아오는 데이터 형식을 json 으로 받는다. 
            quote_plus('numOfRows'): '10', # 몇 개의 데이터를 받을지 
            quote_plus('pageNo'): '1', # 몇 페이지를 받을지 
            quote_plus('sidoName'): sido, # 인자로 받아온 지역명을 파라미터로 추가 
            quote_plus('ver'): '1.3', 
        })

        # reponse 를 get 형식으로 받아 data 에 저장 
        # unquote : 한글로 보내준 url 을 풀어준다. 
        data = requests.get(url + unquote(params))

        # json 형식을 딕셔너리 형태로 저장 
        res = data.json()

        # 원하는 데이터 값을 text에 저장 (리스트)
        text = res['response']['body']['items']

        # text 를 리턴 
        return text
    
    # api 에서 데이터를 가져오는 과정에서 오류가 발생하면 경고창을 실행 
    except: 
        return (tkinter.messagebox.showerror("Error!", "API 에서 데이터를 가져올 수 없습니다. "))