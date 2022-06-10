import pathlib
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
from .models import *

class ContentsRecommender:
    def __init__(self):
        start = time.time()
        moviedata = pd.read_csv("resultdata0609.csv")

        # 벡터화
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1,1), min_df = 1)
        tfidf_matrix = tf.fit_transform(moviedata['combined'].values.astype('U'))

        # 코사인 유사도 구하기
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        self.content_based_filtering = pd.DataFrame(cosine_sim)
        
        # index = moviedata.reset_index()
        # title = moviedata['title']
        # self.title_num = pd.Series(index.index, index=index)
        end = time.time()
        print(f"{end-start:.5f}sec")

    def content_based(self, movie_pk):
        # 받은 pk값으로 유사도 비슷한 것 인덱스(pk) 구하기
        index = self.content_based_filtering[movie_pk].sort_values(ascending = False)[1:11].index
        # 인덱스 값 DB에서 pk와 같은 것 찾기
        results = []
        for pk in list(index):
            result = MovieModel.objects.get(pk=pk)
            results.append(result)
        print(results)
        return results

similarmovies = ContentsRecommender()








