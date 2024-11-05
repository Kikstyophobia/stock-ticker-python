import constants
from openai import OpenAI
from stock_ticker import get_stock_data

client = OpenAI(
    api_key=constants.OPENAI_API_KEY
)


def chat_with_gpt(prompt, stock_list):

    payload = prompt + f"{get_stock_data(stock_list)}"

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": payload}
        ]
    )
    print(completion.choices[0].message.content)
