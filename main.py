import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def main():
    print("Application started...")

    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key or api_key == None:
        raise RuntimeError("OPENROUTER_API_KEY tidak ditemukan!")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.chat.completions.create(
        model="openrouter/free",
        messages= [
            {
                "role": "user",
                "content": content,
            }
        ],
    )

    if response.usage == None:
        raise RuntimeError("Usage tidak ditemukan!")
    
    
    print(f"User prompt: {content}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print("Response: ")
    print(response.choices[0].message.content)



if __name__ == "__main__":
    main()

