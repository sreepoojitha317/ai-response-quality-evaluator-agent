from ollama import chat

print("=" * 60)
print("Ollama Llama 3.2 Model Loaded Successfully!")
print("=" * 60)


def generate_response(prompt: str):

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content


if __name__ == "__main__":

    prompt = input("Enter Prompt: ")

    result = generate_response(prompt)

    print("\nLlama Response:\n")

    print(result)