import openai, langchain, os

# from dotenv import load_dotenv
# load_dotenv()
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI

with open('server/data/extracted.txt','r') as f:
    text = f.readlines()
f.close()

chat = ChatOpenAI()

messages = [
    SystemMessage(content="You are responding to a loved one, they have dementia and you are not allowed to tell them that. Keep responses brief."),
    HumanMessage(content=f"{text}")
]

# print(chat(messages))

with open('server/data/response.txt','w') as f:
    f.write(chat(messages).content)

