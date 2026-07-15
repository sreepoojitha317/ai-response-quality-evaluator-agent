import os

from dotenv import load_dotenv
from google import genai

# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# ============================================================
# Configure Gemini Client
# ============================================================

client = genai.Client(api_key=API_KEY)

print("=" * 60)
print("Gemini Model Loaded Successfully!")
print("=" * 60)

# ============================================================
# Function to Generate Response
# ============================================================

def generate_response(prompt: str):

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text


# ============================================================
# Test
# ============================================================

if __name__ == "__main__":

    prompt = input("Enter Prompt: ")

    result = generate_response(prompt)

    print("\nGemini Response:\n")

    print(result)