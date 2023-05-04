#!/usr/bin/env python
# coding: utf-8

# #### 텀프로젝트 최종 보고서 _ 2018100727 이경준

# # 수도권 지하철 이용 승객 수 데이터 분석 

# ###  (1) 주제 선정 이유:
#  서울시 및 경기도에서는 부산, 전라남도 광주와는 다르게 지하철 이용이 활성화 되어있다. 그리고, 강남역, 홍대입구역 등 유동인구가 많은 지역이 주로 서울 지역에 몰려있는데, 경기도와 서울의 지하철 이용자 수는 얼마나 차이가 나며, 서울 내에서도 각각의 지하철역들 사이에 얼마만큼의 차이가 나는지 궁금하여 데이터를 통해 자세히 알아보고자 하였다.

# ### (2) 가설 정의
# 서울에 위치한 지하철역의 이용자 수가 경기도에 위치한 지하철역의 이용자 수보다 더 많을 것이다. 그리고, 서울의 많은 지하철역들 사이에서도 분명히 이용자 수 차이가 존재할 것이다.

# ### (3) 인터넷을 통한 데이터 획득
# 서울시 열린 데이터 광장 웹사이트에서(http://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do) csv 파일 형식으로 월별 지하철 승하차 정보를 제공하고 있다. 이중 나는 10월 한달 동안의 데이터를 나타내는 csv 파일을 다운로드하여 데이터 획득을 하였다. csv 파일 이름은 'CARD_SUBWAY_MONTH_202210' 이다.

# ### (4) 분석을 위한 데이터의 가공
# csv 파일을 살펴보니 사용일자, 노선명, 역명, 승차 총승객, 하차 총승객, 등록일자 순으로 데이터를 나타내었다. 서울 지역에서는 광화문역, 강남역, 홍대 입구역, 명동역의 이용자 수를 알고자 하였으며, 경기도 지역에서는 범계역, 수원역, 영통역, 의왕역의 이용자 수를 알고자 했다. 또한, 승차, 하차 구분 없이 해당 역의 이용자 수를 알고자 하는 것이기 때문에 승차 총승객과 하차 총승객을 더하여 일별 이용자 수를 구하였다. 그렇게 각 지하철역별로 한달간 총 이용자 수를 구하였으며, 월 화 수 목 금 토 일 요일별로도 평균 이용자 수가 어떻게 되는지 알아보았다. <br> 
# 데이터 분석의 세부적인 것을 간단히 이야기 하자면, csv 파일에 있는 데이터를 모두 fileMatrix 의 리스트에 정리하여 넣었으며, 각 역에 해당하는 정보를 다시 또 다른 리스트를 생성하여 넣고 데이터 분석을 했다.<br>
# 그리고, 서울에 위치한 4개의 역 각각의 요일별 평균 이용자 수를 구할 때 2022년 10월 1일이 무슨 요일인지 알아야 했다. 알아본 결과, 2022년 10월 1일은 토요일이었고, 10월 31일은 월요일이었다.

# ### (5) 분석 결과 도출
# <br> 아래는 결과를 print 함수를 통해 간단히 나타낸 것이다.<br>
# <br>Total users who used GwangWhaMoon station for a month are 1936807
# <br>Total users who used GangNam station for a month are 4317062
# <br>Total users who used HongDae station for a month are 1725050
# <br>Total users who used MyeongDong station for a month are 1612883
# <br>Total users who used BeomGye station for a month are 1576408
# <br>Total users who used SuWon station for a month are 1457540
# <br>Total users who used YeongTong station for a month are 522126
# <br>Total users who used UiWang station for a month are 524825
# <br>Gwangwha users of each day: [17051, 23132, 24733, 24844, 25712, 15244, 8491]
# <br>Gangnam users of each day: [39241, 55865, 55647, 56278, 60467, 31288, 17420]
# <br>Hongdae users of each day: [25419, 33369, 10682, 8538, 30416, 7983, 6757]
# <br>Myeongdong users of each day: [13149, 18375, 19293, 19549, 20536, 15208, 10771]


# ### (6) 결론
# 히스토그램을 통해 각 지하철역의 한달 동안 이용한 총 이용자 수를 시각화 하였는데, 강남역이 이용자 수가 가장 많고 의왕역과 영통역의 이용자 수가 가장 적은 쪽에 속한다는 결론을 도출하였다. 이때, 서울에 위치한 지하철역의 이용자 수가 경기도에 위치한 범계역, 수원역보다 훨씬 많을 것으로 예상했는데, 그렇지 않다는 것을 깨달았다. <br>또한, 서울 지하철역에서의 요일별 평균 이용자 수도 그래프를 통해 시각화해 보았는데, 금요일에 대체적으로 이용자수가 가장 많은 것을 확인할 수 있었다. 다만, 홍대입구역의 경우 화요일에 평균 이용자 수가 가장 많았는데, 이는 예외 사례로 생각하려고 한다.<br>

