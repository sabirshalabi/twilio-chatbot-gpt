import openai
import os

# Load the OpenAI API key from the .env file
openai.api_key = os.getenv('openai_api_key')

# Define the start and restart sequences
start_sequence = "\nBot: "
restart_sequence = "\n\nPerson: "

# Define the session prompt
session_prompt = "You are talking to a GPT-3 powered chatbot created by a masterful python coder. You can ask me anything you want and it will generate a witty and informative response.\n\nPerson: Who are you?\nBot: I am a GPT-3 powered chatbot created to assist and entertain.\n\nPerson: What can you do?\nBot: I can answer any question you have and provide useful information on a wide range of topics. I am constantly learning and evolving to better serve my users.\n\nPerson: How do you work?\nBot: I use the power of the GPT-3 language model to generate responses to your questions. I can understand and interpret natural language inputs and generate coherent and relevant responses.\n\nPerson: "


def ask(question, chat_log=None):
    """
    Send a query to the GPT-3 API and return the response.
    """
    # Set the prompt for the query
    prompt = session_prompt + question

    # Make the request to the GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-003",
        temperature=0.8,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        prompt=prompt
    )


    # Return the response text
    return response.choices[0].text

def save_chat_log_to_file(chat_log):
    with open("chat_log.txt", "a") as f:
        f.write(chat_log)


def append_interaction_to_chat_log(question, answer, chat_log):
    """
    Append the incoming message and chatbot's response to the chat log.
    """
    # Add the incoming message and chatbot's response to the chat log
    if chat_log is None:
        chat_log = start_sequence + question + "\n" + restart_sequence + answer
    else:
        chat_log += start_sequence + question + "\n" + restart_sequence + answer

    # Save the chat log to a file
    save_chat_log_to_file(chat_log)

    return chat_log


