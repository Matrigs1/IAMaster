import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI                               
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain_experimental.utilities import PythonREPL
from langchain.prompts import PromptTemplate

def configure():
    load_dotenv()

configure()

chave_api = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-3.5-turbo',
)
