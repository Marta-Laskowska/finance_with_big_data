# PC Lab 1 – Applied Portfolio Theory

## Overview

This project applies Markowitz’s Modern Portfolio Theory to a selection of S&P 500 stocks.  
The goal is to manipulate financial time series data, compute portfolio statistics, simulate random portfolios, and identify the tangency (maximum Sharpe ratio) portfolio.

The project combines data analysis, visualization, and portfolio optimization techniques in Python, bridging financial theory with practical implementation.

---

## Task

The objectives were:

- Import and clean stock price data
- Perform exploratory data analysis
- Compute and visualize normalized prices
- Calculate daily returns and correlations
- Simulate random portfolios
- Identify the tangency portfolio (maximum Sharpe ratio)
- Draw the efficient frontier
- Test out-of-sample portfolio performance

The broader context:  
We were asked to act as analysts in an asset management company and determine the optimal portfolio weights for a regulated mutual fund with no transaction costs.

---

## Structure

```
.
├── PCLab_1.ipynb           # Main Jupyter notebook with full analysis
├── Data_PCLab1_Stock.csv   # Stock price dataset
├── DFF.csv                 # Interest rates dataset
└── README.md               # Project documentation
```

---

## Data

- Historical daily prices of selected S&P 500 stocks  
- Time period starting in 2012  
- Large-cap equities including Amazon, Apple, Tesla, Boeing, MGM and the S&P 500 index  

Preprocessing included sorting by date, checking for missing values, and computing basic descriptive statistics.

---

## Methods

- Exploratory data analysis of price dynamics  
- Price normalization to compare relative performance  
- Computation of daily returns and correlation matrix  
- Visualization using line plots, histograms, and heatmaps  
- Simulation of 1000 random portfolios  
- Calculation of portfolio return, volatility, and Sharpe ratio  
- Identification of the maximum Sharpe (tangency) portfolio  
- Optional estimation of the efficient frontier and out-of-sample testing  

---

## Results

- Identification of the tangency portfolio maximizing the Sharpe ratio  
- Visualization of the risk–return tradeoff through portfolio simulations  
- Evidence of strong correlations among large-cap stocks  
- Out-of-sample analysis highlighting sensitivity of mean-variance optimization to estimation error  

The results illustrate both the practical implementation and the limitations of classical portfolio theory.

---

## Key Learnings

- Portfolio optimization is highly sensitive to return and covariance estimates  
- Diversification benefits depend heavily on correlation structure  
- In-sample optimal portfolios may not perform equally well out-of-sample  

---

## Team

This project was developed for the course **Finance with Big Data** – Bocconi University

**Team Members:**
- Luca Milani
- Marta Laskowska
- Monika Kaczorowska

---

## Financial Interpretation

This project demonstrates how classical Markowitz theory can be implemented using modern data science tools. It highlights the tradeoff between risk and return and illustrates both the power and the limitations of mean-variance optimization in real-world financial markets.