import random
from datetime import date

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    random_number = random.randint(1, 10)
    year = date.today().year
    # Rendering HTML Elements
    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    sex = requests.get(f"https://api.genderize.io?name={name}").json()['gender']
    age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    return render_template("guess.html", name=name, sex=sex, age=age)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blogs = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", blogs=blogs, num=int(num))


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
