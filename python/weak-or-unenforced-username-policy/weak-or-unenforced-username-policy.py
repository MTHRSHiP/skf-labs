# import re
from flask import Flask, render_template, request, url_for, redirect, session
from json import dumps


from db.db import seed_db
from db.users import get_user_by_id, get_user, create_user


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
app.secret_key = 'mysecret'


seed_db()


@app.route("/")
def home():
    username = None

    if "id" in session:
        user = get_user_by_id(session['id'])
        if user is None:
            session.clear()
            redirect(url_for('home'))

    if "username" in session:
        username = session['username']

    return render_template("index.html", user=username)


@app.route("/register/", methods=['GET', 'POST'])
def register_route():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        username = request.get_json()['username']
        password = request.get_json()['password']
        # user = get_user_by_username(username)
        # if user:
        #     error = "User already exists"
        #     return dumps({"error": error}, default=str), 403
        # else:
        create_user(username, password)
        return dumps({"message": "User created"}, default=str)


@app.route("/login/", methods=['GET', 'POST'])
def login_route():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.get_json()['username']
        password = request.get_json()['password']
        user = get_user(username, password)
        if user:
            session['id'] = user["id"]
            session['username'] = user["username"]
            return dumps({"message": "User logged in"}, default=str)
        else:
            error = "Invalid username or password"
            return dumps({"error": error}, default=str), 401


@app.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', use_reloader=False)
