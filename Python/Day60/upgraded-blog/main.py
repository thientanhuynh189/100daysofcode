from flask import Flask, render_template, request
import requests
import smtplib

OWN_EMAIL = ""
OWN_PASSWORD = ""
app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/a706c15e51fcc0b8422e")
all_posts = response.json()


@app.route('/')
def get_all_post():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/contact')
def get_contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['id']
        phone = request.form['phone']
        message = request.form['message']
        print(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
