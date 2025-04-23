# DA/clean_and_export.py

import pandas as pd

# STEP 1: Load the raw data
file_path = "prev-County_Parcels.csv"  # Make sure this is in your DA folder
df = pd.read_csv(file_path)

# STEP 2: Keep only useful columns for now
df = df[[
    "PID", "MUNIC_NM", "BUILD_YR", "SALE_DATE", "SALE_PRICE",
    "PARCEL_AREA", "MKT_VAL_TOT", "PR_TYP_NM1", "LAT", "LON"
]]

# STEP 3: Clean column names
df.columns = [col.lower() for col in df.columns]

# STEP 4: Convert data types
df["build_yr"] = pd.to_numeric(df["build_yr"], errors="coerce")
df["sale_price"] = pd.to_numeric(df["sale_price"], errors="coerce")
df["mkt_val_tot"] = pd.to_numeric(df["mkt_val_tot"], errors="coerce")

# STEP 5: Standardize city names
df["municipality"] = df["munic_nm"].str.strip().str.title()

# STEP 6: Drop rows with missing market value or lat/lon
df = df.dropna(subset=["mkt_val_tot", "lat", "lon"])

# STEP 7: Export cleaned version
df.to_csv("cleaned_county_parcels.csv", index=False)
print("✅ Cleaned file exported as cleaned_county_parcels.csv")