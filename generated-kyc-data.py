import random
from datetime import date, timedelta

import pandas as pd
from faker import Faker

# Same seed = same data every run (change the number for a different set)
SEED = 42
random.seed(SEED)
Faker.seed(SEED)
fake = Faker()

TODAY = date.today()

# A fixed list of countries so the sheets actually overlap and can be cross-checked
COUNTRIES = [
    "Nigeria", "Ghana", "Kenya", "South Africa", "Egypt", "United Kingdom",
    "United States", "Canada", "Germany", "France", "India", "China",
    "United Arab Emirates", "Russia", "Iran", "North Korea", "Syria", "Myanmar",
    "Venezuela", "Cuba", "Afghanistan", "Libya", "Yemen", "Sudan", "Somalia",
    "Pakistan", "Turkey", "Brazil", "Mexico", "Singapore", "Switzerland",
    "Panama", "Cayman Islands", "Cyprus", "Lebanon", "Iraq", "Belarus",
    "Ukraine", "Japan", "Australia",
]

def rand_date(start, end):
    """Random date between two dates (start and end included)."""
    if end < start:
        end = start
    return start + timedelta(days=random.randint(0, (end - start).days))

def years_ago(n):
    return TODAY - timedelta(days=int(365.25 * n))

def added_and_review(earliest):
    """Date Added is never before `earliest`; Last Review is never before Date Added."""
    added = rand_date(max(earliest, years_ago(10)), TODAY)
    review = rand_date(added, TODAY)
    return added, review


# Nature of business - big list so the corporate sample is varied
NATURE_OF_BUSINESS = [
    "Retail", "Manufacturing", "Technology", "Defense & Arms",
    "Education", "Entertainment", "Financial Services",
    "Real Estate", "Construction", "Oil & Gas",
    "Mining & Metals", "Agriculture", "Food & Beverage", "Hospitality & Tourism",
    "Healthcare", "Pharmaceuticals", "Telecommunications", "Transportation & Logistics",
    "Shipping & Maritime", "Aviation", "Automotive", "Fashion & Apparel", "Cosmetics & Beauty", "Gaming & Gambling",
    "Foreign Exchange Bureau", "Legal Services", "Accounting & Audit", "Management Consulting",
    "Advertising & Marketing", "Publishing & Printing", "Sports & Recreation", "Non-Profit / NGO",
    "Religious Organisation", "Art, Antiques & Auctions", "Jewellery & Precious Metals", "Waste Management", 
    "Security Services", "Alcohol & Tobacco"
]

# How an individual can be tied to a corporate entity
ASSOCIATIONS = ["Signatory", "Director", "Trustee", "Beneficial Owner"]

# =====================================================
# NAME GENERATION - one shared "used names" set for BOTH sheets
# =====================================================
import re

USED_NAMES = set()          # every name handed out (individual OR corporate) lives here

def _norm(name):
    """Lower-case, letters/digits only - so 'Smith & Sons Ltd.' and 'smith sons ltd' count as the same."""
    return re.sub(r"[^a-z0-9]", "", name.lower())

# Words that only a company would have. Individuals must NEVER contain these.
CORPORATE_TOKENS = {
    "ltd", "limited", "llc", "inc", "incorporated", "plc", "corp", "corporation", "co",
    "group", "holdings", "sons", "partners", "enterprises", "industries", "international",
    "global", "solutions", "services", "trading", "ventures", "capital", "associates",
    "bros", "brothers", "company", "gmbh", "sa", "ag", "nv", "llp", "lp",
}

def looks_corporate(name):
    words = re.findall(r"[a-z]+", name.lower())
    return any(w in CORPORATE_TOKENS for w in words)

CORP_SUFFIXES = ["Ltd", "Limited", "LLC", "Inc.", "PLC", "Corp.", "Group", "Holdings",
                 "& Sons", "Co.", "Partners", "Enterprises", "Industries", "International",
                 "Global", "Solutions", "Services", "Trading", "Ventures", "Capital"]

