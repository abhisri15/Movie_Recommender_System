import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    full_path = "https://image.tmdb.org/t/p/w500/" + 'poster_path'
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    # to get movie index
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load data
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# Set page configuration
st.set_page_config(page_title="Movie Recommender System", page_icon="🎬", layout="wide")
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f0f0;
    }
    .caption-text {
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Main title and header
st.title('Welcome to Movie Recommender System')
st.header('Find Your Next Favorite Movie!')

# Sidebar with selectbox and button
st.sidebar.title("Movie Recommender System")
selected_movie_name = st.sidebar.selectbox('Which movie would you like to watch?', movies['title'].values)
recommend_button = st.sidebar.button('Recommend')

# Recommendation results
# ...

# Recommendation results
if recommend_button:
    names, posters = recommend(selected_movie_name)
    st.subheader('Recommended Movies:')
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.image(posters[0], use_column_width=True)
    col1.markdown(f"<p class='caption-text'>{names[0]}</p>", unsafe_allow_html=True)

    col2.image(posters[1], use_column_width=True)
    col2.markdown(f"<p class='caption-text'>{names[1]}</p>", unsafe_allow_html=True)

    col3.image(posters[2], use_column_width=True)
    col3.markdown(f"<p class='caption-text'>{names[2]}</p>", unsafe_allow_html=True)

    col4.image(posters[3], use_column_width=True)
    col4.markdown(f"<p class='caption-text'>{names[3]}</p>", unsafe_allow_html=True)

    col5.image(posters[4], use_column_width=True)
    col5.markdown(f"<p class='caption-text'>{names[4]}</p>", unsafe_allow_html=True)





# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#     data = response.json()
#     full_path = "https://image.tmdb.org/t/p/w500/" + 'poster_path'
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#
# def recommend(movie):
#     # to get movie index
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_posters = []
#
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         # fetch poster from API
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies,  recommended_movies_posters
#
# movies_dict = pickle.load(open('movies_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open('similarity.pkl','rb'))
#
# st.header('Movie Recommender System')
#
# selected_movie_name = st.selectbox(
#     'Which movie would you like to watch?',
#     movies['title'].values)
#
# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])