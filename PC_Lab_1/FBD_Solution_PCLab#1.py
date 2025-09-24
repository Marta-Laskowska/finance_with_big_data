# ------------------------------------------------------------------------------------------------------- #
# PCLab 1 Solution: this files focuses on some aspects (not all) of the PC Lab.
# In particular: How to compute return and risk of a portfolio, optimization and testing the M-V framework.


# If you have any issue understanding my code / if you want a more detailed solution, please contact me: clement.mazetsonilhac@unibocconi.it
# OR, have a look to some of your collegues' solution (on BBoard), they meight be better than mine! 
# ------------------------------------------------------------------------------------------------------- #


# ------------------------------------------------------------------------------------------------------- #
# Import packages:
# ------------------------------------------------------------------------------------------------------- #

from xml.dom.expatbuilder import theDOMImplementation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from copy import copy
from scipy import stats
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

# ------------------------------------------------------------------------------------------------------- #
# Import data:
# ------------------------------------------------------------------------------------------------------- #

stocks_df = pd.read_csv('C:/Users/cms27/Dropbox/FinanceBigData/S1_AssetPricing1/Lab1/Data_PCLab1_Stock.csv')
stocks_df

# Sort the stock data by date
stocks_df = stocks_df.sort_values(by = ['Date'])

# ------------------------------------------------------------------------------------------------------- #
# Task #1 tp #3 are not covered here.
# ------------------------------------------------------------------------------------------------------- #



# ------------------------------------------------------------------------------------------------------- #
# Task #5: Calculate stock returns
# ------------------------------------------------------------------------------------------------------- #

# Let's define a function to calculate stocks daily returns (for all stocks) 
def daily_return(df):
  df_daily_return = df.copy()

  # Loop through each stock (while ignoring time columns with index 0)
  for i in df.columns[1:]:
    
    # Loop through each row belonging to the stock
    for j in range(1, len(df)):

      # Calculate the percentage of change from the previous day
      df_daily_return[i][j] = ((df[i][j]- df[i][j-1])/df[i][j-1]) * 100
    
    # set the value of first row to zero since the previous value is not available
    df_daily_return[i][0] = 0
  
  return df_daily_return

stocks_daily_return = daily_return(stocks_df)

# Plot the histograms:
def show_plot(df, fig_title):
  df.plot(x = 'Date', figsize = (15,7), linewidth = 2, title = fig_title)
  plt.grid()
  plt.show()

# Notice huge drops in MGM around March 2020 (Pandemic effect)
show_plot(stocks_daily_return, 'STOCKS DAILY RETURNS')

# Daily Return Correlation
cm = stocks_daily_return.drop(columns = ['Date']).corr()

plt.figure(figsize=(10, 10))
ax = plt.subplot()
sns.heatmap(cm, annot = True, ax = ax);
plt.show()

# Histogram of daily returns
stocks_daily_return.hist(figsize=(10, 10), bins = 40);
plt.show()

# Interactive version (be carefull with same bins and same scale!):
df_hist = stocks_daily_return.copy()
df_hist = df_hist.drop(columns = ['Date'])
data = []

# Loop through every column
for i in df_hist.columns:
  data.append(stocks_daily_return[i].values)

fig = ff.create_distplot(data, df_hist.columns)
fig.show()

# ------------------------------------------------------------------------------------------------------- #
# Task #6 & #7: Efficient frontier, testing the M-V framework
# ------------------------------------------------------------------------------------------------------- #

# We need new packages:
from pickletools import optimize
from tkinter import W
import numpy as np

stocks_df['Date'] = pd.to_datetime(stocks_df['Date'])
stocks_df = stocks_df.set_index(stocks_df['Date'])
stocks_df = stocks_df.sort_index()

stocks = (stocks_df.drop('Date', axis=1))
stocks = stocks[['AAPL','MGM', 'AMZN', 'IBM', 'BA', 'T', 'TSLA', 'GOOG']].copy()

log_ret = np.log(stocks/stocks.shift(1))

