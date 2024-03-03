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

#def landingPgRouting():

# def contact():
#     if request.form['submit_button'] == 'try me!':
#         return render_template('tryMe.html')
#     elif request.form['submit_button'] == 'Do Something Else':
#         pass # do something else
#     else:
#         pass # unknown
    
@app.route('/submit_time' , methods=['POST'])
def submit_time():
     years = request.form['number']
     total_time = int(years) * 365
     return render_template("submit_time.html", total_time = total_time)

if __name__ == '__main__':
    app.run()
