from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/a706c15e51fcc0b8422e")
all_posts = response.json()

@app.route('/')
def home():

    return render_template("index.html", posts=all_posts)

@app.route('/blog/<num>')
def get_post(num):
    return render_template("post.html", num=num, posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
