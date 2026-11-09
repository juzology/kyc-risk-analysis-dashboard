# kyc-risk-analysis-dashboard
Interactive KYC risk analysis dashboard built with Microsoft Excel, Power Pivot, DAX and a Python generated synthetic data.

# Project Overview
This project presents an interactive Know Your Customer (KYC) and AML/CTF Compliance Risk Analysis Dashboard developed using Microsoft Excel. The dashboard is designed to support the analysis of customer and entity-level compliance risk by bringing together multiple indicators, including PEP status, sanctions exposure, adverse media, high-risk jurisdictions, and overall risk scoring. The project demonstrates how structured KYC data can be transformed into an interactive analytical tool for identifying risk patterns and supporting compliance-focused decision-making.

# Project Objectives
The main objectives of this project were to: Analyze KYC and compliance-related entity information. Identify entities associated with elevated risk indicators. Examine adverse media trends. Analyze geographic/high-risk jurisdiction exposure. Develop a structured entity risk-scoring approach. Build an interactive Excel dashboard for compliance analysis. Enable both entity-level and geographic-level analysis through interactive filtering.

# Dataset
The project uses a synthetic KYC dataset generated using Python's Faker library. The dataset was created specifically for educational and portfolio purposes and does not contain real customer or confidential information. The synthetic data was structured to simulate a realistic KYC/compliance environment containing information relevant to: Entities and customers PEP indicators Sanctions indicators Adverse media High-risk jurisdictions Geographic information Sanctions sources and restriction types

# Charts Overview
The analysis contains:

A Gauge Chart for displaying the entity risk score and accompanied with several measure such as the Entity name, Risk Levels, Sanctions, PEP and Adverse Media count to give a holistic view to the customer risk profile

A Doughnut Chart displaying the different entity types between corporate and individuals.

A Stacked Column chart for displaying the several risk factors such as Sanctions, PEP, Adverse Media, High Risk Country and High Risk Business used in the analysis

A Horizontal Bar Chart for displaying Adverse Media Information or financial crime trends across the client base

A Line Chart with markers for displaying the ID expiry date and Next Review Date of customer profiles

# Tools & Technologies
Microsoft Excel, Power Pivot, DAX, Pivot Tables, Slicers, Timelines and Data Visualization, and Python to generate the synthetic dataset

# Data Analysis & Methodology
The project follows a structured analytical workflow: Synthetic Data Generation, Data Preparation & Cleaning, Data Modelling, Risk Indicator Analysis, Risk Scoring, Pivot-Based Analysis, Interactive Dashboard, Insights and Interpretation. The analysis combines multiple compliance indicators to provide a broader view of entity risk rather than relying on a single risk factor.

# Risk Analysis
The dashboard incorporates multiple risk indicators, including: PEP Risk Sanctions Risk Adverse Media Geographic / High-Risk Jurisdiction Analysis High Risk Industry / Business

# Interactive Dashboard
The dashboard provides three complementary analytical perspectives.

# Entity-Level Risk Assessment
An Entity slicer allows the user to select an individual entity. The selected entity is then reflected in the risk-analysis section, including: Entity name Risk level Risk score Related compliance indicators A gauge-style visualization is used to communicate the selected entity's risk score.

# Geographic-Level Analysis
A separate geographic/country slicer enables broader analysis across jurisdictions. This allows users to investigate how sanctions, PEP, adverse media, and other indicators vary geographically. The geographic filtering is intentionally used for the analytical charts rather than the individual entity risk gauge.

# Timeline Analysis
A timeline which enables time specific analysis across the dataset which can be especially useful during audit reviews, allowing us to access the customers risk profiles over a given period of time.

# Technical Skills Demonstrated
This project demonstrates practical application of: Data cleaning and preparation, Data analysis, Data modelling, Microsoft Excel, Power Pivot, DAX, Pivot Tables, Interactive slicers, Risk scoring, Compliance analytics, KYC analysis, Sanctions analysis, PEP analysis, Geographic analysis, Dashboard development, Data visualization and Analytical storytelling.

```kyc-risk-analysis-dashboard/
│
├── README.md
│
├── python/
│   └── generate_kyc_data.py
│
├── excel/
│   └── Synthetic_KYC_Dataset.xlsx
│
├── screenshots/
    ├── Dashboard.png
    ├── Entity_Level_Analysis.png
    ├── Geographic_Level_Analysis.png
    └── Timeline_Analysis.png
```
# Limitations
This project is a portfolio demonstration and is based on synthetic data. The risk-scoring methodology is designed to demonstrate analytical and dashboard-development techniques and should not be interpreted as a production-ready AML/KYC risk model. Real-world compliance environments would require additional considerations, including regulatory requirements, institution-specific risk policies, data-quality controls, screening methodologies, model validation, and ongoing monitoring.

# Disclaimer
This project is intended strictly for educational and portfolio purposes. All customer/entity records are synthetic. No real customer, personal, or confidential KYC information is included in the project. The dashboard and risk methodology are illustrative and should not be considered a substitute for an organization's formal AML/KYC compliance framework.
