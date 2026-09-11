#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import pandas as pd
from faker import Faker

fake = Faker()

# --- Sheet 1: Corporate ---
def generate_corporate_data(n=300):
    corporates = []
    for i in range(1, n+1):
        corporates.append({
            "Corporate_ID": f"COR-{i:04d}",
            "Corporate Name": fake.company(),
            "Country": fake.country(),
            "Nature of Business": random.choice(["Retail", "Manufacturing", "Technology", "Defense"]),
            "RC Number": f"RC-{random.randint(1000,99999)}",
            "Date of Incorporation": fake.date_between(start_date="-15y", end_date="today").strftime("%d/%m/%y"),
            "Date Added": fake.date_between(start_date="-10y", end_date="today").strftime("%d/%m/%y"),
            "Date of Last Review": fake.date_between(start_date="-5y", end_date="today").strftime("%d/%m/%y"),
            "Adverse Media": random.choice(["Y", "N"]),
            "PEP": random.choice(["Y", "N"]),
            "Sanctions": random.choice(["Y", "N"])
        })
    return pd.DataFrame(corporates)

# --- Sheet 2: Individual ---
def generate_individual_data(n=200):
    id_types = ["Passport", "Driver’s License", "National ID"]
    individuals = []
    for i in range(1, n+1):
        individuals.append({
            "Individual_ID": f"IND-{i:04d}",
            "Individual Name": fake.name(),
            "Country": fake.country(),
            "Last Means of ID": random.choice(id_types),
            "ID Number": f"{fake.random_uppercase_letter()}{fake.random_uppercase_letter()}-{random.randint(10000,99999)}",
            "Date of Expiry": fake.date_between(start_date="-5y", end_date="today").strftime("%d/%m/%y"),
            "Date Added": fake.date_between(start_date="-10y", end_date="today").strftime("%d/%m/%y"),
            "Date of Last Review": fake.date_between(start_date="-5y", end_date="today").strftime("%d/%m/%y"),
            "Adverse Media": random.choice(["Y", "N"]),
            "PEP": random.choice(["Y", "N"]),
            "Sanctions": random.choice(["Y", "N"])
        })
    return pd.DataFrame(individuals)

# --- Sheet 3: Sanctions ---
def generate_sanctions_data(corporates, n=50):
    sanctions = []
    sanctioning_bodies = ["EU", "OFAC", "UK Treasury", "UN"]
    sanction_types = ["Asset Freeze", "Financial Restriction", "Arms Embargo", "Travel Ban"]

    sanctioned_names = random.sample(list(corporates["Corporate Name"]), n)

    for i, corp_name in enumerate(sanctioned_names, start=1):
        sanctions.append({
            "Sanction_ID": f"SAN-{i:04d}",
            "Entity Name": corp_name,
            "Entity Type": "Corporate",
            "Country": fake.country(),
            "Sanctioning Body": random.choice(sanctioning_bodies),
            "Sanction Type": random.choice(sanction_types),
            "Date Added": random.randint(42000,46000),  # Excel-style serial dates
            "Date of Last Review": random.randint(42000,46000),
            "Date of Removal": random.choice(["Still Listed", random.randint(42000,46000)])
        })
    return pd.DataFrame(sanctions)

# --- Sheet 4: PEP ---
def generate_pep_data(corporates, n=100):
    pep = []
    for i in range(1, n+1):
        corp_name = random.choice(corporates["Corporate Name"])
        pep.append({
            "PEP_ID": f"PEP-{i:04d}",
            "Entity Name": corp_name,
            "Entity Type": "Corporate",
            "Country": fake.country(),
            "Position / Role": random.choice(["Minister", "Parliament Member", "Governor", "Mayor"]),
            "Date of Assuming Office": random.randint(42000,46000),
            "Date of Leaving Office": random.choice([random.randint(42000,46000), "Present"]),
            "Date Added": random.randint(42000,46000),
            "Date of Last Review": random.randint(42000,46000)
        })
    return pd.DataFrame(pep)

# --- Sheet 5: Adverse Media ---
def generate_adverse_media_data(corporates, n=100):
    media_sources = ["Reuters", "BBC", "Bloomberg", "Al Jazeera", "Financial Times"]
    issues = ["Sanctions Evasion", "Fraud", "Money Laundering", "Corruption"]
    media = []
    for i in range(1, n+1):
        corp_name = random.choice(corporates["Corporate Name"])
        media.append({
            "Media_ID": f"MED-{i:04d}",
            "Entity Name": corp_name,
            "Entity Type": "Corporate",
            "Country": fake.country(),
            "Media Source": random.choice(media_sources),
            "Issue / Allegation": random.choice(issues),
            "Date Added": fake.date_between(start_date="-10y", end_date="today").strftime("%d/%m/%y"),
            "Date of Last Review": fake.date_between(start_date="-5y", end_date="today").strftime("%d/%m/%y")
        })
    return pd.DataFrame(media)

# --- Sheet 6: High Risk Country ---
def generate_high_risk_country_data(n=50):
    reasons = ["Political Instability", "Sanctions Evasion", "Civil Unrest", "Terrorism Risk"]
    risk_levels = ["Critical", "High", "Medium", "Low"]
    hrj = []
    for i in range(1, n+1):
        hrj.append({
            "HRJ_ID": f"HRJ-{i:04d}",
            "Country": fake.country(),
            "Risk Level": random.choice(risk_levels),
            "Reason / Notes": random.choice(reasons),
            "Date Added": fake.date_between(start_date="-10y", end_date="today").strftime("%d/%m/%y"),
            "Date of Last Review": fake.date_between(start_date="-5y", end_date="today").strftime("%d/%m/%y")
        })
    return pd.DataFrame(hrj)

# --- Generate Workbook ---
corporates_df = generate_corporate_data(300)
individuals_df = generate_individual_data(200)
sanctions_df = generate_sanctions_data(corporates_df, 50)
pep_df = generate_pep_data(corporates_df, 100)
media_df = generate_adverse_media_data(corporates_df, 100)
hrj_df = generate_high_risk_country_data(50)

with pd.ExcelWriter("Compliance_Workbook_Fake.xlsx") as writer:
    corporates_df.to_excel(writer, sheet_name="Corporate", index=False)
    individuals_df.to_excel(writer, sheet_name="Individual", index=False)
    sanctions_df.to_excel(writer, sheet_name="Sanctions", index=False)
    pep_df.to_excel(writer, sheet_name="PEP", index=False)
    media_df.to_excel(writer, sheet_name="AdverseMedia", index=False)
    hrj_df.to_excel(writer, sheet_name="HighRiskCountry", index=False)

print("Workbook generated with 6 sheets: Compliance_Workbook_Fake.xlsx")


# In[ ]:




