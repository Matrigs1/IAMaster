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

# Geração de imagens.
response = client.images.generate(
    model='dall-e-3', # Modelo da LLM.
    prompt='Um Space Marine do Warhammer 40k', # O que gerar.
    size='1024x1024', # Tamanho da imagem (influencia no preço).
    quality='standard', # Qualidade da imagem (influencia no preço).
    n=1,
)

image_url = response.data[0].url
print(image_url)