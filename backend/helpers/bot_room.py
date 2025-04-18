import requests
from settings import utils
from logger_setup import logger

class BotAPI:
    def __init__(self, token: str, payload: dict, base_url: str = None):
        """
        Initialize the BotAPI class.

        :param token: Authorization token for API access.
        :param base_url: Base URL for the API (optional, uses utils.base_url if not provided).
        """
        logger.info("Initializing BotAPI")
        self.token = token
        self.payload = payload
        self.base_url = base_url or utils.base_url()
        self.url = self.base_url + "bots/start"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        logger.debug(f"BotAPI initialized with URL: {self.url} and headers: {self.headers}")
    
    def start_bot(self) -> requests.Response:
        """
        Sends a POST request to start a bot.

        :return: The response object from the API request.
        """
        logger.info("Starting bot")
        try:
            print(f"URL: {self.url} PAYLOAD: {self.payload} HEADEARS : {self.headers}")
            response = requests.post(self.url, json=self.payload, headers=self.headers)
            logger.info(f"Bot started with response status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to start bot: {e}")
            return str(e)