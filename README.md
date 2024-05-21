# New Zealand Stocks and Machine Learning
New Zealand's Exchange, known commonly as the NZX, is the national stock exchange for New Zealand and a publicly owned company. For this project I will be using the NZX50 stocks index which is the main stock market index in New Zealand. It comprises of the 50 biggest stocks by free-float market capitalisation trading on the New Zealand Stock Market.

Machine learning uses patterns it learned from data to accomplish a goal. The goal
of this project is to use machine learning to extract information from stocks data to
automate key investment activities. The key to beating the stock market is to find
an edge, also known as alpha. Alpha is used in finance as a measure of performance,
indicating when a strategy has accomplished beating the market return over some
period.

## Project Description
For this project, I will focus on using unsupervised learning to identify structure in
data in order to identify patterns, correlations, or anomalies in data. Unsupervised
learning can help us gain insight on financial data without having labeled training
data.

## Structure of the Project
1) The start the project we have to have Python 3.12.2 in our Computer and install the necessary packages. I'm using a M1 Mac for this project.
2) Download NZX50 Stocks File and Grab symbols from dataframe and convert into a list for YFinance
3) Calculate Features and Technical indicators for each stock
4) Calculate Monthly Returns for different time horizons as features
5) Download Fama-French Factors and Calculate Rolling Factor Betas
6) K-Means Clustering
7) For each month select assests based on the cluster and form a portfolio based on Efficient Frontier max sharpe ratio optimization
8) Using PyPortfolioOpt and EfficientFrontier optimizer, to define a function to maximize the sharpe ratio

## Python Environment and Packages used in the Notebook 
* Python 3.12.2
* from statsmodels.regression.rolling import RollingOLS
* pandas_datareader.data 
* matplotlib.pyplot 
* statsmodels.api 
* pandas 
* numpy 
* datetime
* yfinance 
* pandas_ta
* sklearn.cluster 
* my_functions (Includes custom functions for calculating garman klass volatility, relative strength index, bollinger bands, Average true range, Moving average convergence/divergence)



