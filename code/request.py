from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
client = OpenAI()

# System prompt to limit chatbot to one-line stories
system_prompt = "You are a one-line storyteller. You must respond with exactly ONE sentence stories only. Keep stories short, creative, and entertaining."

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Write a bedtime story about a unicorn."}
    ]
)
print(response.choices[0].message.content)

