from translate import Translator

def translate_english_to_spanish(word):
    translator = Translator(from_lang='en', to_lang='es')
    translated_word = translator.translate(word)
    return translated_word

# Replace 'hello' with the word you want to translate
word_to_translate = 'hello'
translated_word = translate_english_to_spanish(word_to_translate)

print(f"{word_to_translate} in Spanish is: {translated_word}")
