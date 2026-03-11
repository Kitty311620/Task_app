import flask
import random
app = flask.Flask("MyfirstApp")
correctnumber = random.randint(0,100)

# homepage,about
#we use function/methods to make different pages
@app.route("/homepage")
def Homepage():
    return flask.render_template ("Homepage.html")

@app.route("/Aboutme")
def Aboutme():
    return flask.render_template ("Aboutme.html")
@app.route("/Login", methods=["POST", "GET"])
def Login():
    return flask.render_template ("Login.html")
@app.route("/Guess", methods=["POST", "GET"])
def Guess():
    if flask.request.method == "POST":
        print ("Someone pressed the button")
        guessednumber = flask.request.form.get("NO.")
        print(guessednumber)
        if int(guessednumber) < correctnumber:
            return("Too low. Try again")
        if int(guessednumber) > correctnumber:
            return("Too high. Try again")
        if guessednumber == str(correctnumber):
            return("Congratulations! You guessed the correct number!")
    return flask.render_template ("Guess.html")
    
app.run()
