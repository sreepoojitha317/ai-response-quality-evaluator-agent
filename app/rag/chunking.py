import os
import pickle
import pandas as pd

from langchain_core.documents import Document

# ============================================================
# Load Processed Dataset
# ============================================================

dataset_path = "data/processed/processed_dataset.csv"

df = pd.read_csv(dataset_path)

print("=" * 60)
print("Processed Dataset Loaded Successfully")
print("=" * 60)
print(f"Total Records : {len(df)}")

# ============================================================
# Create One Document Per QA Pair
# ============================================================

documents = []

for _, row in df.iterrows():

    content = (
        f"Question: {row['question']}\n\n"
        f"Answer: {row['answer']}\n\n"
        f"Context: {row['context']}"
    )

    doc = Document(
        page_content=content,
        metadata={
            "question": row["question"],
            "answer": row["answer"],
            "source": row["source"]
        }
    )

    documents.append(doc)

print("\n" + "=" * 60)
print("Document Creation Completed")
print("=" * 60)
print(f"Total Documents : {len(documents)}")

# ============================================================
# Save Documents
# ============================================================

os.makedirs("data/processed", exist_ok=True)

chunk_path = "data/processed/chunks.pkl"

with open(chunk_path, "wb") as f:
    pickle.dump(documents, f)

print("\nSample Document:\n")
print(documents[0].page_content)

print("\nMetadata:")
print(documents[0].metadata)

print("\n" + "=" * 60)
print("Documents Saved Successfully")
print("=" * 60)
print(f"Location : {chunk_path}")