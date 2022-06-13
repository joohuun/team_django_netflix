# from .models import *
import pandas as pd
import pymysql.cursors

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
cursor = connection.cursor()
sql = "select * from comment;"
cursor.execute(sql)
result = cursor.fetchall()
df = pd.DataFrame(result)

# ratings_matrix = ratings.pivot_table("rate", "userid", "movieid")

print(df)
# def collab_recommender():
#     comment_data = MovieComment.objects.all()
#     comment = pd.DataFrame(comment_data)
#     print(comment)

