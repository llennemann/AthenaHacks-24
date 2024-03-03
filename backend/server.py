import time
from flask import Flask, request, render_template
from data_generator import all_data

curr_day = 0

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
    
def getTableData(currentDay):
    industries, stocks = all_data()
    table = {} # result dictionary
    for key in stocks.keys():
        table[key] = [industries.get(key), stocks.get(key)[currentDay]]

    return table
    
@app.route('/buy' , methods=['POST'])
def buy():
     years = request.form['number']
     total_time = int(years) * 365
     return render_template("buy.html", total_time = total_time, stock_data=getTableData(curr_day))

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/exchange', methods=['GET'])
def exchange():
    stock_name = request.args.get('stock_name')
    price = request.args.get('stock_info[1]')
    return render_template("exchange.html", stock_name = stock_name, price= price)

@app.route('/more')
def more():
    return render_template("more.html")


if __name__ == '__main__':
    app.run()
