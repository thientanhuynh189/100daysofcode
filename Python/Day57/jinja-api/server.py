import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/guess/<name>')
def guess(name):
    url_get_1 = f"https://api.agify.io?name={name}"
    data_1 = requests.get(url=url_get_1)
    url_get_2 = f"https://api.genderize.io?name={name}"
    data_2 = requests.get(url=url_get_2)

    data_1.raise_for_status()
    data_2.raise_for_status()

    name_guess = data_1.json()["name"]
    age_guess = data_1.json()["age"]
    gender_guess = data_2.json()["gender"]

    return render_template("index.html", name=name_guess, age=age_guess, gender=gender_guess)

if __name__ == "__main__":
    app.run(debug=True)
