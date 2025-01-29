import os
from dotenv import load_dotenv
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

def configure():
    load_dotenv()

configure()

chave_api = os.getenv('OPENAI_API_KEY')

wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        lang='pt'
    )
)

wikipedia_results = wikipedia.run('Quem foi Alan Turing?')
print(wikipedia_results)