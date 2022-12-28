# Twilio-GPT Chatbot
A chatbot powered by the OpenAI GPT-3 language model, designed to assist and entertain users by providing useful information on a wide range of topics.

## Features
* Utilizes the GPT-3 language model to generate responses to user questions
* Can understand and interpret natural language inputs and generate coherent and relevant responses
* Constantly learning and evolving to better serve users
## Getting Started
To use the Twilio-GPT Chatbot, you will need to have a Twilio account and a phone number that can receive SMS messages. You will also need to obtain an OpenAI API key.
1. Clone the repository and install the dependencies:
```bash
git clone https://github.com/sabirshalabi/twilio-chatbot-gpt/
cd twilio-gpt-chatbot
pip install -r requirements.txt
```
2. Set the following environment variables:
* account_sid: Your Twilio account SID
* auth_token: Your Twilio auth token
* twilio_phone_number: Your Twilio phone number
* my_phone_number: The phone number to send SMS messages to
* openai_api_key: Your OpenAI API key
3. Run the app:
```bash 
python app.py
```
4. Send a text message to your Twilio phone number with your question or request. The chatbot will respond with an answer or information.
## Troubleshooting
If you encounter any issues while using the Twilio-GPT Chatbot, you can check the 'chat_log.txt' file for more information and troubleshoot accordingly.

