# Do FinTechs Discriminate?  
### Financial Consumer Complaints and Demographic Disparities in the U.S.
Bocconi University  
December 2025  

---

## Overview

This project investigates whether the quality of financial services differs across neighborhoods with different demographic characteristics and whether FinTech companies behave differently from traditional financial institutions.

Using **11.7 million CFPB consumer complaints (2011–2025)** merged with **U.S. Census demographic data at the ZIP code level**, we examine whether complaint rates are systematically related to:

- Minority share  
- Income  
- Education  
- Firm type (FinTech vs. non-FinTech)

The central research question:

> **Do FinTech firms reduce or amplify disparities in financial service quality across minority and low-income neighborhoods?**

Our empirical strategy builds on Begley & Purnanandam (2021) and Bartlett et al. (2022), extending their insights using complaint-level data rather than pricing data.

---

## Research Motivation

Prior literature finds:

- Higher minority-share neighborhoods experience significantly more complaints (Begley & Purnanandam, 2021).
- Algorithmic lending (FinTech) may reduce discrimination relative to traditional lenders (Bartlett et al., 2022).

We contribute by:

1. Measuring **service quality via complaint intensity**
2. Comparing **FinTech vs. traditional institutions**
3. Testing whether FinTech mitigates or reinforces disparities
4. Exploring whether AI adoption (GPT-3 shock in June 2020) altered complaint dynamics

---

## Data

### 1. CFPB Consumer Complaints
- 11.7 million complaints (2011–2025)
- Information on:
  - Company
  - Product
  - Issue
  - ZIP code
  - Date
  - Narrative text (29% include narratives)

### 2. U.S. Census (2020)
Merged at ZIP Code Tabulation Area (ZCTA) level:

- **P3** – Population by race (minority share)
- **S1901** – Income (mean & median household income)
- **S1501** – Education attainment

### 3. Firm Classification
- Manual classification of institutions into:
  - **FinTech**
  - **Non-FinTech**
- Based on business model and digital orientation

---

## Project Structure

```
# Notebooks
├── EDA_census.ipynb
├── EDA_complaints.ipynb
├── eda_census_and_complaints.ipynb
├── data_modelling.ipynb
├── 2nd_data_modelling.ipynb

# Input Data
├── 2020_census_P3.csv
├── 2020_census_S1901.csv
├── 2020_census_S1501.csv
├── complaints.csv
├── ai_adoption.xlsx

# Output Data
├── all_census_data.csv
├── NLP_processed_complaints.csv
├── merged_aggregated.csv
├── new_merged_aggregated.csv
```

Note: Some large files are excluded from GitHub due to size constraints.

---

## Exploratory Data Analysis

### Census Insights

- Income and education are strongly correlated.
- Minority share varies significantly across ZIP codes.
- Higher income ZIP codes tend to have higher education levels.

### CFPB Insights

- Complaint volume increased substantially over time.
- A small number of large institutions account for a large share of complaints.
- Complaint narratives are overwhelmingly negative (aligned with the nature of complaints).

Demographic quintiles were constructed for:
- Minority share
- Income
- Education

---

## Econometric Framework

### Baseline Specification (OLS)

We estimate models of the form:

\[
\log(\text{Complaints}_{i,z,t}) = \beta_0 
+ \text{Demographic Quintiles}_{z}
+ \text{FinTech}_i
+ \text{Interactions}
+ \text{Fixed Effects}
+ \varepsilon_{i,z,t}
\]

Baseline group:
- Non-FinTech firms
- High-minority ZIP codes
- Lowest income and education quintiles

We estimate four model families:
1. Minority-only specification  
2. Income-only specification  
3. Education-only specification  
4. Full model (all demographics + interactions)

Multicollinearity was tested using:
- Cramer’s V
- Variance Inflation Factor (VIF)

Most variables had VIF < 10.

---

## Main Results (OLS)

### 1. Minority Share

- Lower minority-share ZIP codes file **substantially fewer complaints**.
- Minority share is the strongest demographic predictor.

### 2. Income

- Higher-income ZIP codes file fewer complaints.
- Income effects are statistically robust.

### 3. Education

- Higher education levels are associated with fewer complaints.
- Effects smaller than minority and income variables.

### 4. FinTech vs Non-FinTech

- FinTech firms receive **fewer complaints overall**.
- However, this advantage **weakens in the highest-minority ZIP codes**.
- Disparities remain present in high-minority areas.

---

## Diff-in-Diff: GPT-3 Shock (June 2020)

To test whether AI adoption changed complaint dynamics, we implement:

\[
\log(\text{Complaints}) = \beta_0 
+ FE_{\text{Month}} 
+ FE_{\text{Firm}} 
+ \beta_1(\text{FinTech} \times \text{Post})
\]

Findings:

- No statistically significant post-GPT divergence.
- Event study confirms no strong structural break.

Conclusion:
> The relative complaint gap between FinTech and traditional institutions does not materially change after GPT-3.

---

## Interpretation

Our findings align with prior literature:

- High-minority geographies experience worse outcomes.
- FinTech firms reduce overall complaints.
- However, FinTech does **not eliminate disparities** in the most minority-dense neighborhoods.

Compared to Bartlett et al. (2022):
- We confirm modest improvement from FinTech.
- But geographic disparities persist.

---

## Limitations

1. Manual classification of FinTech vs non-FinTech
2. ZIP codes used as proxies for individual characteristics
3. Not all companies in CFPB data are banks
4. Complaints measure perceived service quality, not pricing discrimination
5. Potential measurement error in complaint reporting intensity

---

## Key Contributions

- Merges large-scale complaints data with Census demographics.
- Provides ZIP-level evidence of demographic disparities.
- Extends discrimination analysis beyond pricing to service quality.
- Tests AI adoption shock using quasi-experimental framework.

---

## Conclusion

FinTech firms appear to reduce overall complaint intensity, suggesting improved service efficiency or transparency. However:

- Minority-dense ZIP codes still face disproportionately high complaint rates.
- FinTech does not fully close demographic gaps in service outcomes.
- Structural inequalities in financial service provision remain visible.

The evidence suggests:
> Technology may improve efficiency, but it does not automatically eliminate geographic or demographic disparities.

---

## Team

Finance with Big Data – Bocconi University  

- Luca Milani  
- Marta Laskowska  
- Monika Kaczorowska  
