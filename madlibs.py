"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    rand_num = [1, 2, 3]

    compliments = sample(AWESOMENESS, choice(rand_num))

    if len(compliments) == 3:
        last_compliment = compliments[2]
        other_compliments = compliments[:2]

    if len(compliments) == 2:
        other_compliments = compliments[:1]
        last_compliment = compliments[1]

    if len(compliments) == 1:
        other_compliments = compliments[0]
        last_compliment = ''

    return render_template("compliment.html",
                           person=player,
                           other_compliments=other_compliments, 
                           last_compliment=last_compliment)

@app.route('/game')
def show_madlib_form():

    play_game = request.args.get("game")

    if play_game == "no":
        return render_template('goodbye.html')
    else:
        return render_template('game.html')

@app.route('/madlib', methods=['POST'])
def show_madlib():
    template_list = ['madlib.html', 'madlib2.html']
    person = request.form.get("person")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    thoughts = request.form.getlist("thoughts")
    print(thoughts)
    # if yay:
    #     yay = 'Yay!'
    # else:
    #     yay = ''

    return render_template(choice(template_list), person=person, color=color, 
    noun=noun, adjective=adjective, thoughts=thoughts)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
