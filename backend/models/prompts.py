from pydantic import BaseModel

class Default(BaseModel):
    name: str = "John"

class Bajaj(BaseModel):
    customer_name: str = "om"
    ai_name: str = "bajaj"
    total_due: float = 10000.0
    emi_amount: float = 5000.0

class HDFC(BaseModel):
    name: str = "abc"