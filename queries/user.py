import logging

from core.database_settings import execute_query

def register_user(data : dict):
    try :
        query = """
            INSERT INTO users (full_name, phone_number, chat_id) VALUES (%s, %s, %s);
        """
        params = (
            data.get("name"), data.get("phone_number"),
            data.get("chat_id")
        )

        execute_query(query, params)
        return True
    except Exception as e:
        logging.error(e)
        return None

def get_user(chat_id: int):
    try:
        query = """
            SELECT * FROM users WHERE chat_id = %s;
        """
        params = (chat_id,)
        return execute_query(query=query,params= params,fetch="one")
    except Exception as e:
        logging.error(e)
        return None