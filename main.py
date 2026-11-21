import os
import json
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt 
from call_function import available_functions


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

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    user_prompt = str(parser.parse_args().user_prompt)
    is_verbose = bool(parser.parse_args().verbose)
    
    messages = [
        {"role": "user", "content": user_prompt},
        {"role": "system", "content": system_prompt}
    ]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    if response.usage == None:
        raise RuntimeError("Usage tidak ditemukan!")

    message = response.choices[0].message
    
    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

       
    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_args = json.loads(
                tool_call.function.arguments or "{}"
            )
        print(f"Calling function: {tool_call.function.name}({function_args})")
    else:
        print(message.content)

if __name__ == "__main__":
    main()