CORP_WORDS = ["Apex", "Summit", "Pinnacle", "Horizon", "Meridian", "Vanguard", "Sterling",
              "Crestview", "Bluewater", "Ironbridge", "Goldleaf", "Northgate", "Silverline",
              "Redwood", "Oakmont", "Falcon", "Evergreen", "Stonebridge", "Riverstone",
              "Westfield", "Eastbrook", "Lakeshore", "Highland", "Cornerstone", "Keystone",
              "Atlas", "Orion", "Phoenix", "Titan", "Zenith", "Prime", "United", "Premier",
              "Allied", "Global", "Pacific", "Atlantic", "Continental", "Royal", "Imperial"]

def unique_corporate_name():
    """Always looks like a company (ends in a company suffix) and is never reused."""
    while True:
        suffix = random.choice(CORP_SUFFIXES)
        pattern = random.randint(1, 4)
        if pattern == 1:
            name = f"{fake.last_name()} {suffix}"
        elif pattern == 2:
            name = f"{fake.last_name()} & {fake.last_name()} {suffix}"
        elif pattern == 3:
            name = f"{random.choice(CORP_WORDS)} {random.choice(CORP_WORDS)} {suffix}"
        else:
            name = f"{fake.last_name()} {random.choice(CORP_WORDS)} {suffix}"
        name = name.replace("& Sons Sons", "& Sons")
        if name.startswith(("& ",)) or name.count("&") > 1:
            continue
        key = _norm(name)
        if key not in USED_NAMES:
            USED_NAMES.add(key)
            return name

def unique_individual_name():
    """Plain 'First Last' - no Mr./Dr./Jr./MD, and nothing that looks like a company."""
    while True:
        name = f"{fake.first_name()} {fake.last_name()}"
        if looks_corporate(name):
            continue
        key = _norm(name)
        if key not in USED_NAMES:
            USED_NAMES.add(key)
            return name
# =====================================================
# MASTER SHEETS - built first. Every other sheet copies from these.
# =====================================================

# Legal-form words that are not counted when taking a company's initials
LEGAL_WORDS = {"ltd", "limited", "llc", "inc", "plc", "corp", "co"}

def corporate_email_part(name):
    """One-word company ('Doe Limited') -> full name 'doe'.
    Two or more words ('John Joe & Sons Limited') -> initials 'JJS'.
    '&', 'and' and legal-form words like Limited/Ltd are skipped."""
    words = [w for w in re.findall(r"[A-Za-z]+", name)
             if w.lower() not in LEGAL_WORDS and w.lower() != "and"]
    if len(words) == 1:
        return words[0]
    return "".join(w[0] for w in words)

# --- Sheet 1: Corporate ---
def generate_corporate_data(n=180):
    rows = []
    for i in range(1, n + 1):
        incorporated = rand_date(date(1990, 1, 1), years_ago(1))   # as far back as 1990
        added, review = added_and_review(incorporated)   # added AFTER incorporation
        rows.append({
            "Corporate_ID": f"COR-{i:04d}",
            "Corporate Name": unique_corporate_name(),   # looks like a company, never repeats
            "Country": random.choice(COUNTRIES),
            "Nature of Business": random.choice(NATURE_OF_BUSINESS),
            "RC Number": f"RC-{random.randint(100000, 999999)}",
            "Date of Incorporation": incorporated,
            "Date Added": added,
            "Date of Last Review": review,
        })
    return pd.DataFrame(rows)


# --- Sheet 2: Individual ---
ID_FORMATS = {
    "Passport":        lambda: f"{random.choice('ABCDEFGHJKLMNPRSTUVWXYZ')}{random.randint(10000000, 99999999)}",
    "Driver's License": lambda: f"DL-{random.randint(1000000, 9999999)}",
    "National ID":     lambda: f"{random.randint(10000000000, 99999999999)}",
}

