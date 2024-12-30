
'''import openai


openai.api_key = "cd/sushmareddy/chatbot_ex/openai_key.txt"

def chat_with_gpt(prompt):
    try:
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  
            messages=[{"role": "user", "content": prompt}]
        )

        message = response['choices'][0]['message']['content']
        return message

    except openai._exceptions.OpenAIError as e:
        print(f"An error occurred: {e}")
        return "Sorry, I couldn't process your request."

# Main loop to interact with the chatbot
print("Chatbot is running. Type 'quit', 'exit', or 'bye' to stop.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit', 'bye']:
        print("Goodbye!")
        break
    
    response = chat_with_gpt(user_input)
    print(f"Chatbot: {response}")
'''



import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

if openai.api_key is None:
    print("API key not set. Please set the OPENAI_API_KEY environment variable.")
    exit()

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            timeout=30
        )
        return response.choices[0].message.content.strip()
    except openai.error.OpenAIError as e:  
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Chatbot is running. Type 'quit', 'exit', or 'bye' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
