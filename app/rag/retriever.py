from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Configuration

DB_PATH = "data/chroma_db"

# Load Embedding Model

print("=" * 60)
print("Loading Embedding Model...")
print("=" * 60)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding Model Loaded Successfully!")

# Load Vector Database

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embedding_model
)

print("\nVector Database Loaded Successfully!")

# Check Metadata

print("\nChecking metadata stored in ChromaDB...\n")

sample_docs = db.similarity_search(
    query="watermelon",
    k=3
)

for i, doc in enumerate(sample_docs, start=1):
    print(f"Document {i} Metadata:")
    print(doc.metadata)

# User Question

question = input("\nEnter your question: ")

print("\nSearching TruthfulQA first...\n")

# Search TruthfulQA First

results = db.similarity_search_with_score(
    query=question,
    k=2
)

# Fallback

if len(results) == 0:

    print("No TruthfulQA result found.")
    print("Searching entire Knowledge Base...\n")

    results = db.similarity_search_with_score(
        query=question,
        k=5
    )

# Display Results

print("=" * 60)
print("Top Retrieved Chunks")
print("=" * 60)

for i, (doc, score) in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 60)

    print(f"Similarity Score : {score:.4f}")

    print("\nMetadata:")
    print(doc.metadata)

    print("\nContent:")
    print(doc.page_content)

print("\n" + "=" * 60)
print("Retrieval Completed")
print("=" * 60)