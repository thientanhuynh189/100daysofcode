from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    url_1 = f"https://api.agify.io?name={name}"
    data_1 = requests.get(url=url_1)
    url_2 = f"https://api.genderize.io?name={name}"
    data_2 = requests.get(url=url_2)

    name = data_1.json()["name"]
    age = data_1.json()["age"]
    gender = data_2.json()["gender"]

    return render_template("guess.html", name_person=name, gender=gender, age=age)

# Get a number in index.html file
@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/a706c15e51fcc0b8422e"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
