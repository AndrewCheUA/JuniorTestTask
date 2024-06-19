from pathlib import Path


from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent

class Settings(BaseSettings):
    huggingfacehub_api_token: str = "huggingfacehub_api_token"

    class Config:
        env_file = BASE_DIR / '.env'


settings = Settings()