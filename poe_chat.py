"""
    This is an example of how to use Poe's GPT-3.5-Turbo model to generate responses.
"""

import asyncio
from fastapi_poe.types import ProtocolMessage
from fastapi_poe.client import get_bot_response


async def get_responses(user_input, api_key="ukkYm5SRphTXXIyo8WB3XJEZLucenG_fEyH1cM8jRVU"):
    message = ProtocolMessage(role="user", content=user_input)
    async for partial in get_bot_response(messages=[message], bot_name="GPT-3.5-Turbo", api_key=api_key):
        print(partial.text, end='')


def chat():
    while True:
        user_input = input("Please input your message: ")
        if user_input.lower() == "quit":
            break
        asyncio.run(get_responses(user_input))
        print()


if __name__ == "__main__":
    chat()
