# 2º Como usar los delimitadores p insertar un parafo con otro Tactic 01:
import openai
import os

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
# Tactic 1: Use delimiters to clearly indicate distinct parts of the input
# Delimiters can be anything like: ```, """, < >, <tag> </tag>, :

# Ej: es cambiar '''{text}'''  por  <{text}>   p insertar un parrafo.
text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
<{text}>
"""
response = get_completion(prompt)
print(response)

# respuesta:
# Clear and specific instructions should be provided to guide a model 
# towards the desired output, and longer prompts can provide more clarity
# and context for the model, leading to more detailed and relevant outputs.