# ### (7) 참고문헌
# matplotlib 이용 - https://wikidocs.net/92071 
# <br> 실습 자료 이용


# ### (8) 직접 개발한 Python 소스코드 원본

# In[1]:


class info:
    def __init__(self):
        self.fileMatrix=[]
    def make_list(self, filename):
        with open(filename,'r',encoding='UTF8') as file:
            for line in file:
                self.fileMatrix.append(line.strip('\n').split(','))
        
filelist=info()
filelist.make_list('CARD_SUBWAY_MONTH_202210.csv')
length=len(filelist.fileMatrix)

Gwangwha=[]
for i in range(length):
    if filelist.fileMatrix[i][2]=='"광화문(세종문화회관)"':
        Gwangwha.append(filelist.fileMatrix[i])
    else:
        continue

Gangnam=[]
for i in range(length):
    if filelist.fileMatrix[i][2]=='"강남"':
        Gangnam.append(filelist.fileMatrix[i])
    else:
        continue
        
Hongdae=[]
for i in range(length):
    if filelist.fileMatrix[i][2]=='"홍대입구"':
        Hongdae.append(filelist.fileMatrix[i])
    else:
        continue
        
Myeongdong=[]
for i in range(length):
    if filelist.fileMatrix[i][2]=='"명동"':
        Myeongdong.append(filelist.fileMatrix[i])
    else:
        continue

Gwangwha_people=0
Gangnam_people=0
Hongdae_people=0
Myeongdong_people=0

def read(station_name,station_users):
    sentence="Total users who used "+station_name+" station for a month are "+str(station_users)
    return sentence

        
for i in range(31):
    Gwangwha_people=Gwangwha_people+int(Gwangwha[i][3].replace('"',''))+int(Gwangwha[i][4].replace('"',''))
    Gangnam_people=Gangnam_people+int(Gangnam[i][3].replace('"',''))+int(Gangnam[i][4].replace('"',''))
    Hongdae_people=Hongdae_people+int(Hongdae[i][3].replace('"',''))+int(Hongdae[i][4].replace('"',''))
    Myeongdong_people=Myeongdong_people+int(Myeongdong[i][3].replace('"',''))+int(Myeongdong[i][4].replace('"',''))

print(read("GwangWhaMoon",Gwangwha_people))
print(read("GangNam",Gangnam_people))
print(read("Hongdae",Hongdae_people))
print(read("Myeongdong",Myeongdong_people))


Beomgye=[]
Suwon=[]
Yeongtong=[]
Uiwang=[]

for i in range(length):
    if filelist.fileMatrix[i][2]=='"범계"':
        Beomgye.append(filelist.fileMatrix[i])
    elif filelist.fileMatrix[i][2]=='"수원"':
        Suwon.append(filelist.fileMatrix[i])
    elif filelist.fileMatrix[i][2]=='"영통"':
        Yeongtong.append(filelist.fileMatrix[i])
    elif filelist.fileMatrix[i][2]=='"의왕"':
        Uiwang.append(filelist.fileMatrix[i])
    else:
        continue

class calculate:
    def __init__(self):
        self.people=0
        self.i=0
        self.monday=0
        self.tuesday=0
        self.wednesday=0
        self.thursday=0
        self.friday=0
        self.saturday=0
        self.sunday=0
    
    def calculate_people(self,list):
        while self.i<31:
            self.people=self.people+int(list[self.i][3].replace('"',''))+int(list[self.i][4].replace('"',''))
            self.i=self.i+1
        return self.people
    
    def calculate_average(self,list):
        for self.i in range(len(list)):
            if self.i in [2,9,16,23,30]:
                self.monday=self.monday+int(list[self.i][3].replace('"',''))+int(list[self.i][4].replace('"',''))
                self.monday=int(self.monday/5)
            elif self.i in [3,10,17,24]:
                self.tuesday=self.tuesday+int(list[self.i][3].replace('"',''))+int(list[self.i][4].replace('"',''))
                self.tuesday=int(self.tuesday/4)
            elif self.i in [4,11,18,25]:
                self.wednesday=self.wednesday+int(list[self.i][3].replace('"',''))+int(list[self.i][4].replace('"',''))
                self.wednesday=int(self.wednesday/4)
            elif self.i in [5,12,19,26]:
                self.thursday=self.thursday+int(list[self.i][3].replace('"',''))+int(list[self.i][4].replace('"',''))
                self.thursday=int(self.thursday/4)
            elif self.i in [6,13,20,27]:
                self.friday=self.friday+int(list[self.i][3].replace('"',''))+int(list[self.i][4].replace('"',''))
                self.friday=int(self.friday/4)
            elif self.i in [0,7,14,21,28]:
                self.saturday=self.saturday+int(list[self.i][3].replace('"',''))+int(list[self.i][4].replace('"',''))
                self.saturday=int(self.saturday/5)
            elif self.i in [1,8,15,22,29]:
                self.sunday=self.sunday+int(list[self.i][3].replace('"',''))+int(list[self.i][4].replace('"',''))
                self.sunday=int(self.sunday/5)
        return [self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday, self.sunday]

    
