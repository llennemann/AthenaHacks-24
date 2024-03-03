import numpy as np
import matplotlib.pyplot as plt

def all_data(): #time is in dayas and stock_names is a list of strings
    stocks = { 
        "BluePeak Energy": "Renewable Energy",
        "CyberNetic Tech": "Artificial Intelligence",
        "SolarFlare Power": "Solar Energy",
        "VirtualRealms Gaming": "Video Games",
        "AquaGen Biotech": "Biotechnology",
        "Mystic Media": "Entertainment",
        "EcoMobile Autos": "Electric Vehicles",
        "NanoMaterials Corp": "Nanotechnology",
        "FutureFinance": "FinTech",
        "HealthPulse Pharma": "Pharmaceuticals",
    }


    def generate(stocks, days=10950):
        np.random.seed(120)
        new_dict = {}
        mu_set = [0.0005, 0.0007, 0.0001, 0.0006, 0.0004, 0.0008, 0.0009, 0.0007, 0.0005, 0.0006]
        sigma_set = [0.02, 0.025, 0.03, 0.022, 0.02, 0.03, 0.035, 0.025, 0.02, 0.03]
        start = [100, 150.7, 100.8, 120, 80, 75, 180, 199, 90.5, 100.5]

        for i, stock in enumerate(stocks.keys()):
            mu = mu_set[i]
            sigma = sigma_set[i]
            start_price = start[i]

            prices = [start_price]
            for _ in range(1, days):
                change = np.random.normal(mu, sigma)
                prices.append(prices[-1] * (1 + change))

            new_dict[stock] = prices

        return new_dict

    return stocks, generate(stocks)
     
def portfolio_data (time_bought, time_sold, stock_names):
    dict_stocks = all_data()[1]
    my_data = {}
    for i in stock_names:
        my_data[i] = dict_stocks[i][time_bought:time_sold]
    return my_data
