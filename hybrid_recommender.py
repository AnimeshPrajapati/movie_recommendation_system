from movie_recommender import recommend_movies as content_recommend
from collab_recommender import recommend_for_user

def hybrid_recommendation(user_id, liked_movie, top_n=5):
    try:
        # Get content-based recommendations based on liked movie
        content_recs = content_recommend(liked_movie, num_recommendations=15)
        
        # Get collaborative recommendations for the user
        collab_recs = recommend_for_user(user_id, n=20)

        # Combine both recommendations — find common movies
        hybrid = [movie for movie in content_recs if movie in collab_recs]

        # If no overlap, fallback to content-based
        if not hybrid:
            hybrid = content_recs[:top_n]

        return hybrid[:top_n]
    
    except Exception as e:
        return [f"Error in hybrid recommendation: {str(e)}"]
