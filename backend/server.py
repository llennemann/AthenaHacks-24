import time
from flask import Flask, request, render_template

app = Flask(__name__)
total_time = 0 #in days

@app.route('/')
def home():
    return render_template("landingPage.html")

@app.route('/tryMe')
def tryMe():
    return render_template("tryMe.html")

@app.route('/aboutMe')
def aboutMe():
    return render_template("aboutMe.html")
    
@app.route('/buy' , methods=['POST'])
def buy():
     years = request.form['number']
     total_time = int(years) * 365
     return render_template("buy.html", total_time = total_time)
@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run()
