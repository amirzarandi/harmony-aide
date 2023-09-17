import openai, langchain, os

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(openai_api_key = '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')

messages = [
    SystemMessage(content="You are responding to a loved one, they have dementia and you are not allowed to tell them that. Keep responses brief."),
    HumanMessage(content="Hello dear, how was your day.")
]

# print(chat(messages))

with open('server/data/response.txt','w') as f:
    f.write(chat(messages).content)

