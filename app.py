import streamlit as st
import pickle
import gzip
import requests
import pandas as pd
import streamlit as st
# print('stream version yeh ha',st.__version__)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# moive_dict=pickle.load(open('movie_dict.pkl','rb'))
# similarity=pickle.load(open('similarity.pkl','rb'))
with gzip.open('movie_dict.pkl.gz', 'rb') as f:
    model_dict = pickle.load(f)
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)
# moive_list=moive_list['title'].values
movies=pd.DataFrame(model_dict)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances=similarity[index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    recommend_list=[]
    recommend_movie_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        # 743b17fad153bacac9c734595edb8093 API KEY
        # fetch movie poster
    #     curl --request GET \
    #  --url 'https://api.themoviedb.org/3/genre/movie/list?language=en' \
    #  --write 'accept: application/json'
        recommend_list.append(movies.iloc[i[0]].title)
        recommend_movie_posters.append(fetch_poster(movie_id))
    return recommend_list , recommend_movie_posters

st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
    'How would you like to be search movie on recommended base system?',
    movies['title'].values
) 

if st.button('Recommend'):
    name,posters=recommend(selected_movie_name)
    
    col1,col2,col3,col4,col5 =  st.columns(5)
    with col1:
         st.write(name[0])
         st.image(posters[0])
    with col2:
         st.write(name[1])
         st.image(posters[1])
    with col3:
         st.write(name[2])
         st.image(posters[2])
    with col4:
         st.write(name[3])
         st.image(posters[3])
    with col5:
         st.write(name[4])
         st.image(posters[4])


        