# install flask with `pip install flask`
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# creating an app instance

# use a decorator @ to define the route for our web page
@app.route("/")
# setting up a default page
def index():
    return "Welcome to DevOps team"

@app.route("/welcome/")
def welcome():
    return f"Welcome on board"

@app.route("/home/")
def home():
    return render_template("index.html")


# create 2 more pages/ routes and add the functionality for email and password
# implement OOP inheritance

users = []
users.append({"user_id": 1, "email": "James@gmail.com", "password": "Bond"})
@app.route("/base/", methods = ["GET", "POST"])
def base():
    if request.method == "POST":
        print("POST")
        email = request.form['exampleInputEmail1']
        password = request.form['exampleInputPassword1']
        print(users)
        print(email)
        print(password)
        return render_template("login.html")

    return render_template("base.html")

@app.route("/login/")
def login():

    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)
