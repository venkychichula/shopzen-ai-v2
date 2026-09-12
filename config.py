import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    app_secret: str = os.getenv("APP_SECRET", "")
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")
    cors_origins: list[str] = None

    def __post_init__(self):
        object.__setattr__(
            self,
            "cors_origins",
            [x.strip() for x in os.getenv("CORS_ORIGINS", "*").split(",") if x.strip()]
            or ["*"],
        )

settings = Settings()
