# USAGE: python trader.py --training training.csv --testing testing.csv --output output.csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from pmdarima.arima import auto_arima
# You can write code above the if-main block.
if __name__ == '__main__':
    # You should not modify this part.

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training.csv',
                       help='input training data file name')

    parser.add_argument('--testing',
                        default='testing.csv',
                        help='input testing data file name')

    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')

    args = parser.parse_args()
    
    # The following part is an example.
    # You can modify it at will.

    df_training = pd.read_csv(args.training, header = None)
    c0 = df_training.columns[0]

    df_testing = pd.read_csv(args.testing, header = None)
    period = df_testing.shape[0] # number of columns

    arima = auto_arima(df_training[c0], start_p=1, start_q=1,max_p=3, max_q=3, m=12,start_P=0, seasonal=True, d=1, D=1, trace=True, error_action='ignore',suppress_warnings=True)
    result = arima.predict(n_periods = period) # Predict the stock price of the following xx days 
    result = result.astype('float32')

    prev = 0
    stock = [] # rise or fall
    isfirst = True
    for nxt in result:
        if(isfirst):
            isfirst = False
            prev = nxt
            continue

        if(prev > nxt):
            stock.append(0)          
        else:
            stock.append(1) 

        prev = nxt


    now = 0 # have stock or not
    res = []
    isfirst = True
    for tomo in stock:
        if(now == -1):      # short 
            if(tomo):   # rise
                now = 0
                res.append(1)
            else:       # fall
                now = -1
                res.append(0)


        elif(now == 0):     # no stock
            if(tomo):       # rise
                now = 1
                res.append(1)       # buy
            else:               # fall
                now = -1
                res.append(-1)      # nope

        else:               # have stock
            if(tomo):           # rise
                now = 1
                res.append(0)       # hold
            else:               # fall
                now = 0
                res.append(-1)      # sell 


    df_res = pd.DataFrame(res)
    df_res.to_csv(args.output, index = 0, header = False)