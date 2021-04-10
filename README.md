# AutoTrading
## Usage
`python trader.py --training training.csv --testing testing.csv --output output.csv`
## Data analysis
![](https://scontent.fkhh1-1.fna.fbcdn.net/v/t1.15752-9/169263519_287989606252131_639722569939506058_n.png?_nc_cat=106&ccb=1-3&_nc_sid=ae9488&_nc_ohc=tuPQsT5FQ-0AX_DcyRc&_nc_oc=AQmmdxn6ZSmx9JK2sy7m5aM85-qctG8PgOXmXmDKcJWbx4O_O5tssyZZgxh7E4x3Lw2XBy2NSVSIXWheZ3e_WGmF&_nc_ht=scontent.fkhh1-1.fna&oh=4357fddbe1c9d9bcb86e4f39ef06f8fb&oe=60978395)
## Model Training
* load data
```python
df_training = pd.read_csv(args.training, header = None)
```
* Use ARIMA to train model
```python
arima = auto_arima(df_training[c0], start_p=1, start_q=1,max_p=3, max_q=3, m=12,start_P=0, seasonal=True, d=1, D=1, trace=True, error_action='ignore',suppress_warnings=True)
```
* Predict
```python
result = arima.predict(n_periods = period)
```
* Write csv
```python
    df_res = pd.DataFrame(res)
    df_res.drop(index=0,inplace=True)
    df_res.to_csv(args.output, index = 0)
```



