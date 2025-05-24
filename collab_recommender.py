import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

# Load ratings data
ratings = pd.read_csv('data/ratings.csv')  # Ensure this file exists

# Define the format: userId, itemId, rating
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Train SVD model
trainset, _ = train_test_split(data, test_size=0.2, random_state=42)
model = SVD()
model.fit(trainset)

# Load movie metadata to map movieId to title
movies = pd.read_csv('data/movies.csv')
movie_id_to_title = pd.Series(movies.title.values, index=movies.movieId).to_dict()

def recommend_for_user(user_id, n=10):
    # Get list of all movie IDs
    all_movie_ids = movies['movieId'].unique()

    # Get movies user has already rated
    rated_movies = ratings[ratings['userId'] == user_id]['movieId'].values

    # Predict ratings for all unseen movies
    predictions = []
    for movie_id in all_movie_ids:
        if movie_id not in rated_movies:
            pred = model.predict(user_id, movie_id)
            predictions.append((movie_id, pred.est))

    # Sort predictions by estimated rating
    predictions.sort(key=lambda x: x[1], reverse=True)

    # Get top n movie titles
    top_movie_ids = [movie_id for movie_id, _ in predictions[:n]]
    recommended_titles = [movie_id_to_title.get(mid, "Unknown") for mid in top_movie_ids]

    return recommended_titles
