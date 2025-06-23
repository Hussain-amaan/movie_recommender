
import pandas as pd
import pickle
import streamlit as st

# Load cleaned data and similarity matrix
@st.cache_data
def load_data():
    df = pd.read_csv("D:/movie_recommender/cleaned_tmdb.csv")
    with open("D:/movie_recommender/similarity_matrix.pkl", "rb") as f:
        similarity_matrix = pickle.load(f)
    return df, similarity_matrix


# Recommender function
def recommend_movies(movie_title, df, similarity_matrix, top_n=5):
    try:
        index = df[df['movie_name'].str.lower() == movie_title.lower()].index[0]
    except IndexError:
        return None

    scores = list(enumerate(similarity_matrix[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in scores[1:top_n+1]]
    return df.iloc[top_indices][['movie_name', 'genre']]


st.title("🎬 Movie Plot Recommender")
st.subheader("Find similar movies based on descriptions using TF-IDF")

df, similarity_matrix = load_data()
movie_list = df['movie_name'].sort_values().unique()
movie_input = st.selectbox("Choose a movie:", movie_list)

if st.button("Find Similar Movies"):
    recommendations = recommend_movies(movie_input, df, similarity_matrix)
    if recommendations is None:
        st.error("❌ Movie not found.")
    else:
        st.success(f"Top 5 movies similar to '{movie_input}':")
        for _, row in recommendations.iterrows():
            st.markdown(f"**🎬 {row['movie_name']}**  \n🏷️ _{row['genre']}_\n")
