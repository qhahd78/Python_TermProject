#의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

# 1. api 실행하는 파일 
# 2. tk 만드는 파일
# 3. 장소를 선택하면 그 장소에 맞는 출력 값을 가져온다. 
# 4. 장소를 선택 => 선택 값을 api 파일로 보내줌 => 그 장소 값에 맞는 결과를 호출 => 다시 tk 로 보내줌 => tk 에서 결과 출력 

from tkinter import * 
# 모듈 불러오기 
from apitest import api

site = Tk()
site.title("시도별 대기상태 정보 조회 서비스")

place = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']
selected = StringVar()
selected.set(None)

# api 로 선택된 지역을 보내주는 함수. 
def send() : 
    # 선택된 지역을 placeS 라는 변수에 담아 api 함수로 보내준다. 
    placeS = selected.get()
    result = api(placeS)
    
    return change(result)

def change(result) :
    print(result)
    for i in result : 
        print(result)
        # Label(site, text = str(i['stationName'])).grid(row=0, column=i)
        i = i+1
        dong = (i['stationName'])
        time = ("측정일시: "+ i['dataTime'])
        mise = ("미세먼지 농도: " + i['pm10Value'])
        Ozone = ("오존 지수: " + str(i['o3Grade']))
    

OptionMenu(site, selected, *place).grid(row=0, column=0)
# Label(site, text="결과값", width=20).grid(row=0, column=0)

# 버튼을 클릭할시 선택된 지역의 값을 api 함수로 전달하여 그에 맞는 데이터를 출력 
Button(site, text="출력", command = send).grid(row=1, column=1)

site.mainloop()