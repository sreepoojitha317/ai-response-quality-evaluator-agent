import os
import pickle

from langchain_huggingface import HuggingFaceEmbeddings

# Load Chunks

chunk_path = "data/processed/chunks.pkl"

with open(chunk_path, "rb") as f:
    chunks = pickle.load(f)

print("=" * 60)
print("Chunks Loaded Successfully")
print("=" * 60)
print(f"Total Chunks : {len(chunks)}")

# Load Embedding Model

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("\nEmbedding Model Loaded Successfully!")

# Test Embedding

sample_text = chunks[0].page_content

embedding = embedding_model.embed_query(sample_text)

print("\n" + "=" * 60)
print("Embedding Generated Successfully")
print("=" * 60)
print(f"Embedding Dimension : {len(embedding)}")

print("\nFirst 10 Values:")
print(embedding[:10])