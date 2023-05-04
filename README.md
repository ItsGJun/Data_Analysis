# :train2: 공공데이터 분석 및 시각화 :train2:

## 수도권 지하철 이용 승객 수 데이터 분석

###(1) 주제 선정 이유:   
서울시 및 경기도에서는 부산, 전라남도 광주와는 다르게 지하철 이용이 활성화 되어있다. 그리고, 강남역, 홍대입구역 등 유동인구가 많은 지역이 주로 서울 지역에 몰려있는데, 경기도와 서울의 지하철 이용자 수는 얼마나 차이가 나며, 서울 내에서도 각각의 지하철역들 사이에 얼마만큼의 차이가 나는지 궁금하여 데이터를 통해 자세히 알아보고자 하였다.

###(2) 가설 정의   
서울에 위치한 지하철역의 이용자 수가 경기도에 위치한 지하철역의 이용자 수보다 더 많을 것이다. 그리고, 서울의 많은 지하철역들 사이에서도 분명히 이용자 수 차이가 존재할 것이다.

###(3) 인터넷을 통한 데이터 획득   
서울시 열린 데이터 광장 웹사이트에서(http://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do) csv 파일 형식으로 월별 지하철 승하차 정보를 제공하고 있다. 이중 나는 10월 한달 동안의 데이터를 나타내는 csv 파일을 다운로드하여 데이터 획득을 하였다. csv 파일 이름은 'CARD_SUBWAY_MONTH_202210' 이다.

###(4) 분석을 위한 데이터의 가공   
csv 파일을 살펴보니 사용일자, 노선명, 역명, 승차 총승객, 하차 총승객, 등록일자 순으로 데이터를 나타내었다. 서울 지역에서는 광화문역, 강남역, 홍대 입구역, 명동역의 이용자 수를 알고자 하였으며, 경기도 지역에서는 범계역, 수원역, 영통역, 의왕역의 이용자 수를 알고자 했다. 또한, 승차, 하차 구분 없이 해당 역의 이용자 수를 알고자 하는 것이기 때문에 승차 총승객과 하차 총승객을 더하여 일별 이용자 수를 구하였다. 그렇게 각 지하철역별로 한달간 총 이용자 수를 구하였으며, 월 화 수 목 금 토 일 요일별로도 평균 이용자 수가 어떻게 되는지 알아보았다.   
데이터 분석의 세부적인 것을 간단히 이야기 하자면, csv 파일에 있는 데이터를 모두 fileMatrix 의 리스트에 정리하여 넣었으며, 각 역에 해당하는 정보를 다시 또 다른 리스트를 생성하여 넣고 데이터 분석을 했다.    
그리고, 서울에 위치한 4개의 역 각각의 요일별 평균 이용자 수를 구할 때 2022년 10월 1일이 무슨 요일인지 알아야 했다. 알아본 결과, 2022년 10월 1일은 토요일이었고, 10월 31일은 월요일이었다.

###(5) 분석 결과 도출    
아래는 결과를 print 함수를 통해 간단히 나타낸 것이다.   
   
Total users who used GwangWhaMoon station for a month are 1936807   
Total users who used GangNam station for a month are 4317062   
Total users who used HongDae station for a month are 1725050   
Total users who used MyeongDong station for a month are 1612883   
Total users who used BeomGye station for a month are 1576408    
Total users who used SuWon station for a month are 1457540   
Total users who used YeongTong station for a month are 522126   
Total users who used UiWang station for a month are 524825    
Gwangwha users of each day: [17051, 23132, 24733, 24844, 25712, 15244, 8491]   
Gangnam users of each day: [39241, 55865, 55647, 56278, 60467, 31288, 17420]   
Hongdae users of each day: [25419, 33369, 10682, 8538, 30416, 7983, 6757]   
Myeongdong users of each day: [13149, 18375, 19293, 19549, 20536, 15208, 10771]   
