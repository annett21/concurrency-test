from dotenv import load_dotenv
import os


load_dotenv()


def get_static_url():
    ngrok_url = os.getenv("NGROK_URL")
    if ngrok_url is not None:
        return ngrok_url + "/static/"
    else:
        return "http://localhost:8000/static-dummy/"

