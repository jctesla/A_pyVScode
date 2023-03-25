import os
import openai

#openai.api_key = os.getenv("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")     # Set the API key
openai.api_key = "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"     # Set the API key

# prompt = "What is the capital of France?"
# Define the prompt (the text you want the API to generate)

def crea_pregutna(pregunta):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt= pregunta,
    temperature=0.5,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  return response

# make a request:
pregunta = input(f"Ingresa una Pregunta : ")

if len(pregunta) > 3:

  # Send the request to the API
  #response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=2048)
  # Print the response
  respuesta = crea_pregutna(pregunta)
  print(respuesta["choices"][0]["text"])
else:
  print("No Hay pregunta Correcta!")   

