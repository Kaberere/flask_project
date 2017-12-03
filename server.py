from flask import Flask, escape, render_template, session, redirect, request, url_for
import random


app = Flask(__name__)


# @app.route('/')
# def index():
#     # Returns a HTTP response with this string as a body.
#     return 'Hello, Beautiful!'


# @app.route('/number_please')
# def number_please():
#     return "{}".format(random.randint(1, 20))


# @app.route('/<name>')
# def compliment_Eve(name):
#     return 'Hello, beautiful {}!'.format(name)


# @app.route('/compliment/<name>/<int:number>')
# def compliment_Eve(name, number):
#     return render_template("hello.html", name=name, number=number)


@app.route('/welcome/<name>')
def welcome(name):
    if not 'is_Eve' in session:
        session['is_Eve'] = name.title() == "Eve"
    return render_template("welcome.html", is_Eve=session['is_Eve'])


@app.route('/secret/<password>')
def secret(password):
    if 'is_signed_in' in session:
        return render_template("secrets.html", password=password)


@app.route('/session')
def verify():
    if 'is_signed_in' in session:
        return "You have signed in"
    return redirect("https://www.yahoo.com")


@app.route('/login', methods=['GET', 'POST'])
def get_login():
    if request.method == 'POST':
        password = request.form.get("password")
        if not 'is_signed_in' in session:
            session['is_signed_in'] = password == "bananaPie"
        return redirect(url_for("secret", password=password))
    return render_template("login.html")


@app.route('/success')
def success():
    secret = "Bazinga"
    # if 'is_signed_in' in session:
    return render_template("success.html", secret=secret)


@app.route('/table/<int:row>/<int:column>')
def show_table(row, column):
    return render_template("table.html", row=row, column=column)


@app.route('/logout')
def logout():
    session.clear()
    return "You have successfully logged out"


app.secret_key = b'\xee\xfe\xea\xa5RI\xd7\xd2Q(\x92C\x88\xcc\x08\x9d\xd53\xd4\x1a\x03\x8a\xc4\xfc'
