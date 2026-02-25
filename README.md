# Finance with Big Data  
### Bocconi University – Master in Data Science and Business Analytics  

This repository collects the projects developed for the course **Finance with Big Data** at Bocconi University.

The course combines financial economics, econometrics, and machine learning with large-scale datasets and alternative data sources.  
Projects span classical portfolio theory, asset pricing models, NLP-based factor construction, ESG event studies, and machine learning-driven trading strategies.

---

## Repository Structure

```
Finance_with_Big_Data/
│
├── PC_Lab_1/          # Applied Portfolio Theory
├── PC_Lab_2/          # CAPM Empirical Testing
├── PC_Lab_3/          # NLP & Alternative Data Factor
├── PC_Lab_4/          # Machine Learning Return Prediction
├── Hackathon/         # ESG Event Study & NGO Campaigns
└── Final_Project/     # FinTech Discrimination Analysis
```

Each folder contains:
- Jupyter notebooks
- Processed datasets (when size allows)
- A dedicated README explaining methodology and results

---

# Course Projects Overview

## PC Lab 1 – Applied Portfolio Theory

Implementation of **Markowitz mean–variance optimization** using S&P 500 stock data.

Main components:
- Return computation and correlation analysis
- Efficient frontier construction
- Tangency portfolio identification
- Out-of-sample performance testing

Focus:  
Understanding the practical limitations of classical portfolio theory when applied to real-world data.

---

## PC Lab 2 – Applying the CAPM

Empirical estimation of the **Capital Asset Pricing Model (CAPM)**.

Main components:
- OLS estimation of alpha and beta
- Statistical significance testing
- Portfolio construction based on systematic risk
- Evaluation of CAPM predictions

Focus:  
Testing whether systematic risk explains realized returns in practice.

---

## PC Lab 3 – Creating a Factor from Text Data

Construction of a **Twitter-based sentiment and media attention factor**.

Main components:
- Financial tweet preprocessing
- Sentiment classification using NLP models
- Portfolio formation based on attention measures
- Optional risk-adjusted analysis using Fama–French 5 factors

Focus:  
Evaluating whether alternative data sources contain predictive financial signals.

---

## PC Lab 4 – Predicting Stock Returns with Machine Learning

Application of machine learning models to predict daily stock returns.

Main components:
- Feature engineering using prices and volumes
- OLS vs Ridge regression
- Neural networks and tree-based methods
- Out-of-sample evaluation (ROOS)
- AI-driven portfolio construction
- Transaction cost analysis

Focus:  
Distinguishing statistical predictability from economic profitability.

---

## Hackathon – NGO Press Campaigns and Responsible Investment

Research-style project applying **event-study methodology** to ESG-related shocks.

Main components:
- CAPM estimation
- Abnormal return calculation
- Cumulative abnormal returns (CAR)
- Cross-country comparison
- Statistical testing of NGO campaign effects

Focus:  
Understanding how markets react to ESG news and media pressure.

---

# Final Project  
## Do FinTechs Discriminate?

### Financial Consumer Complaints and Demographic Disparities in the U.S.

The final project investigates whether FinTech companies reduce or amplify disparities in financial service quality across neighborhoods.

Using:
- **11.7 million CFPB complaints (2011–2025)**
- **U.S. Census demographic data (ZIP-level)**

We analyze whether complaint intensity varies by:
- Minority share
- Income
- Education
- Firm type (FinTech vs non-FinTech)

### Methodology
- ZIP-level demographic merging
- OLS regressions with interaction terms
- Multicollinearity diagnostics (VIF)
- Difference-in-differences (GPT-3 shock, June 2020)
- Event-study validation

### Main Findings
- Minority share is the strongest predictor of complaint intensity.
- Higher-income and higher-education ZIP codes file fewer complaints.
- FinTech firms receive fewer complaints overall.
- However, FinTech advantages weaken in the highest-minority neighborhoods.
- No structural break after GPT-3 adoption.

Conclusion:
> Technology may improve efficiency, but it does not automatically eliminate demographic disparities.

---


# Team

Projects developed for **Finance with Big Data – Bocconi University**

- Luca Milani  
- Marta Laskowska  
- Monika Kaczorowska  

---

# Final Remarks

This repository represents a structured portfolio of applied quantitative finance projects combining:

- Theory
- Data
- Econometrics
- Machine Learning
- ESG and Alternative Data

The progression of projects reflects the course trajectory:
from classical asset pricing to modern AI-driven financial analysis.