from pydantic import BaseModel, ConfigDict
from models.bot import BotModel

class RoomModel(BaseModel):
    bot_model: BotModel
    max_duration: int = 100

class BotRoomModel(RoomModel):
    # extra allow
    model_config: ConfigDict = ConfigDict(extra="allow")