#의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

# 1. api 실행하는 파일 
# 2. tk 만드는 파일
# 3. 장소를 선택하면 그 장소에 맞는 출력 값을 가져온다. 
# 4. 장소를 선택 => 선택 값을 api 파일로 보내줌 => 그 장소 값에 맞는 결과를 호출 => 다시 tk 로 보내줌 => tk 에서 결과 출력 

from tkinter import *
import tkinter.font as tkFont 
import tkinter.messagebox
# api 모듈 불러오기 
from api import api

site = Tk()
site.geometry('900x320+200+200')
site.title("시도별 대기상태 정보 조회 서비스")

# 지역 옵션 리스트 정의 
place = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']

# 옵션에서 선택된 값 정의 
selected = StringVar()

# api 로 선택된 지역을 보내주는 함수. 
def send() : 
    # 선택된 지역을 placeS 에 저장
    placeS = selected.get()

    # api 함수로 선택된 지역을 인자(placeS)로 보내주고, 결과값을 result 에 저장 
    result = api(placeS)
    
    # send 함수는 change 함수를 리턴, result 값을 인자로 담아 dataset 에 보내준다. 
    return dataset(result)

# api로부터 받은 결과 값을 gui 로 출력해주는 함수 . 
def dataset(result) :
    
    # j 는 한 줄에 지역 하나씩 출력하기 위한 변수값
    # row 3번째 줄부터 출력이 될 것이기 때문에 초기값을 3으로 세팅했음. 
    j = 3

    ##### 데이터셋 설명 #####
    # result 값은 리스트 형태로, 한 지역이 리스트 안에 딕셔너리 형태로 나오기 때문에 for 문을 돌면서 
    # 리스트에서 지역 하나(i)를 선택하고, key 값으로 지역명, 측정시간, 미세먼지 농도, 오존 농도를 조회하여
    # Label 로 key 값에 따른 value 값을 gui로 출력해준다. 
    for i in result : 
        
        # 어떤 데이터인지 설명할 label. 
        Label(site, text = "지역명", bg='yellow', width='20').grid(row=2, column=0)
        Label(site, text = "측정날짜",bg='yellow', width='20').grid(row=2, column=1)
        Label(site, text = "미세먼지 농도",bg='yellow', width='20').grid(row=2, column=2)
        Label(site, text = "미세먼지 등급",bg='yellow', width='20').grid(row=2, column=3)
        Label(site, text = "오존 농도",bg='yellow', width='20').grid(row=2, column=4)
        Label(site, text = "오존 등급",bg='yellow', width='20').grid(row=2, column=5)

        # 데이터 값 : 지역명
        Label(site, text = str(i['stationName']), width='20').grid(row=j, column=0)

        # 데이터 값 : 측정 날짜와 시간
        Label(site, text = str(i['dataTime']), width='20').grid(row=j, column=1)

        # 데이터 값 : 오존 수치 
        Label(site, text = str(i['o3Value'])+ " ppm", width='20').grid(row=j, column=4)

        # 데이터 값 : 미세먼지 수치 
        Label(site, text = str(i['pm10Value'])+" ㎍/㎥", width='20').grid(row=j, column=2)

        # 데이터 값 : 미세먼지 등급 
        # 미세먼지 등급 별로 매우 좋음 ~ 매우 나쁨까지 출력. 
        # 데이터가 없는 경우 에러가 발생하기 때문에 try except 처리
        # 데이터가 없어 등급을 매길 수 없으므로 데이터 값 (none 이나 -)을 등급란에도 그대로 출력
        try : 
            if int(i['pm10Grade']) == 1:
                Label(site, text = str(i['pm10Grade'])+ " 매우 좋음", width='20', fg='blue').grid(row=j, column=3)
            elif int(i['pm10Grade']) == 2:
                Label(site, text = str(i['pm10Grade'])+ " 보통", width='20').grid(row=j, column=3)
            elif int(i['pm10Grade']) == 3:
                Label(site, text = str(i['pm10Grade'])+ " 나쁨", width='20', fg='pink').grid(row=j, column=3)
            elif int(i['pm10Grade']) == 4:
                Label(site, text = str(i['pm10Grade'])+ " 매우 나쁨", width='20', fg='red').grid(row=j, column=3)
            else : 
                Label(site, text = str(i['pm10Value']), width='20').grid(row=j, column=3)
        except : 
            Label(site, text = str(i['pm10Value']), width='20').grid(row=j, column=3)

        # 데이터 값 : 오존 등급
        # 오존 등급 별로 매우 좋음 ~ 매우 나쁨까지 출력. 
        # 데이터가 없는 경우 에러가 발생하기 때문에 try except 처리
        # 데이터가 없어 등급을 매길 수 없으므로 데이터 값 (none 이나 -)을 등급란에도 그대로 출력
        try: 
            if int(i['o3Grade']) == 1:
                Label(site, text = str(i['o3Grade'])+ " 매우 좋음", width='20', fg='blue').grid(row=j, column=5)
            elif int(i['o3Grade']) == 2:
                Label(site, text = str(i['o3Grade'])+ " 보통", width='20').grid(row=j, column=5)
            elif int(i['o3Grade']) == 3:
                Label(site, text = str(i['o3Grade'])+ " 나쁨", width='20', fg='pink').grid(row=j, column=5)
            elif int(i['o3Grade']) == 4:
                Label(site, text = str(i['o3Grade'])+ " 매우 나쁨", width='20', fg='red').grid(row=j, column=5)
            else : 
                Label(site, text = str(i['o3Value']), width='20').grid(row=j, column=5)
        except: 
            Label(site, text = str(i['o3Value']), width='20').grid(row=j, column=5)
        
        # for 문을 돌 때마다 j 를 1씩 증가시켜줌으로써 한 줄에 하나의 지역을 출력해준다. 
        j = j+1 
        
# 창을 닫으려 할 경우 아래의 함수 실행 
def close():
    # 경고창을 띄운다. 
    if tkinter.messagebox.askokcancel("종료", "이 프로그램을 종료하시겠습니까?"):
        # 예 를 누를 경우 프로그램 종료 
        site.destroy()

# 안내문의 폰트 크기를 더 크게 
fontStyle = tkFont.Font(size=12)

# 안내문 띄우기     
Label(site, text = "각 지역의 대기 상태를 확인해보세요.", font=fontStyle).grid(row=0, columnspan=6)

# 선택 받을 지역을 optionmenu 로 띄우기. 선택 받은 값은 selected 변수에 저장 
OptionMenu(site, selected, *place).grid(row=1, columnspan=6)

# 버튼을 클릭할시 선택된 지역의 값을 api 함수로 전달하는 send 함수 실행 및 데이터를 출력 
Button(site, text="결과보기", command = send, width='40', bg='#e4e4e4').grid(row=13, columnspan=6)

# 창을 닫을 경우 한 번 더 경고문 출력하도록 하는 프로토콜 (close 함수 실행 )
site.protocol("WM_DELETE_WINDOW", close)
site.mainloop()