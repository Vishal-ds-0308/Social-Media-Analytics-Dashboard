"""
=============================================================================
 Social Media Insights Analytics — Data Cleaning & Preprocessing Pipeline
=============================================================================
Author      : Vishal L
Description : Loads raw social media data (Instagram, YouTube, Facebook),
              performs full data cleaning, handles missing values, removes
              outliers using IQR, and exports a clean dataset ready for
              analysis and Power BI dashboard integration.
Dataset     : Social Media Analytics 2024 (8,000 records)
=============================================================================
"""

# ─────────────────────────────────────────────────────────────────────────────
# 1. IMPORTS
# ─────────────────────────────────────────────────────────────────────────────

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ─────────────────────────────────────────────────────────────────────────────
# 2. LOAD DATASET
# ─────────────────────────────────────────────────────────────────────────────

DATA_PATH   = "data/Social_Media_Analytics_2024_8k.csv"
OUTPUT_PATH = "data/Social_Media_Analytics_2024_Cleaned.csv"

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)
print(f"Shape         : {df.shape}")
print(f"Total Records : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")
print()
df.info()
print()
print(df.describe(include="all"))


# ─────────────────────────────────────────────────────────────────────────────
# 3. CLEAN COLUMN NAMES
# ─────────────────────────────────────────────────────────────────────────────

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned Column Names:")
print(df.columns.tolist())


# ─────────────────────────────────────────────────────────────────────────────
# 4. IDENTIFY COLUMN TYPES
# ─────────────────────────────────────────────────────────────────────────────

num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

print(f"\nNumerical Columns ({len(num_cols)}) : {num_cols}")
print(f"Categorical Columns ({len(cat_cols)}) : {cat_cols}")


# ─────────────────────────────────────────────────────────────────────────────
# 5. HANDLE DUPLICATES
# ─────────────────────────────────────────────────────────────────────────────

duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows Found : {duplicates}")

df = df.drop_duplicates().reset_index(drop=True)
print(f"Shape After Removing Duplicates : {df.shape}")


# ─────────────────────────────────────────────────────────────────────────────
# 6. HANDLE MISSING VALUES
# ─────────────────────────────────────────────────────────────────────────────

print("\nMissing Values Before Imputation:")
print(df.isnull().sum())

# Fill numerical columns with median
for col in num_cols:
    if df[col].isna().sum() > 0:
        df[col] = df[col].fillna(df[col].median())
        print(f"  ✔ Filled '{col}' with median")

# Fill categorical columns with mode
for col in cat_cols:
    if df[col].isna().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])
        print(f"  ✔ Filled '{col}' with mode")

print("\nMissing Values After Imputation:")
print(df.isnull().sum())


# ─────────────────────────────────────────────────────────────────────────────
# 7. DATA TYPE CONVERSION
# ─────────────────────────────────────────────────────────────────────────────

# Convert post_date to datetime
df["post_date"] = pd.to_datetime(df["post_date"], errors="coerce")

# If conversion created NaT, fill with mode date
if df["post_date"].isna().sum() > 0:
    df["post_date"] = df["post_date"].fillna(df["post_date"].mode()[0])

print("\nData Types After Conversion:")
print(df.dtypes)


# ─────────────────────────────────────────────────────────────────────────────
# 8. OUTLIER HANDLING (IQR Method)
# ─────────────────────────────────────────────────────────────────────────────

print("\nHandling Outliers using IQR Capping ...")

for col in num_cols:
    Q1    = df[col].quantile(0.25)
    Q3    = df[col].quantile(0.75)
    IQR   = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    n_outliers = ((df[col] < lower) | (df[col] > upper)).sum()
    if n_outliers > 0:
        df[col] = np.where(df[col] < lower, lower, df[col])
        df[col] = np.where(df[col] > upper, upper, df[col])
        print(f"  ✔ '{col}': {n_outliers} outliers capped")


# ─────────────────────────────────────────────────────────────────────────────
# 9. DATA VALIDATION — REMOVE INVALID ROWS
# ─────────────────────────────────────────────────────────────────────────────

before = len(df)
df = df[df["likes"]    >= 0]
df = df[df["shares"]   >= 0]
df = df[df["comments"] >= 0]
df = df.reset_index(drop=True)

print(f"\nRows Removed (Invalid Metrics) : {before - len(df)}")
print(f"Final Dataset Shape            : {df.shape}")


# ─────────────────────────────────────────────────────────────────────────────
# 10. FINAL SUMMARY
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("FINAL DATASET SUMMARY")
print("=" * 60)
df.info()
print()
print(df.describe())

print(f"\nPlatforms   : {df['platform'].unique().tolist()}")
print(f"Time Slots  : {df['time_slot'].unique().tolist()}")
print(f"Content Fmt : {df['content_format'].unique().tolist()}")
print(f"Categories  : {df['content_category'].unique().tolist()}")
print(f"Days        : {df['day'].unique().tolist()}")
print(f"Date Range  : {df['post_date'].min().date()}  →  {df['post_date'].max().date()}")

print(f"\nAvg Engagement Rate : {df['engagement_rate'].mean():.4f}")
print(f"Max Reach           : {int(df['reach'].max()):,}")
print(f"Total Posts         : {len(df):,}")


# ─────────────────────────────────────────────────────────────────────────────
# 11. EXPORT CLEANED DATASET
# ─────────────────────────────────────────────────────────────────────────────

df.to_csv(OUTPUT_PATH, index=False)
print(f"\n✅ Cleaned dataset exported → {OUTPUT_PATH}")
