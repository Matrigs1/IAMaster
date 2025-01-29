import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

def configure():
    load_dotenv()

configure()

chave_api = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    api_key=chave_api
)

# Criando uma string que vai servir como template.
template = '''
    Traduza o texto do {idioma1} para o {idioma2}:
    {texto}
'''

# Montando template da classe.
prompt_template = PromptTemplate.from_template(
    template=template,
    
)

# Passando os valores para as interpolações.
prompt = prompt_template.format(
    idioma1='português',
    idioma2='inglês',
    texto='Boa tarde!'
)

# Invocando o modelo com o prompt passado.
response = model.invoke(prompt)
print(response.content)