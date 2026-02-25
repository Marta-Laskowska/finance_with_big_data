# PC Lab 2 – Applying the CAPM

## Overview

This project applies the Capital Asset Pricing Model (CAPM) to a set of S&P 500 stocks.  
The objective is to estimate systematic risk (beta), measure abnormal performance (alpha), and empirically test whether the CAPM explains realized returns.

The project connects asset pricing theory with empirical implementation using regression analysis and financial data.

---

## Task

The objectives were:

- Visualize stock returns against market returns  
- Estimate CAPM alpha and beta using OLS regression  
- Evaluate statistical significance of parameters  
- Identify high-beta (riskier) stocks  
- Construct a portfolio of risky assets  
- Test CAPM predictions using rolling yearly betas  
- Compare realized and predicted returns  
- (Optional) Collect market data via web-scraping and APIs  

The broader context:  
We were asked to act as analysts in a small hedge fund and estimate the systematic risk (beta) of selected stocks in order to guide investment decisions.

---

## Structure

```
.
├── PCLab_2.ipynb           # Main Jupyter notebook with full CAPM analysis
├── Data_PCLab1_Stock.csv   # Stock price dataset
└── README.md               # Project documentation
```

---

## Data

- Historical daily prices of selected S&P 500 stocks  
- Market benchmark: S&P 500 index  
- Time period starting in 2012  
- Returns computed from daily closing prices  

Preprocessing included computing daily returns, aligning stock and market series, and preparing data for regression analysis.

---

## Methods

- Scatter plots of stock returns against market returns  
- Estimation of CAPM parameters via OLS regression:

\[
R_i = \alpha_i + \beta_i R_M + \varepsilon_i
\]

- Statistical significance testing of alpha and beta  
- Ranking stocks by estimated beta  
- Construction of an equally weighted portfolio of high-beta stocks  
- Rolling yearly estimation of beta (252 trading days)  
- Comparison of realized vs CAPM-predicted returns  
- Visualization of prediction errors and regression residuals  

---

## Results

- Estimated beta values capturing systematic risk exposure  
- Identification of high- and low-beta stocks  
- Evidence that alpha is often not statistically significant  
- Differences between realized and CAPM-predicted returns  
- Empirical illustration of the limitations of the CAPM in explaining cross-sectional returns  

The results highlight the gap between theoretical asset pricing models and real-world market behavior.

---

## Key Learnings

- Beta measures systematic exposure but does not fully explain expected returns  
- Empirical CAPM tests are sensitive to estimation window choice  
- High-beta stocks do not necessarily deliver proportionally higher realized returns  
- Asset pricing models require careful economic interpretation beyond statistical estimation  

---

## Team

This project was developed for the course **Finance with Big Data** – Bocconi University

**Team Members:**
- Luca Milani
- Marta Laskowska
- Monika Kaczorowska

---

## Financial Interpretation

This project demonstrates how the CAPM can be tested empirically using regression techniques.  
It shows how systematic risk is estimated in practice and provides insight into the empirical challenges of validating asset pricing models in financial markets.