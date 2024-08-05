import os
import requests
from dotenv import load_dotenv

load_dotenv()
KOBIS_API_KEY = os.getenv('KOBIS_API_KEY')
URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
WEEKLY_URL = f'{URL}?key={KOBIS_API_KEY}&targetDt=20240701'
# print(WEEKLY_URL)

res = requests.get(WEEKLY_URL)
data = res.json()

movie_list = data['boxOfficeResult']['weeklyBoxOfficeList']

movie_dict = {}

for movie in movie_list:
    movie_dict[movie['movieCd']] = {
        '영화명': movie['movieNm'],
        '누적관객수': movie['audiAcc'],
    }

print(movie_dict)