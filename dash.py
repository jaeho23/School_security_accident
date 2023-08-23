import dash
import pandas as pd

# 데이터 불러오기
year = [str(x) for x in range(2020, 2023)]
data = pd.DataFrame()

for i in year:
    df = pd.read_excel("given_data/1. (raw) 사고 발생 데이터.xlsx", sheet_name = i, engine='openpyxl')
    if i == 2020:
        data.columns = df.columns
    data = pd.concat([data, df])

region = {'강원': 14252, '경기': 119448, '경남': 24142, '경북': 15825, '광주': 12000, '대구': 17332, '대전': 11720, '부산': 21099, '서울': 62036, '세종': 5723, '울산': 10665, '인천': 18064, '전남': 9221, '전북': 15111, '제주': 8381, '충남': 15823, '충북': 10983}

print(data['학교급'].value_counts(), data['사고자성별'].value_counts(), data['사고시간'].value_counts(), data['사고장소'].value_counts(), data['사고형태'].value_counts()) # 지역별 사고 수 확인

