# 1º Como usar el chatGPT desde un prompt engeneer:
# ERROR = You exceeded your current quota, please check your plan and billing details.
# API_KEY = "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" #"AQUI tu API_KEY"

import openai

file = open("api_key.txt", mode="r", encoding="utf8")
API_KEY = file.readline().rstrip()                              # quita el final de la line  el  LF o '\n'.
print("API_KEY = " , API_KEY)

openai.api_key = API_KEY

model_engine = "text-ada-001"

def respuesta(pregunta):
  completions = openai.Completion.create(engine=model_engine,
                                         prompt=pregunta,
                                         max_tokens=50,
                                         n=1,
                                         stop=None,
                                         temperature=0.5)
  return completions.choices[0].text.strip()

#------------- MAIN -------------------------------
pregunta = input("Pregunta : ")
if len(pregunta) > 3:
  response = respuesta(pregunta)
  print(response)
else:
  print("No Hizo una Pregunta adecuada!")