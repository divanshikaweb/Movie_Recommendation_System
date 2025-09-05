import streamlit as st
import pickle
import pandas as pd
import requests

# ------------------- CSS for labels ------------------- #
st.markdown(
    """
    <style>
    div[data-baseweb="input"] > label {
        color: black !important;
        font-size: 18px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #4B0082;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------- Session State ------------------- #
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# ------------------- App Header ------------------- #
st.markdown("""
    <h1 style='text-align: center; color: #4B0082;'>🎬 Movie Recommender 🎬</h1>
    <h5><p style='text-align: center; color: #4B0082;'>Please enter your login details to continue</p></h5>
""", unsafe_allow_html=True)

# ------------------- Login Form ------------------- #
credentials = {"divanshika": "1234", "ongc": "5678"}

if not st.session_state.logged_in:
    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")
    login_btn = st.button("💜 Login")

    if login_btn:
        if username in credentials and credentials[username] == password:
            st.session_state.logged_in = True
            st.success(f"Welcome {username}!")
        else:
            st.error("❌ Invalid username or password")
# ------------------- Recommendation Section ------------------- #
if st.session_state.logged_in:

    # ---------------- Poster Fetch Function (Unchanged) ---------------- #
    def fetch_poster(movie_id):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=57280b45bc97554a2dafb9e602eda50b&language=en-US"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            print("API response for", movie_id, ":", data)  # debug print
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                return "https://via.placeholder.com/500x750?text=No+Poster"
        except requests.exceptions.RequestException as e:
            print(f"Error fetching poster for movie_id={movie_id}: {e}")
            return "https://via.placeholder.com/500x750?text=Error"


    # ---------------- Load Data ---------------- #
    movies_dict = pickle.load(open('movies.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(open('similarity.pkl', 'rb'))          # BOW similarity
    similarity_bert = pickle.load(open('similarity_bert.pkl', 'rb'))  # BERT similarity


    # ---------------- Recommendation (BOW) ---------------- #
    def recommend_bow(movie):
        if movie not in movies['title'].values:
            return [], []
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommend_movies, recommended_movies_poster = [], []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommend_movies.append(movies.iloc[i[0]].title)
            recommended_movies_poster.append(fetch_poster(movie_id))

        return recommend_movies, recommended_movies_poster


    # ---------------- Recommendation (BERT) ---------------- #
    def recommend_bert(movie):
        if movie not in movies['title'].values:
            return [], []
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity_bert[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommend_movies, recommended_movies_poster = [], []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommend_movies.append(movies.iloc[i[0]].title)
            recommended_movies_poster.append(fetch_poster(movie_id))

        return recommend_movies, recommended_movies_poster


    # ---------------- Streamlit UI ---------------- #

    selected_movie_name = st.selectbox(
        "Choose a movie to get recommendations:",
        movies['title'].values
    )

    if st.button('Show Recommendation'):
        # Try BERT first, fallback to BOW
        recommended_movie_names, recommended_movie_posters = recommend_bert(selected_movie_name)
        if not recommended_movie_names:  # fallback
            recommended_movie_names, recommended_movie_posters = recommend_bow(selected_movie_name)

        # Display recommendations
        if recommended_movie_names:
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
