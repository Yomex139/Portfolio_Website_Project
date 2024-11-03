from flask import Flask, render_template

app = Flask(__name__)


# Home page
@app.route('/')
def home():
    return render_template("index.html")


# About page
@app.route('/about')
def about():
    return render_template("about.html")


# Projects page
@app.route('/project')
def projects():
    return render_template("project.html")


if __name__ == "__main__":
    app.run(debug=True)