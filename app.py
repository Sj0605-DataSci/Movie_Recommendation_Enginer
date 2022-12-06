import streamlit as st
import pickle
import pandas as pd
import requests
import bz2

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3a16da99b9773e318613f2811d9fe79b&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w300/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = simi[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key = lambda x:x[1])[1:6]
    recommend_movies=[]
    posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return recommend_movies,posters

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
simi = pickle.load(open('simi.pkl','rb'))

def set_bg_hack_url():

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://149695847.v2.pressablecdn.com/wp-content/uploads/2019/04/ntflxx.png");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

set_bg_hack_url() 

st.title("Movie Recommendation Engine")
selected_movie_name = st.selectbox('How would you like to be connected?',movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3 ,col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
