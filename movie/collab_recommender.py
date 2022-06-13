
import pandas as pd
import pymysql.cursors
from sklearn.metrics.pairwise import cosine_similarity

from user.models import UserModel

#from user.models import UserModel
from .models import MovieComment, MovieModel

import random

connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='5781',
    db='testdb',
    charset='utf8',
    autocommit=True,
    cursorclass=pymysql.cursors.DictCursor
)


class Collab_recommender:
    def __init__(self):
        # DB comment에 있는 정보 데이터 프레임으로 만들기
        cursor = connection.cursor()
        sql = "select * from comment;"
        cursor.execute(sql)
        result = cursor.fetchall()
        df = pd.DataFrame(result)

        # 유저 평점으로 피벗테이블 만들기
        ratings_matrix = df.pivot_table("user_rate", "user_id", "movie_id")
        ratings_matrix.fillna(0, inplace=True)
        self.ratings_matrix = pd.DataFrame(ratings_matrix)
        print(df)
        print(self.ratings_matrix)

        # 코사인 유사도 구하기
        cosine_sim = cosine_similarity(ratings_matrix, ratings_matrix)
        self.user_based_collab = pd.DataFrame(cosine_sim)
        print(self.user_based_collab)

    def collab_recommend(self, user):
        # 1. 가장 비슷한 1명이 높은 평점을 준 영화 상위 20개 뽑기
        # 1번 유저와 가장 비슷한 유저를 뽑고,
        try:
            similar_user = self.user_based_collab[user -
                                                  1].sort_values(ascending=False)[:3].index[1]
            print(similar_user)
            # 그 유저가 좋아했던 영화를 평점 내림차순으로 출력
            print(self.ratings_matrix)
            index = self.ratings_matrix.iloc[similar_user].sort_values(ascending=False)[
                :20]
            #index = self.ratings_matrix.query(f"user_id == {similar_user}").sort_values(ascending=False, by=user, axis=1)
            print(list(index.index))

            results = []
            for pk in list(index.index):
                result = MovieModel.objects.get(pk=pk)
                results.append(result)
            print(results)
            return results

        except KeyError:
            results = []
            items = list(MovieModel.objects.all())
            # change 3 to how many random items you want
            random_items = random.sample(items, 10)
            print(random_items)
            return random_items


collab = Collab_recommender()
