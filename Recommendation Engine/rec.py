import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

rating=pd.read_csv("ratings.csv")
movie=pd.read_csv("movies.csv")
ratings=pd.merge(rating,movie).drop(['genres','timestamp'],axis=1)

user_rating=ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
user_rating=user_rating.dropna(thresh=10,axis=1).fillna(0)

item_similarity=user_rating.corr(method='pearson')
def get_similar_movies(movie_name,user_rating):
    similar_score=item_similarity[movie_name]*(user_rating-2.5)
    similar_score=similar_score.sort_values(ascending=False)
    return similar_score

similar_movies=pd.DataFrame()
        for movie,rating in action_lover:
            similar_movies=similar_movies.append(get_similar_movies(movie,rating),ignore_index=True)
        print(similar_movies.sum().sort_values(ascending=False).head())
    
# similar_movies.head(10)
   