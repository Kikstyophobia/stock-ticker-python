import constants
from openai import OpenAI

client = OpenAI(
    api_key=constants.OPENAI_API_KEY
)


def chat_with_gpt(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message.content)


chat_with_gpt("how are you today?")
