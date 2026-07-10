import os
import json
import pandas as pd

# ============================================================
# Load TruthfulQA Dataset
# ============================================================

truthfulqa_path = "data/raw/TruthfulQA.csv"

truthful_df = pd.read_csv(truthfulqa_path)

print("=" * 60)
print("TruthfulQA Loaded Successfully")
print("=" * 60)

print(f"Total Records : {len(truthful_df)}")

print("\nColumns:")
print(truthful_df.columns.tolist())

print("\nFirst 5 Rows:")
print(truthful_df.head())

# ============================================================
# Load SQuAD Training Dataset
# ============================================================

train_path = "data/raw/train-v1.1.json"

with open(train_path, "r", encoding="utf-8") as f:
    squad_train = json.load(f)

print("\n" + "=" * 60)
print("SQuAD Train Loaded Successfully")
print("=" * 60)

print(f"Total Articles : {len(squad_train['data'])}")

# ============================================================
# Load SQuAD Validation Dataset
# ============================================================

dev_path = "data/raw/dev-v1.1.json"

with open(dev_path, "r", encoding="utf-8") as f:
    squad_dev = json.load(f)

print("\n" + "=" * 60)
print("SQuAD Validation Loaded Successfully")
print("=" * 60)

print(f"Total Articles : {len(squad_dev['data'])}")

# ============================================================
# Convert TruthfulQA to Common Format
# ============================================================

truthful_records = []

for _, row in truthful_df.iterrows():

    truthful_records.append(
        {
            "question": row["Question"],
            "answer": row["Best Answer"],
            "context": row["Best Answer"],
            "source": "TruthfulQA"
        }
    )

print("\n" + "=" * 60)
print("TruthfulQA Converted Successfully")
print("=" * 60)

print(f"Total QA Pairs : {len(truthful_records)}")

print("\nSample Record:")
print(truthful_records[0])

# ============================================================
# Convert SQuAD to Common Format
# ============================================================

squad_records = []

for article in squad_train["data"]:

    for paragraph in article["paragraphs"]:

        context = paragraph["context"]

        for qa in paragraph["qas"]:

            question = qa["question"]
            answer = qa["answers"][0]["text"]

            squad_records.append(
                {
                    "question": question,
                    "answer": answer,
                    "context": context,
                    "source": "SQuAD"
                }
            )

print("\n" + "=" * 60)
print("SQuAD Converted Successfully")
print("=" * 60)

print(f"Total QA Pairs : {len(squad_records)}")

print("\nSample Record:")
print(squad_records[0])

# ============================================================
# Merge & Shuffle Datasets
# ============================================================

# Keep TruthfulQA first, then SQuAD
all_records = truthful_records + squad_records

merged_df = pd.DataFrame(all_records)

# Shuffle dataset to reduce ordering bias
merged_df = merged_df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

print("\n" + "=" * 60)
print("Merged Dataset")
print("=" * 60)

print(f"Total Records : {len(merged_df)}")

print("\nSample Record:")
print(merged_df.iloc[0].to_dict())

# ============================================================
# Save Merged Dataset
# ============================================================

os.makedirs("data/processed", exist_ok=True)

merged_path = "data/processed/merged_dataset.csv"

merged_df.to_csv(
    merged_path,
    index=False
)

print("\nMerged Dataset Saved Successfully!")
print(f"Location : {merged_path}")