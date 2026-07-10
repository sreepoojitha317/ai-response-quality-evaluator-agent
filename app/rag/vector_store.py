import os
import pickle
import shutil
import time

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# ============================================================
# Configuration
# ============================================================

CHUNK_PATH = "data/processed/chunks.pkl"
DB_PATH = "data/chroma_db"

BATCH_SIZE = 1000

# ============================================================
# Load Documents
# ============================================================

print("=" * 60)
print("Loading Documents...")
print("=" * 60)

with open(CHUNK_PATH, "rb") as f:
    documents = pickle.load(f)

print(f"Total Documents : {len(documents)}")

# ============================================================
# Load Embedding Model
# ============================================================

print("\nLoading Embedding Model...")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding Model Loaded Successfully!")

# ============================================================
# Remove Existing Database (Fresh Build)
# ============================================================

if os.path.exists(DB_PATH):
    print("\nRemoving Existing ChromaDB...")
    shutil.rmtree(DB_PATH)

os.makedirs(DB_PATH, exist_ok=True)

# ============================================================
# Initialize ChromaDB
# ============================================================

db = Chroma(
    collection_name="knowledge_base",
    persist_directory=DB_PATH,
    embedding_function=embedding_model
)

print("\nChromaDB Initialized Successfully!")

# ============================================================
# Generate Embeddings & Store
# ============================================================

start_time = time.time()

print("\nStarting Embedding Generation...\n")

total_documents = len(documents)

for i in range(0, total_documents, BATCH_SIZE):

    batch = documents[i:i + BATCH_SIZE]

    ids = [
        f"doc_{j}"
        for j in range(i, i + len(batch))
    ]

    db.add_documents(
        documents=batch,
        ids=ids
    )

    completed = min(i + BATCH_SIZE, total_documents)

    print(f"Completed : {completed}/{total_documents}")

end_time = time.time()

# ============================================================
# Verify Database
# ============================================================

stored_documents = db._collection.count()

# ============================================================
# Finished
# ============================================================

print("\n" + "=" * 60)
print("Vector Database Created Successfully")
print("=" * 60)

print(f"Database Location : {DB_PATH}")
print(f"Documents Stored : {stored_documents}")
print(f"Time Taken : {(end_time-start_time)/60:.2f} minutes")