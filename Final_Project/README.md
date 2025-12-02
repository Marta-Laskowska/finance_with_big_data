# Financial Consumer Complaints Analysis

Analysis of CFPB consumer complaints data merged with U.S. Census demographic data to identify patterns and disparities in financial services across different demographics and ZIP codes.

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
├── companies.csv
├── companies2.csv
├── NLP_processed_complaints.csv
├── merged_aggregated.csv
└── new_merged_aggregated.csv
```

## Notebooks

### 1. EDA_census.ipynb
Exploratory analysis of 2020 Census demographic datasets:
- P3 - Population by race
- S1901 - Household income (mean, median income in last 12 months)
- S1501 - Education attainment (percent with high school, college, graduate degree)

**Outputs:** `all_census_data.csv`

### 2. EDA_complaints.ipynb
Exploratory analysis of CFPB complaints data. Analyzes complaint patterns by product, company, and geography. Performs NLP processing on complaint narratives including sentiment analysis.

**Outputs:** `NLP_processed_complaints.csv`

### 3. eda_census_and_complaints.ipynb
Merges census and complaints data on ZIP codes. Filters out credit bureau complaints, creates demographic quintile classifications, and aggregates by ZCTA and company.

**Outputs:** `merged_aggregated.csv` (used in first modelling notebook), `new_merged_aggregated.csv` (used in second modelling notebook)

### 4. data_modelling.ipynb
Initial modeling of demographics and complaint patterns. Includes regressions and Diff in Diff analysis.


### 5. 2nd_data_modelling.ipynb
Second modeling file with professor's feedback incorporated. Includes regression analysis of the 4 model families, VIF diagnostics, and linear combination analysis.


## Data Input Files

**Input Files:**
- `2020_census_P3.csv` - Census population and race data by ZCTA
- `2020_census_S1501.csv` - Census population and education data by ZCTA
- `2020_census_S1901.csv` - Census population and income data by ZCTA
- `complaints.csv` - Consumer complaints downloaded from CFPB database
- `ai_adoption.xlsx` - Company fintech classification created manually
