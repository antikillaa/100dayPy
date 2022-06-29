import random

from flask import Flask

app = Flask(__name__)
guess_int = random.choice(range(0, 9))


@app.route('/')
def start():
    # Rendering HTML Elements
    return '<h1>"Guess a number between 0 and 9"</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


def check_choice(fn):
    def wrapper(guess):
        if guess < guess_int:
            return '<h1>Too low, try again</h1>' \
                    '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
        elif guess > guess_int:
            return '<h1>Too high, try again</h1>' \
                    '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
        else:
            return '<h1>You found me!</h1>' \
                   '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    return wrapper


@app.route('/<int:guess>')
@check_choice
def higher_lower(guess):
    return f"{guess}"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True, host='0.0.0.0', port=5001)
