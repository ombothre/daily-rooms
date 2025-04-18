from pydantic import BaseModel
from typing import Optional

class TTS(BaseModel):
    service: str

class STT(BaseModel):
    model: str = "nova-2-general"
    language: str = "en"

class LLM(BaseModel):
    service: str
    model: str
    system_prompt: Optional[str] = None

class BotModel(BaseModel):
    bot_profile: str
    tts: TTS
    stt: STT
    llm: LLM