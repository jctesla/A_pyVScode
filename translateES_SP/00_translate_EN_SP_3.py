from translate_api import TranslateAPI

def translate_english_to_spanish(word):
    translator = TranslateAPI()
    translated_word = translator.translate(word, source='en', target='es')
    return translated_word

# Replace 'hello' with the word you want to translate
word_to_translate = 'hello, this is my last Sync to changes all about Py'
translated_word = translate_english_to_spanish(word_to_translate)

print(f"{word_to_translate} in Spanish is: {translated_word}")
