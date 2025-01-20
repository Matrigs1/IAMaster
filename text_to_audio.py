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

response = client.audio.speech.create(
    model='tts-1',
    voice='nova',
    input='Salve o tricolor paulista, amado clube brasileiro, tu és forte tu és grande, dentre os grandes, é o primeiro.',
)

response.write_to_file('meu_audio.mp3')