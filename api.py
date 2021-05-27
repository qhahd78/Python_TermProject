from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import requests
import json

# print('실시간 지하철 위치 조회 서비스')

url ='http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth'


with open ("secret.json") as file : 
    secret = json.loads(file.read())



params = "?" + urlencode({
    quote_plus('serviceKey'): key,
    quote_plus('returnType'): 'json',
    # quote_plus('SERVICE'): 'realtimeStationArrival',
    # quote_plus('START_INDEX'): int(0),
    # quote_plus('END_INDEX'): int(5),
    # quote_plus('statnNm') : station
})

data = requests.get(url + unquote(params))

print(data)

res = data.json()
print(res)