# 5º En una conversacion de libreto ej entre un Padre y su Hijo, de froma metaforica, como a la
# IA le pregunta sobre el significado de la Resilencia, ya q el Padre se lo dice de forma metaforica
# y la IA es capaz de Interpretar el significado.
import openai

file = open("api_key.txt", mode="r", encoding="utf8")
API_KEY = file.readline().rstrip()                              # quita el final de la line  el  LF o '\n'.
print("API_KEY = " , API_KEY)

openai.api_key = API_KEY

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


#------------- MAIN -------------------------------
# Tactic 4: few-Shot prompting
# Give sucessful examples of completing task, then ask Model to performe a Task. 
# Ej de un dialogo y como la IA interpreta la metafora del padre a su hijo: "Resilencia"
# NOTA: cambiar '''{text}'''  por  \"\"\"{text}\"\"\"  p insertar un parrafo.
prompt = f"""
Your task is to answer in a consistent style.

<child>: Teach me about patience(paciencia).

<grandparent>: The river that carves the deepest valley flows from a modest spring; the \ 
grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
"""
response = get_completion(prompt)
print(response)

# OutPut:
# <grandparent>: Resilience is like a tree that bends with the wind but never breaks.
# It is the ability to bounce back from adversity and overcome challenges. Just like
# a tree needs strong roots to withstand the storm, we need to cultivate inner 
# strength and perseverance to be resilient.