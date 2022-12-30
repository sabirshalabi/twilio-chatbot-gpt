# @app.route('/', methods=['POST'])
# def bot():
#     # Get the incoming message from the request values
#     incoming_msg = request.values['Body']
#
#     # Get the chat log from the session data
#     chat_log = session.get('chat_log')
#
#     # Get the chatbot's response
#     answer = ask(incoming_msg, chat_log)
#
#     # Append the incoming message and chatbot's response to the chat log
#     session['chat_log'] = append_interaction_to_chat_log(
#         incoming_msg, answer, chat_log)
#
#     # Use Twilio to send the chatbot's response as a text message
#     message = client.messages.create(
#         body=answer,
#         from_=twilio_phone_number,
#         to=my_phone_number
# )
#
#     return str(message.sid)