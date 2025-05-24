# 🎬 Movie Recommendation System

This project is a **Hybrid Movie Recommendation System** built using **Flask**, which combines **content-based** and **collaborative filtering** techniques to suggest personalized movies based on user preferences.

## 📌 Features
- Content-based filtering using movie overviews and TF-IDF
- Collaborative filtering using SVD (Surprise library)
- Hybrid recommendation: combines both methods
- Simple Flask web interface for user interaction

## 📁 Project Structure
movie-recommender/
├── app.py # Flask app
├── movie_recommender.py # Content-based recommender
├── collab_recommender.py # Collaborative recommender
├── hybrid_recommender.py # Hybrid logic
├── data/
│ ├── movies.csv # Movie metadata
│ └── ratings.csv # User ratings
├── templates/
│ └── index.html # Web interface
├── requirements.txt # Python dependencies
└── README.md

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app

bash
Copy
Edit
python app.py
Visit in browser

cpp
Copy
Edit
http://127.0.0.1:5000
🧪 Sample Input
User ID: 1

Liked Movie: Toy Story (1995)

🛠 Technologies Used
Python

Flask

Pandas, Scikit-learn, Surprise

HTML, CSS (basic styling
