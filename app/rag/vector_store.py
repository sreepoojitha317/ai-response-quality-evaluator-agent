import os
import pickle
import time

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Configuration

CHUNK_PATH = "data/processed/chunks.pkl"
DB_PATH = "data/chroma_db"

BATCH_SIZE = 1000

# Load Chunks

print("=" * 60)
print("Loading Chunks...")
print("=" * 60)

with open(CHUNK_PATH, "rb") as f:
    chunks = pickle.load(f)

print(f"Total Chunks : {len(chunks)}")

# Load Embedding Model

print("\nLoading Embedding Model...")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding Model Loaded Successfully!")

# Initialize ChromaDB

os.makedirs(DB_PATH, exist_ok=True)

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embedding_model
)

print("\nChromaDB Initialized Successfully!")

# Generate Embeddings & Store

total_chunks = len(chunks)

start_time = time.time()

print("\nStarting Embedding Generation...\n")

for i in range(0, total_chunks, BATCH_SIZE):

    batch = chunks[i:i + BATCH_SIZE]

    ids = [
        f"doc_{j}"
        for j in range(i, i + len(batch))
    ]

    try:

        db.add_documents(
            documents=batch,
            ids=ids
        )

        completed = min(i + BATCH_SIZE, total_chunks)

        print(
            f"Completed : {completed}/{total_chunks}"
        )

    except Exception as e:

        print(f"\nError at batch starting index {i}")
        print(e)
        break

end_time = time.time()

# Finished

print("\n" + "=" * 60)
print("Vector Database Created Successfully")
print("=" * 60)

print(f"Database Location : {DB_PATH}")
print(f"Total Chunks Stored : {total_chunks}")
print(f"Time Taken : {(end_time-start_time)/60:.2f} minutes")