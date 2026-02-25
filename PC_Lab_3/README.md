# PC Lab 3 – Creating a Factor from Text Data

## Overview

This project explores the predictive power of financial Twitter data by constructing a sentiment-based media attention factor.  
The objective is to clean and analyze text data, perform sentiment classification, and test whether Twitter attention is related to stock returns.

The project combines natural language processing (NLP) techniques with asset pricing methods to evaluate whether social media signals can serve as an investment factor.

---

## Task

The objectives were:

- Manipulate and describe a dataset of financial tweets  
- Clean and preprocess text data  
- Perform sentiment analysis using advanced NLP models  
- Construct firm-level measures of media attention  
- Form portfolios based on attention metrics  
- Test whether media attention predicts stock returns  
- (Optional) Remove traditional risk factors using Fama–French 5 factors  

The broader context:  
We were asked to act as analysts in a hedge fund and evaluate whether Twitter sentiment and media attention could generate a new investment factor.

---

## Structure

```
.
├── PC_Lab_3_1.ipynb                          # Tasks 1–3: data cleaning and sentiment analysis
├── PC_Lab_3_2.ipynb                          # Task 4 and optional factor testing
├── PC_Lab_3_2_1.ipynb                        # Extended/alternative version of second notebook
├── Data_PCLab3_Twitter_Stock_Sentiment.csv   # Original Twitter dataset (large file)
├── final_aggregated_sentiments.csv           # Aggregated sentiment dataset
├── F-F_Research_Data_5_Factors_2x3_daily.csv # Fama–French 5 factors (daily)
├── F-F_Research_Data_5_Factors_2x3.csv       # Fama–French 5 factors (monthly)
├── ff5_residuals_static.csv                  # Residual returns after FF5 regression
└── README.md                                 # Project documentation
```

Note:  
`PC_Lab_3_1.ipynb` uses a large StockTwits dataset and may take significant time to run.  
`PC_Lab_3_2.ipynb` runs quickly and includes configurable settings (e.g., same-day vs next-day returns).

---

## Data

- Financial tweets from StockTwits containing stock tickers and sentiment labels  
- Aggregated firm-level sentiment measures  
- Daily stock returns  
- Fama–French 5 factors (Mkt-RF, SMB, HML, RMW, CMA, RF)  

The first notebook processes raw tweet data, while the second notebook uses the aggregated sentiment dataset for portfolio construction and factor testing.

---

## Methods

- Descriptive statistics on tweets (volume, word counts, sentiment distribution)  
- Text preprocessing: cleaning URLs, mentions, hashtags, tokenization, stopword removal  
- Sentiment classification using pretrained NLP models  
- Aggregation of sentiment to firm-day level  
- Construction of media attention measures (tweet counts, positive/negative ratios, disagreement)  
- Formation of portfolios based on attention rankings  
- Testing relationship between attention and returns  
- Optional regression of returns on Fama–French 5 factors to extract abnormal returns  

---

## Results

- Construction of a firm-level Twitter sentiment and attention measure  
- Identification of variation in media attention across stocks  
- Evidence of a relationship between attention metrics and stock returns  
- Comparison between raw returns and risk-adjusted (FF5 residual) returns  
- Assessment of whether media attention can serve as a potential factor  

The results illustrate how alternative data sources can be integrated into traditional asset pricing frameworks.

---

## Key Learnings

- Text data requires substantial preprocessing before financial analysis  
- Sentiment classification performance varies depending on model choice  
- Media attention may capture behavioral or informational effects not explained by traditional factors  
- Alternative data can complement classical asset pricing models  

---

## Team

This project was developed for the course **Finance with Big Data** – Bocconi University

**Team Members:**
- Luca Milani
- Marta Laskowska
- Monika Kaczorowska

---

## Financial Interpretation

This project demonstrates how social media data can be transformed into a quantitative investment signal.  
By combining NLP techniques with portfolio construction and factor regressions, it evaluates whether investor attention and sentiment contain predictive information beyond traditional risk factors.