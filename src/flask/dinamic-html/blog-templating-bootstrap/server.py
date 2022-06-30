import random
from datetime import date

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    # Rendering HTML Elements
    return render_template("index.html")


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
    app.run(debug=True)
