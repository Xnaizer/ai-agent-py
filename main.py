import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt 
from call_function import available_functions, call_function

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
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    try:
        for _ in range(20):
            response = client.chat.completions.create(
                model="openrouter/free",
                messages=messages,
                tools=available_functions,
            )

            message = response.choices[0].message
            messages.append(message)
            
            if is_verbose:
                print(f"User prompt: {user_prompt}")
                print(f"Prompt tokens: {response.usage.prompt_tokens}")
                print(f"Response tokens: {response.usage.completion_tokens}")

            
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    result_message = call_function(tool_call, is_verbose)

                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content" : result_message["content"]
                        }
                    )

                    if not result_message["content"]:
                        raise Exception("Tool returned an empty response")

                    if is_verbose:
                        print(f"-> {result_message['content']}")
            else:
                print(message.content)
                break
        else:
            print("Error: Agent reached the maximum number of iterations (20).")

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    main()