np.random.seed(42)
num_ports = 10000
all_weights = np.zeros((num_ports, len(stocks.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

def simulate_portfolio(nb, size, data):
  num_ports = nb

  for x in range(num_ports):

    # Weights
    weights = np.array(np.random.random(size))
    weights = weights/np.sum(weights)
    
    # Save weights
    all_weights[x,:] = weights
    
    # Expected return (we multiply by 252, the number of business days to annualize returns!)
    ret_arr[x] = np.sum((data.mean() * weights * 252))
    
    # Expected volatility
    vol_arr[x] = np.sqrt(np.dot(weights.T, np.dot(data.cov()*252, weights)))
    
    # Sharpe Ratio
    sharpe_arr[x] = ret_arr[x]/vol_arr[x]

  

simulate_portfolio(10000, 8, log_ret)

# Where is the highest Sharpe ratio
maxw = sharpe_arr.argmax()
print(all_weights[maxw,:])

max_sr_ret=ret_arr[sharpe_arr.argmax()]
max_sr_vol=vol_arr[sharpe_arr.argmax()]

print('Max sharpe ratio in the array: {}'.format(sharpe_arr.max()))
print('Location in the array: {}'.format(sharpe_arr.argmax()))


plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.scatter(max_sr_vol, max_sr_ret,c='red', s=50) # tangency
plt.show()

# ------------------------------------------------------------------------------------------------- #
# Optimization part: drawing the efficient frontier:

# A function that takes weights as inputs and return an array of return, vol and SR:
def get_ret_vol_sr(weights):
    weights = np.array(weights)
    ret = np.sum(log_ret.mean() * weights) * 252
    vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))
    sr = ret/vol
    return np.array([ret, vol, sr])

# Minimization is the inverse of optimization, so we want negative SR:
def neg_sharpe(weights):
# the number 2 is the sharpe ratio index from the get_ret_vol_sr
    return get_ret_vol_sr(weights)[2] * -1

# Contraint for opt.: weights should always sum to 1:
def check_sum(weights):
    #return 0 if sum of the weights is 1
    return np.sum(weights)-1

# Definition of constraint, bounds and initial guess:
cons = ({'type':'eq','fun':check_sum})
bounds=((0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1))
init_guess = [0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25]

# This function simply minimize the negative SR (i.e. maximize the SR), we test it on 1 possible SR here:
import scipy
opt_results = scipy.optimize.minimize(neg_sharpe, init_guess, method='SLSQP', bounds=bounds, constraints=(cons))
print(opt_results)

get_ret_vol_sr(opt_results.x) # works well! But we won't have the lower part of the efficient frontier (where the SR is very low)

# So let's try another minimization: given a return, find the minmum vol. 
# Let's apply that to all possible returns
frontier_y = np.linspace(0,0.3,200)

def minimize_vol(weights):
    return get_ret_vol_sr(weights)[1]

# Ready to store the vol results
frontier_x = []

# Optimization for all the possible returns, contraint=weights sum to 1, find the lowest vol:
for possible_return in frontier_y:
    cons = ({'type':'eq', 'fun':check_sum},
            {'type':'eq', 'fun': lambda w: get_ret_vol_sr(w)[0] - possible_return}) # Output return should be very close to the input one 
    
    result = scipy.optimize.minimize(minimize_vol,init_guess,method='SLSQP', bounds=bounds, constraints=cons)
    frontier_x.append(result['fun'])

plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='plasma')
plt.scatter(max_sr_vol, max_sr_ret,c='red', s=50) # red dot
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.plot(frontier_x,frontier_y, 'green', linewidth=3)
plt.savefig('cover.png')
plt.show()

# ------------------------------------------------------------------------------------------------- #
# Testing the M-V framework on 2 periods:

# Let's create a training and test sample:
train_sample = (stocks_df.query('20120112 <= Date < 20171230').drop('Date', axis=1))
train_sample = train_sample[['AAPL','MGM', 'AMZN', 'IBM', 'BA', 'T', 'TSLA', 'GOOG']].copy()

test_sample = (stocks_df.query('20171230 <= Date <= 20200811').drop('Date', axis=1))
test_sample = test_sample[['AAPL','MGM', 'AMZN', 'IBM', 'BA', 'T', 'TSLA', 'GOOG']].copy()

# Return of the stocks over the train/test sample
log_ret_train = np.log(train_sample/train_sample.shift(1))
log_ret_test = np.log(test_sample/test_sample.shift(1))

# We find the M-V weights on the train sample:
np.random.seed(42)
simulate_portfolio(10000, 8, log_ret_train)

maxw = sharpe_arr.argmax()
print(all_weights[maxw,:])
max_sr_ret=ret_arr[sharpe_arr.argmax()]
max_sr_vol=vol_arr[sharpe_arr.argmax()]

# Save the optimak weights according to M-V theory
optweight = all_weights[maxw,:]
# We also create equal weights for comparison
equalweight = np.array([0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125])

# Return/volalatility of our optimal portfolio over the test period:
ret_test = np.sum( (log_ret_test.mean() * optweight * 252))
vol_test = np.sqrt(np.dot(optweight.T, np.dot(log_ret_test.cov()*252, optweight)))

# Return/volalatility of our EW portfolio over the test period:
ret_ew_test = np.sum( (log_ret_test.mean() * equalweight * 252))
vol_ew_test = np.sqrt(np.dot(equalweight.T, np.dot(log_ret_test.cov()*252, equalweight)))


# Now find the best weights on the test sample and compare to our predicted ones:
# We find the M-V weights on the train sample:
np.random.seed(42)
simulate_portfolio(10000, 8, log_ret_test)

maxw = sharpe_arr.argmax()
print(all_weights[maxw,:])

max_sr_ret=ret_arr[sharpe_arr.argmax()]
max_sr_vol=vol_arr[sharpe_arr.argmax()]

# 1st plot: Tangency portfolio of the test period vs. performance of the optimal portfolio based on training sample weights:
plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.scatter(max_sr_vol, max_sr_ret,c='red', s=50) # tangency over test sample
plt.text(max_sr_vol+0.003, max_sr_ret+0.003, "Tangency portfolio (2017-2020)", c = "red", weight="bold")
plt.scatter(vol_test, ret_test,c='green', s=50) # m-v optimal predicted over train sample
plt.text(vol_test, ret_test-0.015, "Optimal portfolio (opt. weights from 2012-2017)", c = "green", weight="bold")
plt.show()

# 2nd plot: Tangency portfolio of the test period vs. performance of the optimal portfolio based on training sample weights + EW portfolio:
# Note that the EW portfolio may be better of worst than the optimal porfolio based on your seed for the random weights. 

plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='plasma')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.scatter(max_sr_vol, max_sr_ret,c='red', s=50) # tangency over test sample
plt.text(max_sr_vol+0.003, max_sr_ret+0.003, "Tangency portfolio (2017-2020)", c = "red", weight="bold")
plt.scatter(vol_test, ret_test,c='green', s=50) # m-v optimal predicted over train sample
plt.text(vol_test, ret_test-0.015, "Optimal portfolio (opt. weights from 2012-2017)", c = "green", weight="bold")
plt.scatter(vol_ew_test, ret_ew_test,c='blue', s=50) # equally weighted over train sample
plt.text(vol_ew_test-0.01, ret_ew_test+0.01, "EW portfolio", c = "blue", weight="bold")
plt.show()