def generate_individual_data(corporates, n=500):
    rows = []
    # first every corporate gets at least one individual, then the rest are spread randomly
    corp_ids = list(corporates.index)
    random.shuffle(corp_ids)
    assigned = corp_ids[:n] + [random.choice(corp_ids) for _ in range(max(0, n - len(corp_ids)))]
    for i in range(1, n + 1):
        id_type = random.choice(list(ID_FORMATS))
        added, review = added_and_review(years_ago(10))
        # ~85% of IDs are still valid, ~15% expired on purpose (good test cases)
        if random.random() < 0.85:
            expiry = rand_date(TODAY + timedelta(days=1), TODAY + timedelta(days=365 * 5))
        else:
            expiry = rand_date(years_ago(2), TODAY - timedelta(days=1))
        linked = corporates.loc[assigned[i - 1]]       # every individual is tied to one corporate
        name = unique_individual_name()                # plain First Last, never repeats
        first, last = name.split()
        # email = first initial + full last name @ company part + .com
        email = (f"{first[0]}{re.sub(r'[^A-Za-z]', '', last)}@"
                 f"{corporate_email_part(linked['Corporate Name'])}.com").lower()
        rows.append({
            "Individual_ID": f"IND-{i:04d}",
            "Individual Name": name,
            "Email": email,
            "Country": random.choice(COUNTRIES),
            "Linked Corporate_ID": linked["Corporate_ID"],
            "Linked Corporate Name": linked["Corporate Name"],
            "Association": random.choice(ASSOCIATIONS),
            "Last Means of ID": id_type,
            "ID Number": ID_FORMATS[id_type](),
            "Date of Expiry": expiry,
            "Date Added": added,
            "Date of Last Review": review,
        })
    return pd.DataFrame(rows)


USED_NAMES.clear()   # safe to re-run this cell
corporates_df = generate_corporate_data(180)
individuals_df = generate_individual_data(corporates_df, 500)
# =====================================================
# SCREENING SHEETS - names, IDs and countries are COPIED from the masters
# =====================================================

# --- Sheet 3: Sanctions (individuals AND corporates) ---
def generate_sanctions_data(individuals, corporates, n_ind=25, n_corp=25):
    bodies = ["EU", "OFAC", "UK Treasury", "UN"]
    types = ["Asset Freeze", "Financial Restriction", "Arms Embargo", "Travel Ban", "Trade Embargo", "Sectoral Sanctions"]

    picked = pd.concat([
        individuals.sample(n_ind, random_state=SEED).assign(
            Entity_ID=lambda d: d["Individual_ID"], Entity_Name=lambda d: d["Individual Name"], Entity_Type="Individual"),
        corporates.sample(n_corp, random_state=SEED).assign(
            Entity_ID=lambda d: d["Corporate_ID"], Entity_Name=lambda d: d["Corporate Name"], Entity_Type="Corporate"),
    ])

    rows = []
    for i, (_, r) in enumerate(picked.iterrows(), start=1):
        added, review = added_and_review(years_ago(10))
        removed = rand_date(added, TODAY) if random.random() < 0.2 else None   # ~20% delisted
        rows.append({
            "Sanction_ID": f"SAN-{i:04d}",
            "Entity_ID": r["Entity_ID"],
            "Entity Name": r["Entity_Name"],
            "Entity Type": r["Entity_Type"],
            "Country": r["Country"],                 # copied, not re-generated
            "Sanctioning Body": random.choice(bodies),
            "Sanction Type": random.choice(types),
            "Date Added": added,
            "Date of Last Review": review,
            "Date of Removal": removed,              # blank = still listed
            "Status": "Delisted" if removed else "Active",
        })
    return pd.DataFrame(rows)


# --- Sheet 4: PEP (people only - corporates are not PEPs) ---
def generate_pep_data(individuals, corporates, n=40):
    roles = ["Minister", "Parliament Member", "Governor", "Mayor"]
    picked = individuals.sample(n, random_state=SEED)
    rows = []
    for i, (_, r) in enumerate(picked.iterrows(), start=1):
        assumed = rand_date(years_ago(15), years_ago(1))
        left = rand_date(assumed, TODAY) if random.random() < 0.3 else None   # ~30% former PEPs
        rows.append({
            "PEP_ID": f"PEP-{i:04d}",
            "Entity_ID": r["Individual_ID"],
            "Entity Name": r["Individual Name"],
            "Entity Type": "Individual",
            "Country": r["Country"],
            "Position / Role": random.choice(roles),
            "Date of Assuming Office": assumed,
            "Date of Leaving Office": left,          # blank = still in office
            "Status": "Former" if left else "Current",
            "Linked Corporate_ID": r["Linked Corporate_ID"],        # copied from the Individual sheet
            "Linked Corporate Name": r["Linked Corporate Name"],
            "Association": r["Association"],
        })
    return pd.DataFrame(rows)


