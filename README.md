# kyc-risk-analysis-dashboard
Interactive KYC risk analysis dashboard built with Microsoft Excel, Power Pivot, DAX and a Python generated synthetic data.

# Project Overview
This project presents an interactive Know Your Customer (KYC) and AML/CTF Compliance Risk Analysis Dashboard developed using Microsoft Excel.
The dashboard is designed to support the analysis of customer and entity-level compliance risk by bringing together multiple indicators, including PEP status, sanctions exposure, adverse media, high-risk jurisdictions, and overall risk scoring.
The project demonstrates how structured KYC data can be transformed into an interactive analytical tool for identifying risk patterns and supporting compliance-focused decision-making.

# Project Objectives
The main objectives of this project were to:
Analyze KYC and compliance-related entity information.
Identify entities associated with elevated risk indicators.
Analyze Politically Exposed Person (PEP) exposure.
Analyze sanctions exposure across different sanctions lists.
Examine adverse media indicators.
Analyze geographic/high-risk jurisdiction exposure.
Develop a structured entity risk-scoring approach.
Build an interactive Excel dashboard for compliance analysis.
Enable both entity-level and geographic-level analysis through interactive filtering.

# Dataset
The project uses a synthetic KYC dataset generated using Python's Faker library.
The dataset was created specifically for educational and portfolio purposes and does not contain real customer or confidential information.
The synthetic data was structured to simulate a realistic KYC/compliance environment containing information relevant to:
Entities and customers
PEP indicators
Sanctions indicators
Adverse media
High-risk jurisdictions
Risk levels
Risk scores
Geographic information
Sanctions sources and restriction types

# Dataset Overview
The analysis contains:
Metric
Count
Total entities
650
Adverse media records
214
PEP records
189
Sanctions records
177
High-risk jurisdiction records
216
Average risk score
43.62
These figures are based on the current dashboard data and are used to demonstrate the analytical capabilities of the project.

# Tools & Technologies
# Primary Tools
Microsoft Excel, Power Pivot, DAX, Pivot Tables, Slicers and Data Visualization
# Supporting Technology
Python, Faker and Jupyter Notebook. Python/Faker was used to generate the synthetic dataset, while the primary analytical and dashboard work was performed in Excel.

# Data Analysis & Methodology
The project follows a structured analytical workflow:
Synthetic Data Generation, Data Preparation & Cleaning, Data Modelling, Risk Indicator Analysis, Risk Scoring, Pivot-Based Analysis, Interactive Dashboard, Insights and Interpretation. The analysis combines multiple compliance indicators to provide a broader view of entity risk rather than relying on a single risk factor.

# Risk Analysis
The dashboard incorporates multiple risk indicators, including:
PEP Risk
The dashboard identifies entities associated with Politically Exposed Person indicators and the date(year) of assuming position.
PEP categories represented in the analysis include:
Ambassador
Governor
Minister
Parliament Member
A total of 189 PEP records are represented in the current dataset.
Sanctions Risk
The sanctions analysis contains 177 records across multiple sanctions sources, including:
EU
OFAC
UK Treasury
UN
The dashboard also analyzes different sanctions restriction types, including:
Arms Embargo
Asset Freeze
Financial Restriction
Travel Ban
Adverse Media
The dashboard identifies entities associated with adverse media indicators and provides an overall adverse-media count and rate.
The current dataset contains 214 adverse media records.
The analysis also considers different adverse-media themes, including:
Bribery
Corruption
Fraud
Money Laundering
Sanctions Evasion
Terror Financing
Geographic / High-Risk Jurisdiction Analysis
Geographic filtering allows users to examine compliance indicators by country.
The geographic analysis can be used to explore:
Concentration of risk by country
High-risk jurisdiction exposure
Sanctions exposure by geography
PEP exposure by geography
Distribution of compliance indicators across jurisdictions

# Interactive Dashboard
The dashboard provides two complementary analytical perspectives.
# Entity-Level Risk Assessment
An Entity slicer allows the user to select an individual entity.
The selected entity is then reflected in the risk-analysis section, including:
Entity name
Risk level
Risk score
Related compliance indicators
A gauge-style visualization is used to communicate the selected entity's risk score.
# Geographic & Compliance Analysis
A separate geographic/country slicer enables broader analysis across jurisdictions.
This allows users to investigate how sanctions, PEP, adverse media, and other indicators vary geographically.
The geographic filtering is intentionally used for the analytical charts rather than the individual entity risk gauge.

# Key Findings
The current analysis provides several high-level observations:
The dataset contains 650 entities, providing a sufficiently varied synthetic population for demonstrating KYC analysis techniques.
189 PEP records are represented across several PEP categories.
177 sanctions records are distributed across EU, OFAC, UK Treasury, and UN sanctions sources.
Sanctions restrictions include arms embargoes, asset freezes, financial restrictions, and travel bans.
214 adverse media records are represented across themes such as corruption, fraud, money laundering, sanctions evasion, bribery, and terror financing.
216 high-risk jurisdiction records are represented in the dataset.
The overall average risk score is approximately 43.62, providing a portfolio-level view of the simulated entity risk environment.
Interactive entity and geographic filtering allows users to move between individual entity assessment and broader compliance analysis.

# Technical Skills Demonstrated
This project demonstrates practical application of:
Data cleaning and preparation, Data analysis, Data modelling, Microsoft Excel, Power Pivot, DAX, Pivot Tables, Interactive slicers, Risk scoring, Compliance analytics, KYC analysis, Sanctions analysis, PEP analysis, Geographic analysis, Dashboard development, Data visualization and Analytical storytelling

# Project Structure
```kyc-risk-analysis-dashboard/
│
├── README.md
│
├── excel/
│   └──KYC_Risk_Analysis_Dashboard.xlsx
│   └── Synthetic_KYC_Dataset.xlsx
│
├── python/
│   ├── generate_kyc_data.py
│   └── generated_kyc_data.ipynb
│
├── screenshots/
    ├── Dashboard.png
    ├── Entity_Level_Analysis.png
    └── Geographic_Compliance.png
```
# Limitations
This project is a portfolio demonstration and is based on synthetic data.
The risk-scoring methodology is designed to demonstrate analytical and dashboard-development techniques and should not be interpreted as a production-ready AML/KYC risk model.
Real-world compliance environments would require additional considerations, including regulatory requirements, institution-specific risk policies, data-quality controls, screening methodologies, model validation, and ongoing monitoring.

# Disclaimer
This project is intended strictly for educational and portfolio purposes.
All customer/entity records are synthetic. No real customer, personal, or confidential KYC information is included in the project.
The dashboard and risk methodology are illustrative and should not be considered a substitute for an organization's formal AML/KYC compliance framework.
