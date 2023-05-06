# 3º Como pedirle informacion estrcuturada Tactic 02:
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
# Tactic 2: 
prompt = f"""
Generate a list of three made-up book titles along \ 
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""
response = get_completion(prompt)
print(response)

# out:
# [
#   {
#   "book_id": 1,
#   "title": "The Lost City of Zorath",
#   "author": "Aria Blackwood",
#   "genre": "Fantasy"
# },
# {
#   "book_id": 2,
#   "title": "The Last Survivors",
#   "author": "Ethan Stone",
#   "genre": "Science Fiction"
# },
# {
#   "book_id": 3,
#   "title": "The Secret Life of Bees",
#   "author": "Lila Rose",
#   "genre": "Romance"
#  }
# ]