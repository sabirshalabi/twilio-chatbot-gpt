import sqlite3
import uuid


def get_connection():
    """
    Establish a connection to the database and return a connection object.
    """
    conn = sqlite3.connect("chatbot.db")
    return conn


def insert_message(body, message_id):
    """
    Insert a new message into the "messages" table.
    """
    with get_connection() as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO messages (body, message_id) VALUES (?, ?)", (body, message_id))


def insert_response(body, message_id):
    """
    Insert a new chatbot response into the "chatbot_responses" table.
    :param body:
    :param message_id:
    :return:
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO responses (body, message_id) VALUES (?, ?)", (body, message_id))


def get_messages():
    """
    Retrieve all messages from the "messages" table.
    """
    with get_connection() as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM messages")
            return cursor.fetchall()


def get_responses(message_id):
    """
    Retrieve all responses for a given message ID.
    """
    with get_connection() as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM chatbot_responses WHERE message_id=?", (message_id,))
            return cursor.fetchall()
