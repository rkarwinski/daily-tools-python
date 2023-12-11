import openai
import os
from dotenv import load_dotenv

load_dotenv()
ENGINE_OPENIA = os.getenv('ENGINE_OPENIA')

openai.api_key = os.getenv('API_KEY')

def obter_resposta(prompt):
    resposta = openai.chat.completions.create(
        model=ENGINE_OPENIA,
        messages=[
            {"role": "system", "content": "Você é um assistente virtual."},
            {"role": "user", "content": prompt}
        ]
    )
    return resposta['choices'][0]['message']['content'].strip()

pergunta = "Qual é o significado da vida?"
resposta_do_chatgpt = obter_resposta(pergunta)

print(f"Pergunta: {pergunta}")
print(f"Resposta do ChatGPT: {resposta_do_chatgpt}")
