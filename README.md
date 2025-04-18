# dailybots-room

Backend Setup
```
cd backend
uvicorn main:app --reload
```

Route
```
POST http://127.0.0.1:8000/api/createRoom
```

Body
```
{
    "bot_model": {
        "bot_profile": "natural_conversation_2024_11",
        "tts": {
            "service": "cartesia"
        },
        "stt": {
            "model": "deepgram",
            "language": "en"
        },
        "llm": {
            "service": "anthropic",
            "model": "gpt-4",
            "system_prompt": "You are a helpful assistant."
        }
    },
    "max_duration": 300
}
```

Response
```
{
    "roomURL": "https://..........."
}
```
"# daily-rooms" 
