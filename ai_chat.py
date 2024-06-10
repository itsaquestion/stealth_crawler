from openai import OpenAI
from os import getenv
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.


# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=getenv("OR_KEY"),
)

def chat(prompt, model='openai/gpt-4o'):
    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": 'https://cc.imtass.me', # Optional, for including your app on openrouter.ai rankings.
        "X-Title": 'stealth_crawler', # Optional. Shows in rankings on openrouter.ai.
    },
    model=model,
    messages=[
        {
        "role": "user",
        "content": prompt,
        },
    ],
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    print(chat('Say: This is a test.', model = 'openai/gpt-3.5-turbo'))