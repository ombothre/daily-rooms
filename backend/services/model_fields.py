from pydantic import BaseModel

def get_model_fields(model: BaseModel) -> dict:
    return {field for field in model.model_fields.keys()}