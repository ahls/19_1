from flask import Flask

app = Flask(__name__)
@app.route('/welcome')
def welcomePage():
    return "welcome"

    
@app.route('/welcome/home')
def welcomeHomepage():
    return "welcome home"

    
@app.route('/welcome/back')
def welcomeBackPage():
    return "welcome back"

    