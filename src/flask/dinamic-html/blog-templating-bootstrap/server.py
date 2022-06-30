import os

import requests
from flask import Flask, render_template

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route('/')
def main():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    # Rendering HTML Elements
    post = posts[post_id-1]
    return render_template("post.html", post=post, post_id=post_id)


@app.route('/about')
def get_about():
    # Rendering HTML Elements
    return render_template("about.html")


@app.route('/contact')
def get_contact():
    # Rendering HTML Elements
    return render_template("contact.html")


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
