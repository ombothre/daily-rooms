from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from helpers.bot_room import BotAPI
from helpers.bot_setup import BotSetup
from models.room import BotRoomModel, RoomModel
from settings import utils
from services.payload import get_payload
from services.model_fields import get_model_fields
from logger_setup import logger

app = FastAPI()

origins = ["*"]

# Add CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"status": "API is running"}

@app.post("/api/createRoom")
@app.post("/api/createRoom/{bot}")
def create_room(room_model: BotRoomModel, bot: str = "bajaj"):

    kwargs = room_model.model_dump()

    logger.info(f"Creating room for bot: {bot} with kwargs: {kwargs}")
    token = utils.get_api_key()

    prompt = get_payload(bot, **kwargs)

    logger.info(f"Generated prompt: {prompt}")
    bot_setup = BotSetup(room_model.bot_model, prompt, room_model.max_duration)
    
    payload = bot_setup.get_payload()
    bot: BotAPI = BotAPI(token, payload)
    response = bot.start_bot()

    if response.status_code == 200:
        data = response.json()
        room_url = data["room_url"]
        token = data["token"]
        response_body = { "roomURL": f"{room_url}?t={token}"}
        logger.info(f"Room created successfully: {response_body}")
        return response_body
    else:
        logger.error(f"Failed to create room: {response.text}")
        return {"error": "Failed to create room"}
