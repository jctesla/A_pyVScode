# 4º Como pedirle una receta / resumen de una oracion si es valido o no:
# en este caso es VALIDA.
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
text_1 = f"""
Making a cup of tea is easy! First, you need to get some water boiling. While that's happening, \ 
grab a cup and put a tea bag in it. Once the water is hot enough, just pour it over the tea bag. \ 
Let it sit for a bit so the tea can steep. After a few minutes, take out the tea bag. If you \ 
like, you can add some sugar or milk to taste. And that's it! You've got yourself a delicious \ 
cup of tea to enjoy.
"""
prompt = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions,re-write those instructions in the following format:
Step 1 - ...
Step 2 - …
…
Step N - …
If the text does not contain a sequence of instructions, then simply write \"No steps provided.\"
\"\"\"{text_1}\"\"\"
"""

response = get_completion(prompt)
print(response)
# out:
# Step 1 - Get some water boiling.
# Step 2 - Grab a cup and put a tea bag in it.
# Step 3 - Once the water is hot enough, pour it over the tea bag.
# Step 4 - Let it sit for a bit so the tea can steep.
# Step 5 - After a few minutes, take out the tea bag.
# Step 6 - If you like, you can add some sugar or milk to taste.
# Step 7 - Enjoy your delicious cup of tea!


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