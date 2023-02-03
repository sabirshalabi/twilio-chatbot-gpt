# import sqlite3
# import uuid
#
#
# def get_connection():
#     """
#     Establish a connection to the database and return a connection object.
#     """
#     conn = sqlite3.connect("chatbot.db")
#     return conn
#
#
# def insert_message(body, message_id):
#     """
#     Insert a new message into the "messages" table.
#     """
#     with get_connection() as conn:
#         with conn:
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO messages (body, message_id) VALUES (?, ?)", (body, message_id))
#
#
# def insert_response(body, message_id):
#     """
#     Insert a new chatbot response into the "chatbot_responses" table.
#     :param body:
#     :param message_id:
#     :return:
#     """
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO responses (body, message_id) VALUES (?, ?)", (body, message_id))
#
#
# def get_messages():
#     """
#     Retrieve all messages from the "messages" table.
#     """
#     with get_connection() as conn:
#         with conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT * FROM messages")
#             return cursor.fetchall()
#
#
# def get_responses(message_id):
#     """
#     Retrieve all responses for a given message ID.
#     """
#     with get_connection() as conn:
#         with conn:
#             cursor = conn.cursor()
#             cursor.execute("SELECT * FROM chatbot_responses WHERE message_id=?", (message_id,))
#             return cursor.fetchall()

import sqlite3
import uuid
import logging

logger = logging.getLogger(__name__)


def create_connection():
    """
    Creates a connection to the database and returns a connection object.
    """
    conn = sqlite3.connect("chatbot.db")
    return conn


def insert_message(body, message_id):
    """
    Insert a new message into the "messages" table.
    """
    if not body or not message_id:
        raise ValueError("Both 'body' and 'message_id' are required fields")

    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (body, message_id) VALUES (?, ?)", (body, message_id))
        conn.commit()
    except Exception as e:
        logger.error(f"Error inserting message into database: {e}")
        raise
    finally:
        conn.close()


def insert_response(body, message_id):
    """
    Insert a new chatbot response into the "chatbot_responses" table.
    :param body:
    :param message_id:
    :return:
    """
    if not body or not message_id:
        raise ValueError("Both 'body' and 'message_id' are required fields")

    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO responses (body, message_id) VALUES (?, ?)", (body, message_id))
        conn.commit()
    except Exception as e:
        logger.error(f"Error inserting response into database: {e}")
        raise
    finally:
        conn.close()


def get_messages():
    """
    Retrieve all messages from the "messages" table.
    """
    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM messages")
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error retrieving messages from database: {e}")
        raise
    finally:
        conn.close()


def get_responses(message_id):
    """
    Retrieve all responses for a given message ID.
    """
    if not message_id:
        raise ValueError("'message_id' is a required field")

    conn = create_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM responses WHERE message_id=?", (message_id,))
        return cursor.fetchall()
    except Exception as e:
        logger.error(f"Error retrieving responses from database: {e}")
        raise
    finally:
        conn.close()
