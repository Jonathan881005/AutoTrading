# USAGE: python app.py --training op3.csv --output submission.csv --periods 8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from pmdarima.arima import auto_arima
# You can write code above the if-main block.
if __name__ == '__main__':
    # You should not modify this part, but additional arguments are allowed.
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')

    parser.add_argument('--output',
                        default='submission.csv',
                        help='output file name')
    parser.add_argument('--periods',
                        default='10',
                        help='n periods',
                        required=True)
    args = parser.parse_args()
    
    # The following part is an example.
    # You can modify it at will.
    df_training = pd.read_csv(args.training)
    arima = auto_arima(df_training["operating_reserve(MW)"], seasonal=True)
    result = arima.predict(n_periods=int(args.periods))
    result = result.astype('int32')
    result = {"date": [20210323, 20210324, 20210325, 20210326, 20210327, 20210328, 20210329],
              "operating_reserve(MW)": result[-7:]
             }
    df_result = pd.DataFrame(result)
    df_result.to_csv(args.output, index=0)
