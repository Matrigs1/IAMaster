from openai import OpenAI
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

configure()

# Autenticação da conta.
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)

message = client.chat.completions.create(
    model = 'gpt-3.5-turbo', # Modelo do chat.
    # Prompt como usuário.
    messages = [
        {
            'role': 'system',
            'content': 'Você será um tradutor de textos de português para inglês. Apenas traduza e responda a tradução do texto que receber.' # Dando um contexto a IA, que irá retornar informações mais apuradas.
        },
        {
            'role': 'user',
            'content': 'O livro está na mesa.'
        }
    ],
    stream = False, # Automaticamente é False, o que faz com que a resposta seja gerada e, somente enviada após completamente formulada.
    max_tokens=200,
)

print(message.choices[0].message.content)

# # A stream retorna continuamente porções de resposta, que podem ser iteradas e retornadas, assim como no chat GPT.
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end = '')