#의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

# from main import draw
from urllib.parse import urlencode, unquote, quote_plus
import requests
import json

def api(sido) : 
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

    # print(data)

    res = data.json()

    # print(res['response']['body']['items'])

    text = res['response']['body']['items']
    # for i in text : 
    #     print (i['stationName'])
    # print(text)
    return text