Beomgye_f=calculate()
Beomgye_people=Beomgye_f.calculate_people(Beomgye)

Suwon_f=calculate()
Suwon_people=Suwon_f.calculate_people(Suwon)

Yeongtong_f=calculate()
Yeongtong_people=Yeongtong_f.calculate_people(Yeongtong)

Uiwang_f=calculate()
Uiwang_people=Uiwang_f.calculate_people(Uiwang)

print("Total users who used BeomGye station for a month are {}"
      .format(Beomgye_people))
print("Total users who used SuWon station for a month are {}"
      .format(Suwon_people))
print("Total users who used YeongTong station for a month are {}"
      .format(Yeongtong_people))
print("Total users who used UiWang station for a month are {}"
      .format(Uiwang_people))

Gwangwha_f=calculate()
Gangnam_f=calculate()
Hongdae_f=calculate()
Myeongdong_f=calculate()

print('Gwangwha users of each day:',Gwangwha_f.calculate_average(Gwangwha))
print('Gangnam users of each day:',Gangnam_f.calculate_average(Gangnam))
print('Hongdae users of each day:',Hongdae_f.calculate_average(Hongdae))
print('Myeongdong users of each day:',Myeongdong_f.calculate_average(Myeongdong))


import csv
with open('new_station_file.csv','w') as write:
    newwrite=csv.writer(write)
    newwrite.writerow(['사용일자', '노선명', '역명', '승차 총승객', '하차 총승객'
                      , '등록일자'])
    for i in range(31):
        newwrite.writerow(Gwangwha[i])
    for i in range(31):
        newwrite.writerow(Gangnam[i])
    for i in range(31):
        newwrite.writerow(Hongdae[i])
    for i in range(31):
        newwrite.writerow(Myeongdong[i])
    for i in range(31):
        newwrite.writerow(Beomgye[i])
    for i in range(31):
        newwrite.writerow(Suwon[i])
    for i in range(31):
        newwrite.writerow(Yeongtong[i])
    for i in range(31):
        newwrite.writerow(Uiwang[i])

        
import matplotlib.pyplot as plt
import numpy as np

day=range(7)
plt.xticks(day,['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
          ,rotation=45)
plt.plot(day, Gwangwha_f.calculate_average(Gwangwha),'o--',label='Gwangwha',color='cyan')
plt.plot(day, Gangnam_f.calculate_average(Gangnam),'o--',label='Gangnam',color='springgreen')
plt.plot(day, Hongdae_f.calculate_average(Hongdae),'o--',label='Hongdae',color='violet')
plt.plot(day, Myeongdong_f.calculate_average(Myeongdong),'o--',label='Myeongdong',color='orange')
plt.xlabel('Day',fontsize=12)
plt.ylabel('Number of People',fontsize=12)
plt.title('Number of People using Subway each day', fontsize=15,fontweight='bold'
         ,pad=20)
plt.legend()
plt.show()

x = np.arange(8)

years = ['Gwangwha', 'Gangnam','Hongdae','Myeongdong','Beomgye','Suwon','Uiwang',
         'Yeongtong']
values = [Gwangwha_people, Gangnam_people, Hongdae_people, Myeongdong_people,
         Beomgye_people, Suwon_people, Uiwang_people, Yeongtong_people]

plt.bar(x, values, width=0.5, color ='green',alpha=0.5)
plt.xticks(x, years, rotation= 45)
plt.xlabel('Station',fontsize=15)
plt.ylabel('Number of people',fontsize=15)
plt.title('Total Users of Each Station', fontsize=20,pad=20,fontweight='bold')

plt.show()


# In[ ]:




