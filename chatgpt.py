from dotenv import load_dotenv
import os
from openai import OpenAI
from stock_ticker import get_stock_data

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def chat_with_gpt(prompt, data):

    payload = prompt + f"{data}"

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": payload}
        ]
    )
    print(completion.choices[0].message.content)