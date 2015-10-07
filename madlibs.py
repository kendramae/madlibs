from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
# @app.route('/')
# def start_here():
#     return "Hi! This is the home page."

# route to display a simple web page
@app.route('/')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    response = request.args.get("game")

    if response == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():
    noun1 = request.args.get("noun1")
    noun2 = request.args.get("noun2")
    noun3 = request.args.get("noun3")
    plnoun1 = request.args.get("plnoun1")
    plnoun2 = request.args.get("plnoun2")
    plnoun3 = request.args.get("plnoun3")
    adj1 = request.args.get("adj1")
    adj2 = request.args.get("adj2")
    adj3 = request.args.get("adj3")
    verb1 = request.args.get("verb1")
    verb2 = request.args.get("verb2")
    verb3 = request.args.get("verb3")

    return render_template("madlib-shakes.html", noun1=noun1, noun2=noun2,
                            noun3=noun3,
                            plnoun1=plnoun1,
                            plnoun2=plnoun2,
                            plnoun3=plnoun3,
                            adj1=adj1,
                            adj2=adj2,
                            adj3=adj3,
                            verb1=verb1,
                            verb2=verb2,
                            verb3=verb3)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
