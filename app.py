from flask import Flask, render_template, request
from hybrid_recommender import hybrid_recommendation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        try:
            user_id = int(request.form['user_id'])
            movie_name = request.form['movie']
            recommendations = hybrid_recommendation(user_id, movie_name)
        except Exception as e:
            recommendations = [f"Error: {str(e)}"]
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
