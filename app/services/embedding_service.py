import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


def create_embedding(text: str) -> list[float]:

    response = client.embeddings.create(
        model="baai/bge-m3",
        input=text,
    )

    return response.data[0].embedding
