import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    blogs = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", blogs=blogs)


@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    blogs = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("post.html", blogs=blogs, blog_id=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
