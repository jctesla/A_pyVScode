# I got this error from the example you brigme of tranlating "AttributeError: 'NoneType' object has no attribute 'group'"?
# I apologize for the inconvenience. The error you encountered, 'NoneType' object has no attribute 'group', is a known issue with the googletrans library.
# This error may occur when the library's usage exceeds the Google Translate API rate limits, and the library receives a response with empty or None values.
# Unfortunately, as of my knowledge cutoff date in September 2021, the googletrans library had some issues with reliability and was prone to rate-limiting 
# problems. As a result, it may not be the most stable choice for production use.

# hacer esto para que funciones:
# pip uninstall googletrans
# pip install googletrans==3.1.0a0
from googletrans import Translator

def translate_english_to_spanish(word):
    translator = Translator()
    translated = translator.translate(word, src='en', dest='es')
    return translated.text

# Replace 'hello' with the word you want to translate
word_to_translate = 'hello'
translated_word = translate_english_to_spanish(word_to_translate)

print(f"{word_to_translate} in Spanish is: {translated_word}")
