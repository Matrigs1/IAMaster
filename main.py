from openai import OpenAI
from creds import API_KEY

# Autenticação da conta.
client = OpenAI(
    api_key=API_KEY,
)

message = client.chat.completions.create(
    model = 'gpt-3.5-turbo', # Modelo do chat.
    # Prompt como usuário.
    messages = [
        {
            'role': 'system', 'content': 'Dê respostas técnicas sobre programação. Se comporte como um programador Python experiente especialista em padrões de projetos e arquitetura limpa.' # Dando um contexto a IA, que irá retornar informações mais apuradas.
        },
        {
            'role': 'user',
            'content': 'Me mostre como posso fazer um projeto Django com as melhores boas práticas.'
        }
    ],
    stream = False # Automaticamente é False, o que faz com que a resposta seja gerada e, somente enviada após completamente formulada.
)

print(message.choices[0].message.content)

# # A stream retorna continuamente porções de resposta, que podem ser iteradas e retornadas, assim como no chat GPT.
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end = '')