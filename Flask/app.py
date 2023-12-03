import random
import requests
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
   name = '민지'
   lotto = [4, 9, 17, 27, 39, 43]
   
   def generate_lotto_numbers():
        numbers = random.sample(range(1, 46), 6)
        return sorted(numbers)
   random_lotto = generate_lotto_numbers()

   def count_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return len(common_elements)
   # 예시 리스트
   list1 = [1, 2, 3, 4, 9]
   list2 = [4, 5, 6, 7, 8]
   common_count = count_common_elements(list1, list2)
   print("두 리스트에서 공통된 요소의 개수:", common_count)
   
   context = {
      "name": name,
      "lotto": lotto,
      "random_lotto": random_lotto,
      "common_count": common_count
   }
   return render_template('index.html', data = context)

@app.route('/mypage')
def mypage():  
   return 'This is My Page!'

@app.route('/movie')
def movie():
   query = request.args.get('query')
   res = requests.get(
      f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}")
   rjson = res.json()
   movie_list = rjson["movieListResult"]["movieList"]
   return render_template('movie.html', data = movie_list)

@app.route('/answer')
def answer():
   if request.args.get('query'):
      query = request.args.get('query')
   else:
      query = '20230601'
   res = requests.get(
      f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={query}")
   rjson = res.json()
   movie_list = rjson["boxOfficeResult"]["weeklyBoxOfficeList"]
   print(movie_list)
   return render_template('answer.html', data = movie_list)

if __name__ == '__main__':  
   app.run(debug=True)