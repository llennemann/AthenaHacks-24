import time
from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from data_generator import all_data, buyStockDataUpdate, getMyData


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

total_time = 0 #in days
curr_day = 0



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

@app.route('/buy-update', methods=['GET'])
def buyAndUpdate():
    price = float(request.args.get('price'))
    stock_name = request.args.get('stock_name')
    num_shares = float(request.args.get('num_shares'))

    # update amount
    # amount already exists, update amount
    if 'amount' in session:
        session['amount'] = session.get('amount') - (price * num_shares)
    else:
        session['amount'] = 10000 - (price * num_shares)

    # update myData
    buyStockDataUpdate(stock_name, curr_day, num_shares)

    print(getMyData())
 
    return render_template("more.html")

@app.route('/sell-update')
def sellAndUpdate():
    # update amount
    
    # update myData
    # 
    return render_template("more.html")

# for the BUY table
def getTableData(currentDay):
    industries, stocks = all_data()
    table = {} # result dictionary
    for key in stocks.keys():
        table[key] = [industries.get(key), stocks.get(key)[currentDay]]

    return table

def getSellTableData(currentDay):
    industries, stocks = all_data()
    mystocks = getMyData()
    table = {} # result dict
    for key in mystocks.keys():
        boughtDay = mystocks.get(key)[0] 
        soldDay = mystocks.get(key)[1]
        num_shares = mystocks.get(key)[2]
        if soldDay == -1: # if -1, hasn't been sold yet
            table[key] = [industries.get(key), stocks.get(key)[boughtDay], stocks.get(key)[currentDay], num_shares]
    
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
    return render_template("sell.html", mystock=getSellTableData(curr_day))

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/exchange', methods=['GET'])
def exchange():
    stock_name = request.args.get('stock_name')
    price = request.args.get('stock_info[1]')
    return render_template("exchange.html", stock_name = stock_name, price= price)

@app.route('/sell-exchange', methods=['GET'])
def sell_exchange():
    stock_name = request.args.get('stock_name')
    price_now = request.args.get('price_now')
    num_shares = request.args.get('num_shares')
    return render_template("sell-exchange.html", stock_name = stock_name, price= price_now, num_shares=num_shares)

@app.route('/more')
def more():
    return render_template("more.html")


if __name__ == '__main__':
    app.run()
