from textblob import TextBlob

def translate_english_to_spanish(word):
    blob = TextBlob(word)
    translated_word = blob.translate(to='es')
    return str(translated_word)

# Replace 'hello' with the word you want to translate
word_to_translate = 'hello'
translated_word = translate_english_to_spanish(word_to_translate)

print(f"{word_to_translate} in Spanish is: {translated_word}")
