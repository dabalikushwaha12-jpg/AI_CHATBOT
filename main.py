from openai import OpenAI
import os

# Create OpenAI client using environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

client = OpenAI(api_key=api_key)

# Store conversation history
messages = []

def completion(user_message):
    global messages

    # Add user message
    messages.append({
        "role": "user",
        "content": user_message
    })

    try:
        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        reply = response.choices[0].message.content

        # Store assistant reply
        messages.append({
            "role": "assistant",
            "content": reply
        })

        print(f"LUFFY 🤖: {reply}")

    except Exception as e:
        print("Error:", e)


# Main program
if __name__ == "__main__":
    print("Hi, I am LUFFY 🤖. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("LUFFY: Goodbye 👋")
            break

        completion(user_input)