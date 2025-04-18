from dotenv import load_dotenv
import os

class Utils:
    def __init__(self):
        load_dotenv()

    def get_api_key(self):
        return os.getenv('DAILY_API_KEY')

    def base_url(self):
        return 'https://api.daily.co/v1/'
    
utils = Utils()