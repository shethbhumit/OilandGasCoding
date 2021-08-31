from statsmodels.tsa.stattools import adfuller

import matplotlib.pyplot as plt

# augmented Dickey Fuller Test 
# to check time series data whether stationary or not .

def adfuller_test(df,window):

    mean = df.rolling(window).mean()
    std = df.rolling(window).std()
    plt.figure(figsize = (12,6))
    plt.plot(df,color ='blue',label = 'original')
    plt.plot(mean,color ='red',label = 'mean')
    plt.plot(std,color ='black',label = 'std')
    plt.legend(loc ='best')
    plt.title("time series data with mean and std rolling data")
    plt.ylabel("prices")
    plt.xlabel("Years")
    
    adf = adfuller(df,autolag='AIC')
    print("Statistic Test : " , adf[0])
    print("p-value : " , adf[1])
    print("# n_lags : " , adf[2])
    print("No of observation: " , adf[3])
    for key,value in adf[4].items():
        print(f" critical value {key} : {value}")