import streamlit as st
import pickle
import pandas as pd
import requests
#import streamlit.components.v1
def fetch_poster(movie_id):
    #https://api.themoviedb.org/3/movie/{}?api_key=c90938ccd0336ff580db036bf5f734c28&language=en-US".format(movie_id)
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c90938ccd0336ff580db036bf5f734c2".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names,recommended_movie_posters

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")
selected_movie_name = st.selectbox('Select a Movie:',movies['title'].values)
if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])