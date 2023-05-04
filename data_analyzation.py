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
