import pandas as pd

# Load Merged Dataset

dataset_path = "data/processed/merged_dataset.csv"

df = pd.read_csv(dataset_path)

print("=" * 60)
print("Merged Dataset Loaded Successfully")
print("=" * 60)

print(f"Total Records Before Cleaning : {len(df)}")

# Remove Missing Values

df.dropna(
    subset=["question", "answer"],
    inplace=True
)

# Remove Empty Strings

df = df[
    (df["question"].str.strip() != "") &
    (df["answer"].str.strip() != "")
]

# Remove Duplicate Questions

df.drop_duplicates(
    subset=["question"],
    inplace=True
)

# Remove Extra Spaces

df["question"] = df["question"].str.strip()

df["answer"] = df["answer"].str.strip()

df["context"] = df["context"].str.strip()

# Display Results

print("\n" + "=" * 60)
print("Data Cleaning Completed")
print("=" * 60)

print(f"Total Records After Cleaning : {len(df)}")

print("\nSample Record:\n")

print(df.iloc[0])

# Save Clean Dataset

output_path = "data/processed/processed_dataset.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nProcessed dataset saved successfully!")

print(f"Location : {output_path}")