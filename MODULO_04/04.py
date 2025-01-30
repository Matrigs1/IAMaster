import os
from dotenv import load_dotenv
from langchain import hub                                                # Hub para importação de modelos pré-setados de instruções para a IA.
from langchain_openai import ChatOpenAI                               
from langchain_community.tools import DuckDuckGoSearchRun
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

prompt = '''
    Como assistente financeiro pessoa, que responderá às perguntas dando dicas financeiras e de investimento.
    Responda tudo em português brasileiro.
    Perguntas: {q}
'''

prompt_template = PromptTemplate.from_template(prompt)

# Primeira ferramenta.
# Aqui estamos instanciando um objeto PythonREPL, capaz de rodar código nativo.
python_repl = PythonREPL()
# Após instância, queremos que esse objeto vire uma Tool para ser usado com o langchain, então setados um nome para essa Tool, a função dela e, executamos passando o obj criado e, utilizando a função run.
python_rpl_tool = Tool(
    name='Python REPL',
    description='Um shell Python. Use isso para executar código Python. Execute apenas códigos Python válidos.'
    'Se você precisar obter o retorno do código, use a função "print(...)".'
    'Use para realizar cálculos financeiros necessários para responder as perguntas e dar dicas.',
    func=python_repl.run
)

# Segunda ferramenta.
search = DuckDuckGoSearchRun()
duckduckgo_tool = Tool(
    name='Busca DuckDuckGo',
    description='Útil para encontrar informações e dicas de economia, além de opções de investimento.'
                'Você sempre deve pesquisar na internet as melhores dicas usando esta ferramenta.'
                'Não responda diretamente, sua busca deve informar que há elementos pesquisados na internet.',
    func=search.run
)

# Aqui estamos importando instruções pré-setadas para a IA.
react_instructions = hub.pull('hwchase17/react')

# Como uma das premissas de um agente é justamente ter mais de uma ferramenta para interação, iremos mandar duas para esse.
tools = [python_rpl_tool, duckduckgo_tool]

# Criação do agente, passando o modelo de resposta, as ferramentas que criamos e, o modelo pré-setado de instruções.
agent = create_react_agent(
    llm=model,
    tools=tools,
    prompt=react_instructions
)

# O AgentExecutor é um orquestrador de agentes. Ele que vai colocá-los para rodar, passar as ferramentas para eles e, forncecer logs do funcionamento.
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

question = '''
    Minha renda é de R$10000 por mês. Tenho muitos cartões de crédito no total de R$12000 por mês.
    Tenho mais despesa de alguel e cumbustível de R$1500.
    Quais dicas você me dá?
'''

# Invocando o agent_executor e, passando o prompt com a pergunta para ele. Com base nesse prompt, as tarefas serão executadas.
output = agent_executor.invoke(
    {'input': prompt_template.format(q=question)}
)

print(output.get('output'))