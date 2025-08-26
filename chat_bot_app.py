# TODOS
# Add chat memory
# use a local server like streamlit
# Modify streamlit with HTML to make a nice looking chat bot
# Use langchain framework to read .pdf files
# Use an open source LLM that doesn't cost tokens
# imports
import openai
# logic
# generate response function
def generate_response(user_input):
    try:
        completion = openai.Completion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': "system",
                       "content": "Assume the role of a Python teacher, and think step by step. Your name is Skippy Py."},
                      {'role': "user", "content": user_input}]
        )
        response_text = completion["choices"][0]["message"]["content"]
        return response_text
    except Exception as e:
        print("Error generating response:", e)
        return "I'm sorry, I couldn't generate response."
# program entry point
def main():
    # !###! supply api key to work !###!
    openai.api_key = ""
    print("Welcome to the Python Study Bot! Type 'quit' to exit. \n")
    while True:
        user_input = input("What is your name? ")
        if user_input.lower() == "quit":
            print("Exiting Python Study Bot.")
            break
        response = generate_response(user_input)
        print("Python Study Bot", response)
# idiom
if __name__ == "__main__":
    main()