from flask import Flask, render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = "some secret string"


class MyForm(FlaskForm):
    name = StringField(label='email', validators=[DataRequired(),Email("please enter a valid email")])
    password = PasswordField(label='password', validators=[DataRequired(),Length(min=8, message="Length is at least 8 characters!")])
    submit = SubmitField(label='Submit')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form = MyForm()
    form.validate_on_submit()
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)