# --- Sheet 5: Adverse Media (individuals AND corporates) ---
def generate_adverse_media_data(individuals, corporates, n_ind=30, n_corp=30, extra=40):
    sources = ["Reuters", "BBC", "Bloomberg", "Al Jazeera", "Financial Times"]
    issues = [
        "Sanctions Evasion", "Fraud", "Money Laundering", "Corruption", "Bribery",
        "Embezzlement", "Tax Evasion", "Terrorism Financing", "Human Trafficking",
        "Drug Trafficking", "Arms Trafficking", "Insider Trading", "Market Manipulation",
        "Ponzi / Pyramid Scheme", "Cybercrime / Hacking", "Identity Theft", "Forgery",
        "Illegal Mining", "Environmental Violations", "Child Labour", "Human Rights Abuses",
        "Smuggling", "Organised Crime Links", "Racketeering", "Extortion",
        "Wildlife Trafficking", "Illegal Gambling", "Insider Dealing", "Misappropriation of Public Funds",
        "Fake Invoicing / Trade-Based Money Laundering", "Shell Company Abuse", "Regulatory Breach / Fine",
        "Accounting Irregularities", "Product Safety Violations", "Data Breach / Privacy Violation",
        "Antitrust / Price Fixing", "Kidnapping / Ransom", "Piracy", "Counterfeit Goods", "Cryptocurrency Scam",
    ]

    pool = pd.concat([
        individuals.sample(n_ind, random_state=SEED).assign(
            Entity_ID=lambda d: d["Individual_ID"], Entity_Name=lambda d: d["Individual Name"], Entity_Type="Individual"),
        corporates.sample(n_corp, random_state=SEED).assign(
            Entity_ID=lambda d: d["Corporate_ID"], Entity_Name=lambda d: d["Corporate Name"], Entity_Type="Corporate"),
    ])
    # every picked entity appears at least once; some get several articles
    chosen = pd.concat([pool, pool.sample(extra, replace=True, random_state=SEED)])

    rows = []
    for i, (_, r) in enumerate(chosen.iterrows(), start=1):
        rows.append({
            "Media_ID": f"MED-{i:04d}",
            "Entity_ID": r["Entity_ID"],
            "Entity Name": r["Entity_Name"],
            "Entity Type": r["Entity_Type"],
            "Country": r["Country"],
            "Media Source": random.choice(sources),
            "Issue / Allegation": random.choice(issues),
        })
    return pd.DataFrame(rows)


# --- Sheet 6: High Risk Country (unique countries, taken from the same list) ---
def generate_high_risk_country_data(n=15):
    reasons = [
        "Terrorism Risk", "Sanctions Evasion", "Political Instability", "Civil Unrest",
        "Weak AML Controls", "High Corruption", "Drug Trafficking Hub", "Armed Conflict",
        "Secrecy Jurisdiction", "FATF Grey List", "FATF Black List",
    ]
    rows = []
    for i, country in enumerate(random.sample(COUNTRIES, n), start=1):   # no repeats
        rows.append({
            "HRJ_ID": f"HRJ-{i:04d}",
            "Country": country,
            "Reason / Notes": random.choice(reasons),
        })
    return pd.DataFrame(rows)


sanctions_df = generate_sanctions_data(individuals_df, corporates_df)
pep_df = generate_pep_data(individuals_df, corporates_df)
media_df = generate_adverse_media_data(individuals_df, corporates_df)
hrj_df = generate_high_risk_country_data()
# =====================================================
# CHECKS - every line should print True
# =====================================================
master = pd.concat([
    individuals_df.rename(columns={"Individual_ID": "ID", "Individual Name": "Name"})[["ID", "Name", "Country"]],
    corporates_df.rename(columns={"Corporate_ID": "ID", "Corporate Name": "Name"})[["ID", "Name", "Country"]],
])

def all_match_master(df):
    """Every ID + name + country in a screening sheet must exist, identical, in the masters."""
    check = df.rename(columns={"Entity_ID": "ID", "Entity Name": "Name"})[["ID", "Name", "Country"]]
    return len(check.merge(master, on=["ID", "Name", "Country"])) == len(check)

