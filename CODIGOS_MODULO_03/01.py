import os
from langchain_openai import OpenAI

os.environ['OPENAI_API_KEY'] = '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'

model = OpenAI()

model.invoke(
    input=''
)