import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser # Vai abstrair o nosso response.content. Esse já traz diretamente a resposta.
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader

def configure():
    load_dotenv()

configure()

chave_api = os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-3.5-turbo'
)

# Importa a base de conhecimento em txt.
# loader = TextLoader('./bases_conhecimento/base_conhecimento.txt')

# Importa a base de conhecimento em pdf.
#loader = PyPDFLoader('./bases_conhecimento/base_conhecimento.pdf')

loader = CSVLoader('./bases_conhecimento/base_conhecimento.csv')

# Joga o conteúdo do arquivo na variável documents.
documents = loader.load()

# Criamos um prompt template e, pedimos respostas com base apenas no contexto passado (conteúdo do txt).
prompt_base_conhecimento = PromptTemplate(
    input_variables=['contexto', 'pergunta'],
    template=
    '''
    Use o seguinte contexto para responder à pergunta.
    Responda apenas com base nas informações fornecidas.
    Não utilize informações externas ao contexto:
    Contexto: {contexto}
    Pergunta: {pergunta}
    '''
)

# Chain para output.
chain = prompt_base_conhecimento | model | StrOutputParser()

# Invocamos a chain, passado o contexto (iteramos cada page_content do txt) e a pergunta para o modelo.
response = chain.invoke(
    {
        'contexto': '\n'.join(doc.page_content for doc in documents),
        'pergunta': 'Qual o carro mais novo?'
    }
)

print(response)