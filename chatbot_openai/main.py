import openai
from openai import OpenAI

client = OpenAI(api_key="sk-proj-...")

def chatbot(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # lub inny dostępny model
        messages=[
            {"role": "system", "content": "Jesteś pomocnym chatbotem."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


while True:
    user_input = input("Ty: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("Bot:", chatbot(user_input))
