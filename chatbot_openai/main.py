import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot(prompt, model="gpt-4"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "Jesteś pomocnym asystentem."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

while True:
    user_input = input("Ty: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("Bot:", chatbot(user_input))
