# 4º Como pedirle una receta / resumen de una oracion si es valido o no: 
# en este caso NO es VALIDA.
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
# Tactic 3: Check whether conditions are satisfied:
# Ej: es cambiar '''{text}'''  por  \"\"\"{text}\"\"\"  p insertar un parrafo.
text_2 = f"""
The sun is shining brightly today, and the birds are singing. It's a beautiful day to go for a \ 
walk in the park. The flowers are blooming, and the trees are swaying gently in the breeze. People \ 
are out and about, enjoying the lovely weather. Some are having picnics, while others are playing \ 
games or simply relaxing on the grass. It's a perfect day to spend time outdoors and appreciate the \ 
beauty of nature.
"""
prompt = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, re-write those instructions in the following format:
Step 1 - ...
Step 2 - …
…
Step N - …
If the text does not contain a sequence of instructions, then simply write \"No steps provided.\"
\"\"\"{text_2}\"\"\"
"""
response = get_completion(prompt)
print("Completion for Text 2:")
print(response)

# out:
# Completion for Text 2:
# No steps provided.