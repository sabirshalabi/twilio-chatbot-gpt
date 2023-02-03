import openai
import os
from db import insert_message, insert_response, get_messages, get_responses
from scrape import extract_url, scrape_webpage, preprocess_data, generate_summary
import re

# Load the OpenAI API key from the .env file
openai.api_key = os.getenv('openai_api_key')

# Define the start and restart sequences
start_sequence = "\nBot: "
restart_sequence = "\n\nPerson: "

# Define the session prompt
session_prompt = """
I want you to act as a personable chatbot that can read previous chat history from a sheets file 
and continue the conversation. Your main task will be to engage in conversations with users by reading previous chat 
history from a sheets file and responding appropriately. You should be able to understand the context and tone of the 
conversation and craft responses that are appropriate and engaging. Your role will include tasks such as reading 
previous chat history, responding to user prompts, and maintaining the continuity of the conversation. Do not include 
any tasks that are not related to engaging in conversations with users in your role. 

Here is the previous conversation: {{177731366__rows}}

And here is the newest message to the chatbot:
{{177726073__body}}
"""


# def ask(question, message_id):
#     """
#     Send a query to the OpenAI API and return a response.
#     """
#     # Check if a URL is present in the message
#     url_match = re.search(
#         r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})",
#         question)
#     if url_match:
#         # Extract the URL from the message
#         url = url_match.group(1)
#         # Scrape the webpage at the URL
#         data = scrape_webpage(url)
#         # Preprocess the data
#         preprocessed_data = preprocess_data(data)
#         # Generate a summary of the data
#         summary = generate_summary(preprocessed_data)
#         # Return the summary as the chatbot's response
#         return summary
#     # If the "scrape this" command is not present, use the OpenAI API to generate a response
#     else:
#         # Retrieve all messages and chatbot responses from the database
#         messages = get_messages()
#         chat_log = ""
#         for message in messages:
#             body = message[1]
#             chat_log += f"\nPerson: {body}"
#             responses = get_responses(message_id)
#             for response in responses:
#                 body = response[1]
#                 chat_log += f"\nBot: {body}"
#
#         # Set the prompt for the query
#         prompt = session_prompt
#         # If a chat log is provided, include it in the prompt
#         if chat_log:
#             prompt = prompt.replace("{{177731366__rows}}", str(chat_log))
#         # Include the incoming message in the prompt
#         prompt = prompt.replace("{{177726073__body}}", str(question))
#         # print(prompt)
#         # Make the request to the GPT-3 API
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             temperature=0.8,
#             max_tokens=150,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0.3,
#             prompt=prompt
#         )
#
#         # Insert the chatbot's response into the "responses" table
#         insert_response(response.choices[0].text, message_id)
#
#         # Return the response text
#         return response.choices[0].text

def ask(question, message_id):
    """
    Send a query to the OpenAI API and return a response.
    """
    # Check if a URL is present in the message
    url_match = re.search(
        r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]\.[^\s]{2,})",
        question)
    if url_match:
        # Extract the URL from the message
        url = url_match.group(1)
        # Scrape the webpage at the URL
        data = scrape_webpage(url)
        # Preprocess the data
        preprocessed_data = preprocess_data(data)
        # Generate a summary of the data
        summary = generate_summary(preprocessed_data)
        # Return the summary as the chatbot's response
        return summary
    # If the "scrape this" command is not present, use the OpenAI API to generate a response
    else:
        # Retrieve all messages and chatbot responses from the database
        messages = get_messages()
        chat_log = ""
        for i, message in enumerate(messages[-10:]): # only retrieve the last 10 messages
            body = message[1]
            chat_log += f"\nPerson: {body}"
            responses = get_responses(message_id)
            for response in responses:
                body = response[1]
                chat_log += f"\nBot: {body}"

        # Set the prompt for the query
        prompt = session_prompt
        # If a chat log is provided, include it in the prompt
        if chat_log:
            prompt = prompt.replace("{{177731366__rows}}", str(chat_log))
        # Include the incoming message in the prompt
        prompt = prompt.replace("{{177726073__body}}", str(question))
        # print(prompt)
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

        # Insert the chatbot's response into the "responses" table
        insert_response(response.choices[0].text, message_id)

        # Return the response text
        return response.choices[0].text


