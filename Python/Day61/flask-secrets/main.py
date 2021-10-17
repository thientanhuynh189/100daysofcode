from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
import re


def validate_email(form, field):
    if not re.search(r"[^@]+@[^@]+\.[^@]+", field.data):
        raise ValidationError("Invalid email address.")


def validate_password(form, field):
    if len(field.data) < 8:
        raise ValidationError("Field must be at least 8 characters long.")


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), validate_email])
    password = PasswordField(label='Password', validators=[DataRequired(), validate_password])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = b'\xb2lF\xf6\xfd\xa9\xca\x85\r"\xfd84\xa8\xda\x85'
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
