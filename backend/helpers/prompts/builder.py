from abc import ABC, abstractmethod
from datetime import datetime

class PromptBuilder(ABC):
    def get_time_based_greeting(self) -> str:
        current_hour = datetime.now().hour
        if current_hour < 12:
            return "Good Morning"
        elif current_hour < 18:
            return "Good Afternoon"
        else:
            return "Good Evening"
        
    @abstractmethod
    def get_prompt(self, **kwargs) -> str:
        pass
