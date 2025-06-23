
import pandas as pd
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
df = pd.read_csv("D:/movie_recommender/top_movies.csv")
df['genre'] = df['genre'].fillna("Unknown")

# Clean descriptions
def clean_text(text):
    tokens = word_tokenize(str(text).lower())
    tokens = [t for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return ' '.join(tokens)

df['clean_description'] = df['description'].apply(clean_text)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['clean_description'])

# Cosine Similarity
similarity_matrix = cosine_similarity(tfidf_matrix)

# Save outputs
df.to_csv("D:/movie_recommender/cleaned_tmdb.csv", index=False)

with open("D:/movie_recommender/similarity_matrix.pkl", "wb") as f:
    pickle.dump(similarity_matrix, f)



print("✅ Preprocessing complete. Cleaned data and similarity matrix saved.")