# 🎬 TMDB Movie Recommender App


A content-based movie recommendation system built with **NLP (TF-IDF + Cosine Similarity)** and deployed using **Streamlit**.  
It suggests movies similar in plot and genre using the TMDB movie dataset.

---

## 🧠 Features

- Cleaned movie plot descriptions using **NLTK**
- Generated movie similarity using **TF-IDF vectorization**
- Recommended top 5 similar movies based on description
- Simple and interactive **Streamlit UI**
- Fully deployable and extendable

---



## 🗂️ Project Structure

movie_recommender/

├── app.py # Streamlit app

├── precompute.py # One-time preprocessing script

├── top_movies.csv # Raw dataset

├── cleaned_tmdb.csv # Cleaned dataset (generated)

├── similarity_matrix.pkl # Pickled similarity matrix (generated)

├── requirements.txt

├── .gitignore

└── README.md


---

## 📊 How It Works

### 🔹 1. Preprocessing
- Tokenization & stopword removal via **NLTK**
- TF-IDF vectorization using **scikit-learn**
- Cosine similarity matrix computed and cached

### 🔹 2. Recommendation Logic
- User selects a movie
- App finds its index and recommends top N most similar movies

### 🔹 3. Streamlit UI
- Clean dropdown menu for movie selection
- Shows recommended titles and genres

---

## 🧪 Example

Select: **The Godfather**

Recommendations might be:
```

* The Godfather Part II
* Goodfellas
* Casino
* Scarface
* Donnie Brasco

````

---

## ⚙️ Setup Locally

### 1. Clone the Repo

```bash
git clone https://github.com/Hussain-amaan/movie_recommender.git
cd movie_recommender
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run Preprocessing (once)

```bash
python scripts/precompute.py
```

### 4. Launch Streamlit App

```bash
streamlit run app/app.py
```

---

## ✅ Dependencies

* `pandas`
* `nltk`
* `scikit-learn`
* `streamlit`

---

## 🛰️ Deploy on Streamlit Cloud

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Connect your GitHub repo
3. Set:

   * **Main file path**: `app/app.py`
   * **Branch**: `main`
4. Click **Deploy**

---

## 📌 To-Do

* [ ] Add search functionality
* [ ] Add poster image display using TMDB API
* [ ] Add filters by genre, language, etc.
* [ ] Evaluate with other vectorization methods (e.g., Word2Vec)

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Hussain Amaan**
📧 [hussainaman347@gmail.com](mailto:hussainaman347@gmail.com)
💼 [GitHub Profile](https://github.com/Hussain-amaan)

---


