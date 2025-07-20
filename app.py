import streamlit as st
import pickle

# Load data
movies = pickle.load(open("Movie_Recommender/movies_list.pkl", 'rb'))
similarity = pickle.load(open("Movie_Recommender/similarity.pkl", 'rb'))
movie_titles = movies['title'].values

# Recommend movies (without posters)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_titles = []
    for i in distances[1:6]:  # top 5 recommendations
        recommended_titles.append(movies.iloc[i[0]].title)
    return recommended_titles

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🔍 Movie Recommender System (No Posters)")
selected_movie = st.selectbox("🎬 Choose a movie:", movie_titles)

if st.button("Show Recommendations"):
    with st.spinner("Fetching..."):
        recommendations = recommend(selected_movie)
        st.subheader("Recommended Movies:")
        for movie in recommendations:
            st.write("👉", movie)
