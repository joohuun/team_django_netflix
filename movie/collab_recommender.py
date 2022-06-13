
import pandas as pd
import pymysql.cursors
from sklearn.metrics.pairwise import cosine_similarity

from user.models import UserModel

#from user.models import UserModel
from .models import MovieComment, MovieModel

connection = pymysql.connect(
    host='localhost',
    port = 3306,
    user='root',
    password='#won971219',
    db='django_netflix',
    charset = 'utf8',
    autocommit = True,
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
        print(ratings_matrix)

        # 코사인 유사도 구하기
        cosine_sim = cosine_similarity(ratings_matrix, ratings_matrix)
        self.user_based_collab = pd.DataFrame(cosine_sim)
        print(cosine_sim)

    def collab_recommend(self, user):
        # 1. 가장 비슷한 1명이 높은 평점을 준 영화 상위 20개 뽑기
        # 1번 유저와 가장 비슷한 유저를 뽑고,
        if self.user_based_collab[user-1] is not None:
            similar_user = self.user_based_collab[user-1].sort_values(ascending=False)[:3].index[1]
        print(similar_user)
        # 그 유저가 좋아했던 영화를 평점 내림차순으로 출력
        print(self.ratings_matrix)
        index = self.ratings_matrix.iloc[similar_user].sort_values(ascending=False)[:20]
        print(list(index.index))

        # # 2. 비슷한 유저 상위 5명가지고 하기
        # user_index_list = self.user_based_collab[user-1].sort_values(ascending=False)[1:6].index.tolist()
        # user_weight_list = self.user_based_collab[user-1].sort_values(ascending=False)[1:6].tolist()
        # print(user_index_list, user_weight_list)

        # # 상위 5명이 별점을 준 영화 id
        # movies = []
        # for i in range(5):
        #     index = user_index_list[i]
        #     if self.ratings_matrix[i]

        # weighted_sum = []
        # weighted_user = []
        # for movie in list(index.index):
        #     for i in range(5):
        #         # 해당 영화를 보고 평점을 부여한 사람들의 유사도와 평점만 추가 (즉, 0이 아닌 경우에만 계산에 활용)
        #         if int(self.ratings_matrix[movie][user_index_list[i]]) is not 0:
        #             # 평점 * 유사도 추가
        #             weighted_sum.append(self.ratings_matrix[movie][user_index_list[i]] * user_weight_list[i])
        #             # 유사도 추가
        #             weighted_user.append(user_weight_list[i])

        # print(weighted_sum)
        # print(weighted_user)
        # # 총 평점*유사도 / 총 유사도를 토대로 평점 예측
        # print(sum(weighted_sum)/sum(weighted_user))

        results = []
        for pk in list(index.index):
            result = MovieModel.objects.get(pk=pk)
            results.append(result)
        print(results)
        return results


collab = Collab_recommender()










