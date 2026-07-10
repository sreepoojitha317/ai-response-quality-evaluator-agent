import pandas as pd

# ============================================================
# Load Merged Dataset
# ============================================================

dataset_path = "data/processed/merged_dataset.csv"

df = pd.read_csv(dataset_path)

print("=" * 60)
print("Merged Dataset Loaded Successfully")
print("=" * 60)

print(f"Total Records Before Cleaning : {len(df)}")

# ============================================================
# Remove Missing Values
# ============================================================

df.dropna(
    subset=["question", "answer", "context"],
    inplace=True
)

# ============================================================
# Remove Extra Spaces
# ============================================================

for col in ["question", "answer", "context"]:
    df[col] = df[col].astype(str).str.strip()

# ============================================================
# Remove Empty Records
# ============================================================

df = df[
    (df["question"] != "") &
    (df["answer"] != "") &
    (df["context"] != "")
]

# ============================================================
# Remove Duplicate Question + Answer Pairs
# ============================================================

df.drop_duplicates(
    subset=["question", "answer"],
    inplace=True
)

df.reset_index(drop=True, inplace=True)

# ============================================================
# Display Results
# ============================================================

print("\n" + "=" * 60)
print("Data Cleaning Completed")
print("=" * 60)

print(f"Total Records After Cleaning : {len(df)}")

print("\nSample Record:\n")
print(df.iloc[0])

# ============================================================
# Save Processed Dataset
# ============================================================

output_path = "data/processed/processed_dataset.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nProcessed dataset saved successfully!")
print(f"Location : {output_path}")