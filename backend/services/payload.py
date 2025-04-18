from helpers.prompts.prompts import *
from models.prompts import *
from logger_setup import logger

classes = {
    "default": [DefaultPrompt, Default],
    "bajaj": [BajajPrompt, Bajaj],
    "hdfc": [HDFCPrompt, HDFC]
}

def get_payload(bot: str, **kwargs) -> str:
    logger.debug(f"Generating payload for bot: {bot} with kwargs: {kwargs}")
    curr_class: list = classes.get(bot, classes["default"])
    prompt_class = curr_class[0]
    model_class = curr_class[1]
    print("MODEL: ",model_class)
    vars = model_class(**kwargs)
    prompt = prompt_class().get_prompt(vars)
    logger.debug(f"Generated prompt: {prompt}")
    return prompt
