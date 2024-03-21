"""Questions I am going to try and answer:
1.) What was the change in price of the stock over time?
2.) What was the daily return of the stock on average?
3.) What was the moving average of the various stocks?
4.) What was the correlation between different stocks' closing prices?
4.) What was the correlation between different stocks' daily returns?
5.) How much value do we put at risk by investing in a particular stock?
6.) How can we attempt to predict future stock behavior?
"""

# Data
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import yfinance as yf

# Viz
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# This allows us to read stock information
# wb imports data from World Bank
from pandas_datareader import wb
import pandas_datareader.data as web
# This is for time stamps
from datetime import datetime

# This is installing required fix for yfinance
yf.pdr_override()

tech_list = ['AAPL','GOOG','MSFT','AMZN']
end = datetime.now()
# we subtract 1 from year because we want a year ago
start = datetime(end.year-1,end.month,end.day)

# Dictionary to store DataFrames
stock_data_dict = {}

# now lets make for loop for grabbing some finance data

for ticker in tech_list:
    try:
        stock_data = web.DataReader(ticker, start=start, end=end)
        # add column for stock symbol
        stock_data['Symbol'] = ticker
        # now add dframe to dictionary
        stock_data_dict[ticker] = stock_data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
   
(stock_data_dict['AAPL'].describe())

# Adj(adjusted) close takes into account any changes in the stock
# we will use it to perform historical data analysis
plt.plot(stock_data_dict['AAPL']['Adj Close'])
plt.title(f'AAPL Plot')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend(['Adj Close'])
plt.figure(figsize=(10,4))


# Now lets plot the total volume of stock traded each day this past year
plt.plot(stock_data_dict['AAPL']['Volume'])
plt.title(f'Volume of AAPL Traded Per Day')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.legend(['Volume'])
plt.figure(figsize=(10,4))


# Calculating the moving average
# Make a list for different moving averages i.e. 10 day/20 day
ma_day = [10,20,50]

for ma in ma_day:
    column_name = "MA for %s days" %(str(ma))
    stock_data_dict['AAPL'][column_name] = stock_data_dict['AAPL']['Adj Close'].rolling(window=ma).mean()

# Set figure size before plotting
plt.figure(figsize=(10,4))

plt.plot(stock_data_dict['AAPL']['Adj Close'], label='Adj Close')
for ma in ma_day:
    column_name = "MA for %s days" %(str(ma))
    plt.plot(stock_data_dict['AAPL'][column_name], label=column_name)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('AAPL Data with Moving Averages')
plt.legend(['Adj Close'] + [f'MA for {ma} days' for ma in ma_day])


# Now let's take a quick look at daily returns and risk of the stock
# First we make a new column

stock_data_dict['AAPL']['Daily Return'] = stock_data_dict['AAPL']['Adj Close'].pct_change()

# Now let's plot
plt.figure(figsize=(10,4))

plt.plot(stock_data_dict['AAPL']['Daily Return'],linestyle='--',marker='o')
plt.title(f'Daily Returns of AAPL Stock')
plt.xlabel('Date')
plt.legend(['Daily Return'])


# We can look at average daily return using a histogram

sns.displot(stock_data_dict['AAPL']['Daily Return'].dropna(),bins=100,color='purple',kde=True)

# What if we wanted to analyze all the returns of the stock
# We will build new data frame of adj close columns

closing_df = pd.DataFrame({ticker: web.DataReader(ticker, start=start, end=end)['Adj Close'] for ticker in tech_list})
(closing_df.head())

# Let's make new df to show daily returns

tech_returns = closing_df.pct_change()
(tech_returns)

# Next check if there is a correlation between AMZN and AAPL
# we create a subset of tech returns df to only show aapl and amzn
tech_returns_subset = tech_returns[['AAPL','AMZN']]
sns.jointplot(x='AAPL',y='AMZN',data=tech_returns_subset,kind='scatter')

# How to repeat comparison analysis for every possible combination of stocks in our list
# We can use pairplot through seaborn
sns.pairplot(data=tech_returns.dropna())

# Using pair plot is simple, but we can dive deeper
# using pair grid and map_ functions we can choose what we want in the grid
# "cmap" means color map

returns_fig = sns.PairGrid(data=tech_returns.dropna())
returns_fig.map_upper(plt.scatter,color='purple')
returns_fig.map_lower(sns.kdeplot,cmap='cool_d')
returns_fig.map_diag(plt.hist,bins=30)

# can use seaborn to see correlation with a correlation plot
# first we calculate correlation matrix

correlation_matrix = tech_returns.corr()

# Then create heatmap of matrix
# "annot" means annotation

plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()

# Time to look at ways to analyze risk of the stock

rets = tech_returns.dropna()
# area is used to define area of the circles in the scatterplot
area = np.pi*20
plt.figure(figsize=(10,8))
plt.scatter(x=rets.mean().values,y=rets.std().values,s=area)
plt.xlabel('Expected Returns')
plt.ylabel('Risk')

for label, x, y in zip(rets.columns, rets.mean(), rets.std()):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (50, 50),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=-0.3',color='red'))


# Let's look at value at risk
# Step 1: make daily returns histogram for aapl
plt.figure(figsize=(10,8)) 
sns.histplot(stock_data_dict['AAPL']['Daily Return'].dropna(),kde=True,bins=100,color='purple')
plt.show()

# Step 2: Use quantile to get risk value of stock
print("Risk of AAPL: " + str(rets['AAPL'].quantile(0.05)))
print("Risk of MSFT: " + str(rets['MSFT'].quantile(0.05)))
print("Risk of GOOG: " + str(rets['GOOG'].quantile(0.05)))
print("Risk of AMZN: " + str(rets['AMZN'].quantile(0.05)))