# USAGE: 
#   python trader.py --training training.csv --testing testing.csv --output output.csv
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


    df_training = pd.read_csv(args.training)
    c0 = df_training.columns[0]
    print(df_training[c0])
    # arima = auto_arima(df_training["operating_reserve(MW)"], seasonal=True)

    arima = auto_arima(df_training[c0], start_p=1, start_q=1,max_p=3, max_q=3, m=12,start_P=0, seasonal=True, d=1, D=1, trace=True, error_action='ignore',suppress_warnings=True)
    result = arima.predict(n_periods = 20)
    result = result.astype('float32')
    print(result)

    df_result = pd.DataFrame(result)
    df_result.to_csv(args.output, index=0)

