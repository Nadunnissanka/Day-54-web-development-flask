import random

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h2>Guess A Number Between 0 and 9</h2>' \
           '<img src="https://media0.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif?cid=790b76112c7685879074fd9c21a3f2381f4d71195f9455c1&rid=giphy.gif&ct=g">'


@app.route('/<int:number>')
def check_number(number):
    guess = random.randint(0, 9)

    if number == guess:
        return f'<h2> Guess is correct! ({guess}) </h2>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif number < 0 or number > 9:
        return '<h2> Invalid Input </h2>' \
               f'<img src="https://media0.giphy.com/media/MXywxyJ5UyvtgoF94a/giphy.gif?cid=ecf05e47tkwcg2td3knm2yio0t7v6lc7dvqxsr7651dr7p0x&rid=giphy.gif&ct=g">'
    elif number > guess:
        return f'<h2> {number} is To high </h2>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < guess:
        return f'<h2> {number} is To Low <h2>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
