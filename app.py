from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')

app = Flask(__name__)

@app.route("/")
@app.route("/<category>")
def home(category="general"):
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=cd868227d8504a03a14af27fe1274c9e"
    r = requests.get(url).json()

    news = r.get("articles", [])
    categories = ["Business", "Entertainment", "General", "Health", "Science", "Sports", "Technology"]   
    
    return render_template('index.html', allNews = news, active_category = category, categories = categories)

if __name__ == '__main__':
    app.run(debug=True)