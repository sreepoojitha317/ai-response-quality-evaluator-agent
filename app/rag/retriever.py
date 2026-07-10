from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# ============================================================
# Configuration
# ============================================================

DB_PATH = "data/chroma_db"

# ============================================================
# Load Embedding Model
# ============================================================

print("=" * 60)
print("Loading Embedding Model...")
print("=" * 60)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding Model Loaded Successfully!")

# ============================================================
# Load Vector Database
# ============================================================

db = Chroma(
    collection_name="knowledge_base",
    persist_directory=DB_PATH,
    embedding_function=embedding_model
)

print("\nVector Database Loaded Successfully!")

# ============================================================
# Check Metadata
# ============================================================

print("\nChecking metadata stored in ChromaDB...\n")

sample_docs = db.similarity_search(
    query="watermelon",
    k=3
)

for i, doc in enumerate(sample_docs, start=1):
    print(f"Document {i} Metadata:")
    print(doc.metadata)

# ============================================================
# Interactive Retrieval
# ============================================================

while True:

    print("\n" + "=" * 60)

    question = input("Enter your question: ").strip()

    if question == "":
        print("Please enter a valid question.")
        continue

    print("\nSearching Knowledge Base...\n")

    results = db.similarity_search_with_score(
        query=question,
        k=1
    )

    print("=" * 60)
    print("Top Retrieved Document")
    print("=" * 60)

    for i, (doc, score) in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("-" * 60)

        print(f"Similarity Score : {score:.4f}")

        print("\nSource:")
        print(doc.metadata["source"])

        print("\nQuestion:")
        print(doc.metadata["question"])

        print("\nAnswer:")
        print(doc.metadata["answer"])

        print("\nContent:")
        print(doc.page_content)

    print("\n" + "=" * 60)
    print("Retrieval Completed")
    print("=" * 60)

    choice = input("\nDo you want to ask another question? (Y/N): ").strip().lower()

    while choice not in ["y", "n"]:
        choice = input("Please enter Y or N: ").strip().lower()

    if choice == "n":
        print("\nThank you for using the RAG Retriever!")
        break