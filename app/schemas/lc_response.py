from pydantic import BaseModel


# Define the request model
class SummarizeRequest(BaseModel):
    text: str