print("Sanctions match masters  :", all_match_master(sanctions_df))
print("PEP match masters        :", all_match_master(pep_df))
print("Adverse media match      :", all_match_master(media_df))
print("No duplicate names       :", master["Name"].is_unique)
print("No duplicates (ignoring case/punctuation):", master["Name"].map(_norm).is_unique)
print("No name shared by Individual & Corporate :", set(individuals_df["Individual Name"].map(_norm)).isdisjoint(corporates_df["Corporate Name"].map(_norm)))
print("Individual names look like people        :", not individuals_df["Individual Name"].map(looks_corporate).any())
print("Individual names are exactly First Last  :", individuals_df["Individual Name"].str.split().str.len().eq(2).all())
print("Corporate names look like companies      :", corporates_df["Corporate Name"].map(looks_corporate).all())
print("Review never before added:", all(
    (df["Date of Last Review"] >= df["Date Added"]).all()
    for df in [corporates_df, individuals_df, sanctions_df]))
print("Added after incorporation:", (corporates_df["Date Added"] >= corporates_df["Date of Incorporation"]).all())
print("Left office after started:", (pep_df["Date of Leaving Office"].dropna() >= pep_df.loc[pep_df["Date of Leaving Office"].notna(), "Date of Assuming Office"]).all())
print("Removal after listing    :", (sanctions_df["Date of Removal"].dropna() >= sanctions_df.loc[sanctions_df["Date of Removal"].notna(), "Date Added"]).all())
print("HRC countries unique     :", hrj_df["Country"].is_unique)

# --- new checks ---
print("Every individual has a corporate link :", individuals_df["Linked Corporate_ID"].isin(corporates_df["Corporate_ID"]).all())
linked_check = individuals_df.merge(corporates_df, left_on="Linked Corporate_ID", right_on="Corporate_ID")
print("Linked corporate names match master   :", (linked_check["Linked Corporate Name"] == linked_check["Corporate Name"]).all())
pep_check = pep_df.merge(individuals_df, left_on="Entity_ID", right_on="Individual_ID", suffixes=("", "_ind"))
print("PEP links match Individual sheet      :", (pep_check["Linked Corporate_ID"] == pep_check["Linked Corporate_ID_ind"]).all()
      and (pep_check["Association"] == pep_check["Association_ind"]).all())
print("Yes/No flag columns removed           :", not any(c in df.columns for df in [individuals_df, corporates_df]
      for c in ["Adverse Media", "PEP", "Sanctions", "High Risk Country"]))
print("Risk Level removed from HRC sheet     :", "Risk Level" not in hrj_df.columns)
print("Nature of business variety            :", corporates_df["Nature of Business"].nunique(), "different types")
print("No date columns on PEP/Media/HRC      :", not any(c in df.columns for df in [pep_df, media_df, hrj_df]
      for c in ["Date Added", "Date of Last Review"]))
print("Every corporate has an individual      :", corporates_df["Corporate_ID"].isin(individuals_df["Linked Corporate_ID"]).all())
print("Association types                      :", sorted(individuals_df["Association"].unique()))
print("Sanction types                         :", sorted(sanctions_df["Sanction Type"].unique()))
# =====================================================
# EXPORT - real Excel dates (dd/mm/yyyy), one format everywhere
# =====================================================
with pd.ExcelWriter("Compliance_Workbook_Fake.xlsx", engine="openpyxl",
                    date_format="DD/MM/YYYY", datetime_format="DD/MM/YYYY") as writer:
    sheets = {
        "Corporate": corporates_df, "Individual": individuals_df,
        "Sanctions": sanctions_df, "PEP": pep_df,
        "AdverseMedia": media_df, "HighRiskCountry": hrj_df,
    }
    for name, df in sheets.items():
        df.to_excel(writer, sheet_name=name, index=False)
        ws = writer.sheets[name]
        for col in ws.columns:                       # widen columns to fit
            width = max(len(str(c.value)) if c.value is not None else 0 for c in col)
            ws.column_dimensions[col[0].column_letter].width = min(width + 2, 40)

print("Workbook generated with 6 sheets: Compliance_Workbook_Fake.xlsx")
