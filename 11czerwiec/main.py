from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h1> Witam </h1>"

@app.route("/html/<x>")
def html(x):
    return render_template("index.html", value= x)

@app.route("login")
def login():
    return render_template("login.html")





if __name__ == "__main__":
    app.run(debug=True)