import random
from flask import Flask, request
from twilio.rest import Client
from bot import ask
from db import insert_message, insert_response, get_messages, get_responses
import os

app = Flask(__name__)

# Set the secret key to a random string to keep session data secure
app.config['SECRET_KEY'] = 'any-random-string'

# Set the Twilio account SID and auth token
account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

# Set the Twilio phone number
twilio_phone_number = os.getenv('twilio_phone_number')

# Set the phone number to send SMS to
my_phone_number = os.getenv('my_phone_number')



@app.route('/', methods=['POST'])
def bot():
    # Get the incoming message from the request values
    incoming_msg = request.form['Body']

    # Generate a random message ID
    message_id = random.randint(1, 100000)

    # Insert the new message into the "messages" table
    insert_message(incoming_msg, message_id)

    # Get the chatbot's response
    answer = ask(incoming_msg, message_id)

    # Insert the new chatbot response into the "chatbot_responses" table
    insert_response(answer, message_id)

    # Retrieve all messages and chatbot responses from the database
    messages = get_messages()
    chat_log = ""
    for message in messages:
        message_id = message[0]
        body = message[1]
        chat_log += f"\nPerson: {body}"
        responses = get_responses(message_id)
        for response in responses:
            body = response[1]
            chat_log += f"\nBot: {body}"

    # Use Twilio to send the chatbot's response as a text message
    message = client.messages.create(
        body=answer,
        from_=twilio_phone_number,
        to=my_phone_number
    )

    return str(message.sid)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
