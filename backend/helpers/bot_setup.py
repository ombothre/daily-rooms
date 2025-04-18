from models.bot import BotModel
from helpers.prompts.prompts import *
from logger_setup import logger

class BotSetup:

    def __init__(self, bot_model: BotModel, prompt: str, max_duration: int = 300):

        bot_model.llm.system_prompt = prompt
        logger.info(f"Initializing BotSetup with bot_model: {bot_model}, max_duration: {max_duration}")
        self.payload = {
            "bot_profile": bot_model.bot_profile,
            "max_duration": 500,
            "services": {
                "tts": bot_model.tts.service,
                "llm": bot_model.llm.service,
            },
            "config": [
                {
                    "service": "stt",
                    "options": [
                        {
                            "name": "model",
                            "value": bot_model.stt.model
                        },
                        {
                            "name": "language",
                            "value": bot_model.stt.language
                        }
                    ]
                },
                {
                    "service": "tts",
                    "options": [
                        {
                            "name": "voice",
                            "value": "79a125e8-cd45-4c13-8a67-188112f4dd22"
                        }
                    ]
                },
                {
                    "service": "llm",
                    "options": [
                        {
                            "name": "model",
                            "value": bot_model.llm.model
                        },
                        {
                            "name": "initial_messages",
                            "value": [
                                {
                                    "role": "user",
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": bot_model.llm.system_prompt
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "run_on_config",
                            "value": True
                        }
                    ]
                }
            ]
        }
        logger.debug(f"Payload initialized: {self.payload}")

    def get_payload(self):
        logger.info("Getting payload")
        return self.payload