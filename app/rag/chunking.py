import pandas as pd
import os
import pickle

from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load Processed Dataset

dataset_path = "data/processed/processed_dataset.csv"

df = pd.read_csv(dataset_path)

print("=" * 60)
print("Processed Dataset Loaded Successfully")
print("=" * 60)

print(f"Total Records : {len(df)}")


# Convert DataFrame to LangChain Documents

documents = []

for _, row in df.iterrows():

    content = f"""
Question:
{row['question']}

Answer:
{row['answer']}

Context:
{row['context']}
"""

    doc = Document(

        page_content=content,

        metadata={
            "source": row["source"]
        }

    )

    documents.append(doc)

print("\nTotal Documents :", len(documents))

# Chunk Documents

text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=100

)

chunks = text_splitter.split_documents(documents)

print("\n" + "=" * 60)
print("Chunking Completed")
print("=" * 60)

print(f"Total Chunks : {len(chunks)}")


print("\nSample Chunk:\n")

print(chunks[0].page_content)

print("\nMetadata:")

print(chunks[0].metadata)

# Save Chunks

os.makedirs("data/processed", exist_ok=True)

chunk_path = "data/processed/chunks.pkl"

with open(chunk_path, "wb") as f:
    pickle.dump(chunks, f)

print("\n" + "=" * 60)
print("Chunks Saved Successfully")
print("=" * 60)
print(f"Location : {chunk_path}")
