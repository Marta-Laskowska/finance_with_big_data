# Hackathon – NGO Press Campaigns and Responsible Investment

## Overview

This hackathon project investigates whether NGO press campaigns affect stock prices of banks.  
Using ESG-related campaign data from Sigwatch and financial market data, we implement an event-study framework to test whether markets react to positive or negative NGO campaigns.

The project combines ESG analysis, financial econometrics, and event-study methodology to evaluate the market impact of socially responsible investment pressures.

---

## Task

The hackathon proposed several research tasks centered on ESG campaigns and stock market reactions.

In our project, we focused on:

- Task 4: Estimating CAPM (and factor model) parameters  
- Task 5: Computing cumulative abnormal returns (CARs) around campaign dates  
- Task 6: Testing whether NGO campaigns significantly affect stock prices  

Additional exploratory work included:
- Initial attempts at web scraping (Tasks 1–2)  
- Exploratory data analysis of NGO campaign data  

The objective was to determine whether NGO press campaigns generate statistically and economically significant abnormal returns for targeted banks.

---

## Structure

```
.
├── Hackathon_1_web_scraping.ipynb          # Attempted web scraping (Tasks 1–2)
├── Hackathon_2_eda_sigwatch.ipynb          # EDA on NGO campaign data
├── Hackathon_3_edaBanks_task4_5_6.ipynb    # CAPM estimation, CAR computation, statistical testing
├── banks_data_bocconi/                     # Stock price and return datasets
├── sigwatch_data/                          # NGO campaign data
├── events_date_ngos_company_wide.csv       # Cleaned campaign dataset (generated in EDA)
├── merged_dataset.csv                      # Final merged dataset (events + financial data)
├── gdelt_event_metrics.csv                 # Media-related dataset
├── gdelt_raw_hits.csv                      # Raw GDELT event data
├── example_name_cleaning.txt               # Cleaning reference file
├── Group_2_Hackathon_presentation.pptx     # Final presentation slides
└── README.md                               # Project documentation
```

Note:  
`merged_dataset.csv` allows replication of the final analysis without re-running the full merge procedure.

---

## Data

- Sigwatch NGO campaign data (targeted firms, dates, sentiment, prominence, NGO power)  
- Bank stock prices and returns (Datastream-style data)  
- Market returns and risk-free rates  
- Optional media coverage data (GDELT)  

We focused on banks in the US, UK, and EU.  
Campaigns were classified by sentiment (positive/negative) and other attributes such as prominence.

---

## Methods

- Exploratory data analysis of NGO campaigns (volume, sentiment distribution, targeted firms)  
- Cleaning and structuring campaign event dates  
- Estimation of CAPM (and extended factor model) parameters over rolling windows  
- Event-study methodology:

  1. Estimate expected return using CAPM:
     
     \[
     r_{i,t} = \alpha_i + \beta_i (r_{m,t} - r_{f,t}) + \varepsilon_{i,t}
     \]

  2. Compute abnormal returns:
     
     \[
     AR_{i,t} = r_{i,t} - \hat{r}_{i,t}
     \]

  3. Compute cumulative abnormal returns (CAR):
     
     \[
     CAR_{i} = \sum_{t \in [t_s - 10, t_s + 10]} AR_{i,t}
     \]

- Merging campaign dates with financial return data  
- Statistical testing of CARs across event types  
- Subsample analysis (e.g., by sentiment or prominence)  

---

## Results

- Computation of CARs around NGO campaign dates  
- Evidence that negative campaigns tend to generate stronger market reactions than positive ones  
- Variation in impact depending on campaign prominence and sentiment  
- Cross-country heterogeneity in reactions (US vs EU/UK banks)  

The findings suggest that ESG-related information and NGO campaigns can influence financial markets, consistent with the literature on CSR news and shareholder value.

---

## Key Learnings

- Event-study methodology is a powerful tool to measure market reactions  
- ESG shocks can carry economically meaningful information  
- Data cleaning and merging across heterogeneous sources is critical  
- Market reactions depend on the informational content and perceived credibility of campaigns  

---

## Team

This project was developed for the course **Finance with Big Data** – Bocconi University

**Team Members:**
- Luca Milani  
- Marta Laskowska  
- Monika Kaczorowska  

---

## Financial Interpretation

This project connects sustainable finance and traditional asset pricing by studying how markets respond to ESG-related shocks.  
It provides empirical evidence on whether NGO press campaigns affect shareholder value and highlights the growing relevance of non-financial information in capital markets.

The Hackathon illustrates how ESG, media pressure, and responsible investment interact with market efficiency and investor behavior.