import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser # Vai abstrair o nosso response.content. Esse já traz diretamente a resposta.

def configure():
    load_dotenv()

configure()

chave_api = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-3.5-turbo'
)

# prompt_template = PromptTemplate.from_template(
#     'Me fale sobre o carro {carro}'
# )

chain = (
    PromptTemplate.from_template(
        'Me fale sobre o carro {carro}.'
    )
    | model
    | StrOutputParser()
)

# runnable_sequence = prompt_template | model | StrOutputParser()

response = chain.invoke({'carro': 'Marea 20v 1999'})
print(response)
