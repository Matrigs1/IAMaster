import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI                               
from langchain_community.utilities.sql_database import SQLDatabase # Tool para realizar a conexão SQL.
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

def configure():
    load_dotenv()

configure()

chave_api = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-4',
)

# String de conexão com o SQLite.
db = SQLDatabase.from_uri('sqlite:///ipca.db')

# Cria e retorna uma lista de ferramentas para serem trabalhadas pelo Agent.
toolkit = SQLDatabaseToolkit(
    db=db,
    llm=model,
)

system_message = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm=model,
    tools=toolkit.get_tools(), # O parâmetro tools espera uma lista de tools, que é justamente o que o método get_tools do Toolkit retorna.
    prompt=system_message,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=True,
)

prompt = '''
Use as ferramentas necessárias para responder perguntas relacionadas ao histórico de IPCA ao longo dos anos.
Responda tudo em português brasileiro.
Perguntas: {q}
'''

prompt_template = PromptTemplate.from_template(prompt)

question = '''
Faça uma previsão dos próximos meses, até o final de 2025. Base nos dados históricos.
'''

output = agent_executor.invoke(
    {'input': prompt_template.format(q=question)}
)

print(output.get('output'))