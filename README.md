# 🎬 Modified Movie Recommendation System  

## 📌 Overview  
The **Modified Movie Recommendation System** suggests movies to users based on content similarity.  
It combines two approaches:  

- **Bag of Words (BoW):** Uses CountVectorizer + cosine similarity to recommend movies with similar keywords, cast, crew, and genres.  
- **BERT Embeddings:** Uses `all-MiniLM-L6-v2` (Sentence Transformers) to capture semantic meaning in text, providing context-aware recommendations.  

BERT serves as the **primary recommendation engine**, with BoW acting as a **fallback mechanism**.  
A **Streamlit web app** provides an interactive interface where users can select a movie and view the top 5 recommendations along with their posters (fetched via TMDB API).  

## 📂 Project Structure  
Modified Movie Recommender System/
│── Modified Movie Recommender System.ipynb # Jupyter Notebook (data preprocessing, BoW & BERT models)
│── main.py # Streamlit frontend
│── tmdb_5000_movies.csv # Dataset (movies metadata)
│── tmdb_5000_credits.csv # Dataset (credits metadata)
│── movies.pkl # Processed movies dataframe
│── similarity.pkl # Cosine similarity (BoW)
│── similarity_bert.pkl # Cosine similarity (BERT)
│── requirements.txt # Dependencies for deployment
│── README.md # Project documentation

## ⚙️ System Requirements  
- **OS:** Windows, macOS, or Linux  
- **RAM:** 8 GB recommended (BERT embeddings are memory-heavy)  
- **Python:** Version 3.8+  
- **Processor:** Intel i5 or higher  

## 📦 Installation  

1. **Clone the repository**  
```bash```
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

2. **⚙️Create Virtual Environment(Recommended)**
```bash```
conda create -n recommender python=3.9
conda activate recommender

## 📦 Install Dependencies
```bash```
pip install -r requirements.txt

## ▶️ Running the Project
### Option 1: Run Notebook
Open `Modified Movie Recommender System.ipynb` in Jupyter Notebook.

Run all cells to:
- Preprocess dataset
- Generate BoW and BERT similarities
- Save pickle files

### Option 2: Run Streamlit App
Make sure pickle files (`movies.pkl`, `similarity.pkl`, `similarity_bert.pkl`) are present.

Run the app:
```bash```
streamlit run main.py

Open browser at: http://localhost:8501

## 🌐 Deployment on Render
Push the project to GitHub.

Create a new Web Service in Render.

Configure:

Build Command:
```bash```
pip install -r requirements.txt

Start Command:
```bash```
streamlit run main.py --server.port $PORT --server.address 0.0.0.0

Deploy and get a live URL to share your app.

## 📊 Features
- Content-based recommendation (BoW + BERT)
- Movie poster fetching using TMDB API
- WordCloud of frequently used words
- Genre distribution (bar + pie chart)
- Histogram of similarity scores for recommendations
- Interactive web app (Streamlit)

## ✅ Best Practices
- Run Jupyter Notebook first if pickle files are missing
- Cache embeddings to avoid recomputation
- Use GPU for faster BERT embeddings (optional)

## 👩‍💻 Author
Developed by Divanshika as part of a Machine Learning project.

