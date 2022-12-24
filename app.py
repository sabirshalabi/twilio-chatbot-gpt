from flask import Flask, request, session
from twilio.rest import Client
from sabirsbot import ask, append_interaction_to_chat_log
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
def sabirsbot():
    # Get the incoming message from the request values
    incoming_msg = request.values['Body']

    # Get the chat log from the session data
    chat_log = session.get('chat_log')

    # Get the chatbot's response
    answer = ask(incoming_msg, chat_log)

    # Append the incoming message and chatbot's response to the chat log
    session['chat_log'] = append_interaction_to_chat_log(
        incoming_msg, answer, chat_log)

    # Use Twilio to send the chatbot's response as a text message
    message = client.messages.create(
        body=answer,
        from_=twilio_phone_number,
        to=my_phone_number
)

    return str(message.sid)



# @app.route('/sabirsbot', methods=['POST'])
# def sabirsbot():
#     # Get the incoming message from the request values
#     incoming_msg = request.values['Body']

#     try:
#         # Get the chat log from the session data
#         chat_log = session.get('chat_log')
#     except Exception as e:
#         print(e)
#         return "Error getting chat log"
#     try:
#         # Get the chatbot's response
#         print("Getting chatbot's response")
#         answer = ask(incoming_msg, chat_log)
#     except Exception as e:
#         print(e)
#         return "Error getting chatbot's response"

#     try:
#         # Append the incoming message and chatbot's response to the chat log
#         session['chat_log'] = append_interaction_to_chat_log(
#             incoming_msg, answer, chat_log)
#     except Exception as e:
#         print(e)
#         return "Error appending incoming message and chatbot's response to chat log"

#     try:
#         # Use Twilio to send the chatbot's response as a text message
#         message = client.messages.create(
#             body=answer,
#             from_=twilio_phone_number,
#             to=my_phone_number
#         )
#     except Exception as e:
#         print(e)
#         return "Error sending chatbot's response as text message"

#     return str(message.sid)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
