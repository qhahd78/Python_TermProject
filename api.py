#의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

from tkinter import * 
from urllib.parse import urlencode, unquote, quote_plus
import requests
import json
import tkinter.messagebox

# 인수로 입력받은 지역명을 받아왔음 
def api(sido) : 
    # 오류 없이 작동 된다면 아래의 코드 실행. 
    try: 
        url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'

        with open ("secret.json") as file : 
            secret = json.loads(file.read())

        params = "?" + urlencode({
            quote_plus('serviceKey'): secret["SECRET"],
            quote_plus('returnType'): 'json',
            quote_plus('numOfRows'): '10',
            quote_plus('pageNo'): '1',
            quote_plus('sidoName'): sido,
            quote_plus('ver'): '1.3',
        })

        data = requests.get(url + unquote(params))

        res = data.json()

        text = res['response']['body']['items']

        return text
    
    # api 에서 데이터를 가져오는 과정에서 오류가 발생하면 경고창을 실행 
    except: 
        return (tkinter.messagebox.showerror("Error!", "API 에서 데이터를 가져올 수 없습니다. "))