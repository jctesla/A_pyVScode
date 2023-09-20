from googletrans import Translator

translator = Translator()
texto_a_traducir = "Hello, how are you?"
traduccion = translator.translate(texto_a_traducir, dest="es")

print(traduccion.text)