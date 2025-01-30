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

audio_file = open('meu_audio.mp3', 'rb')

transcription = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file,
    
)

print(transcription.text)