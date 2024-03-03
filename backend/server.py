import time
from flask import Flask, request, render_template
from data_generator import all_data


app = Flask(__name__)
total_time = 0 #in days
curr_day = 0
amount = 10000

@app.route('/')
def home():
    return render_template("landingPage.html")

@app.route('/tryMe')
def tryMe():
    return render_template("tryMe.html")

@app.route('/aboutMe')
def aboutMe():
    return render_template("aboutMe.html")

@app.route('/financeBasics')
def financeBasics():
    return render_template("financeBasics.html")
    
# cancel buy/sell transaction
@app.route('/cancel')
def cancel():
     return render_template("buy.html", total_time = total_time, stock_data=getTableData(curr_day))

@app.route('/buy-update')
def buyAndUpdate():
    # update amount

    # update myData
    # 
    return render_template("more.html")

@app.route('/sell-update')
def sellAndUpdate():
    # update amount
    
    # update myData
    # 
    return render_template("more.html")

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

@app.route('/buy-2')
def buy2():
    return render_template("buy.html", stock_data=getTableData(curr_day))

@app.route('/sell', methods=["POST"])
def sell():
    return render_template("sell.html")

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
