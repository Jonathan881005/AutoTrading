# AutoTrading
## Usage
`python trader.py --training training.csv --testing testing.csv --output output.csv`
## Data analysis

## Model Training
* load data
```python
df_training = pd.read_csv(args.training)
```
* Use ARIMA to train model
```python
arima = auto_arima(df_training[c0], start_p=1, start_q=1,max_p=3, max_q=3, m=12,start_P=0, seasonal=True, d=1, D=1, trace=True, error_action='ignore',suppress_warnings=True)
```
* Predict
```python
result = arima.predict(n_periods = 20)
```
* Write csv
```python
df_res = pd.DataFrame(res)
df_res.to_csv(args.output, index = 0)
```



