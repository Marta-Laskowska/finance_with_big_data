# PC Lab 4 – Predicting Stock Returns with Machine Learning

## Overview

This project applies machine learning techniques to predict stock returns using daily price and volume data.  
The objective is to train predictive models, evaluate their out-of-sample performance, and construct an AI-driven portfolio based on model forecasts.

The project bridges empirical asset pricing and modern machine learning methods, focusing on practical portfolio implementation.

---

## Task

The objectives were:

- Manipulate and visualize stock price and volume data  
- Construct predictive features from prices and volumes  
- Train linear and regularized regression models  
- Evaluate out-of-sample predictive performance  
- Implement alternative ML models (e.g., Neural Networks or Trees)  
- Build a portfolio based on predicted returns  
- Compare performance to random portfolios  
- Evaluate the impact of transaction costs  

The broader context:  
We were asked to act as interns at a quantitative hedge fund and test whether simple machine learning models, applied at daily frequency using limited signals (prices and volumes), can generate predictive power and profitable trading strategies.

---

## Structure

```
.
├── PC_Lab_4.ipynb                 # Main notebook with full ML pipeline and portfolio analysis
├── scraped_data_close_volume.csv  # Scraped price and volume dataset
└── README.md                      # Project documentation
```

---

## Data

- Daily stock prices (closing prices)  
- Daily trading volumes  
- Multiple securities including large-cap stocks and the S&P 500  
- Scraped or downloaded financial data  

The dataset combines price and volume information to construct predictive signals over different horizons (short, medium, and long term).

---

## Methods

- Exploratory analysis of prices and trading volumes  
- Feature construction using past returns and past volumes (5, 20, 60-day windows)  
- Train-test split (75% training, 25% testing)  
- OLS regression model  
- Ridge regression with regularization  
- Out-of-sample performance evaluation using:

\[
R_{OOS} = 1 - \frac{\sum (r_{t} - \hat{r}_{t})^2}{\sum r_{t}^2}
\]

- Alternative performance metrics: MSE, sign accuracy, R²  
- Extension to non-linear models (e.g., Neural Networks or Tree-based methods)  
- Construction of a long-only AI-driven portfolio selecting top predicted assets  
- Comparison with randomly generated portfolios  
- Evaluation of performance with and without transaction costs  

---

## Results

- Estimation of predictive performance across different horizons  
- Comparison between OLS, Ridge, and alternative ML models  
- Measurement of out-of-sample predictive power  
- Construction of an AI-driven portfolio and cumulative return analysis  
- Performance comparison against random allocation benchmarks  
- Assessment of sensitivity to trading costs  

The results highlight the challenges of daily return prediction and the importance of proper out-of-sample validation in financial machine learning.

---

## Key Learnings

- Financial return predictability is weak at high frequency  
- Regularization improves model stability relative to OLS  
- Out-of-sample evaluation is crucial in avoiding overfitting  
- Portfolio implementation must account for transaction costs  
- Machine learning models require careful economic interpretation  

---

## Team

This project was developed for the course **Finance with Big Data** – Bocconi University

**Team Members:**
- Luca Milani
- Marta Laskowska
- Monika Kaczorowska

---

## Financial Interpretation

This project illustrates how machine learning techniques can be integrated into asset pricing and portfolio construction.  
It emphasizes the distinction between statistical predictability and economic profitability, particularly when transaction costs and model instability are taken into account.