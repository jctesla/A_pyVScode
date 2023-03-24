lbl="hola amigos voy a dividir esta frase en diferentes partes"
for i in range(2,16):                                                     # un bucle para divir por frases en grupos de 2 a 16 letras
	partes = [lbl[idx:idx+i]  for idx,itm in enumerate(lbl)   if idx%i==0]  # 
	print(partes)

# Grupos de 2 a 16 letras:
# 02 letras = ['ho', 'la', ' a', 'mi', 'go', 's ', 'vo', 'y ', 'a ', 'di', 'vi', 'di', 'r ', 'es', 'ta', ' f', 'ra', 'se', ' e', 'n ', 'di', 'fe', 're', 'nt', 'es', ' p', 'ar', 'te', 's']
# 03 letras = ['hol', 'a a', 'mig', 'os ', 'voy', ' a ', 'div', 'idi', 'r e', 'sta', ' fr', 'ase', ' en', ' di', 'fer', 'ent', 'es ', 'par', 'tes']
# 04 letras = ['hola', ' ami', 'gos ', 'voy ', 'a di', 'vidi', 'r es', 'ta f', 'rase', ' en ', 'dife', 'rent', 'es p', 'arte', 's']
# 05 letras = ['hola ', 'amigo', 's voy', ' a di', 'vidir', ' esta', ' fras', 'e en ', 'difer', 'entes', ' part', 'es']
# 06 letras = ['hola a', 'migos ', 'voy a ', 'dividi', 'r esta', ' frase', ' en di', 'ferent', 'es par', 'tes']
# 07 letras = ['hola am', 'igos vo', 'y a div', 'idir es', 'ta fras', 'e en di', 'ferente', 's parte', 's']
# 08 letras = ['hola ami', 'gos voy ', 'a dividi', 'r esta f', 'rase en ', 'diferent', 'es parte', 's']
# 09 letras = ['hola amig', 'os voy a ', 'dividir e', 'sta frase', ' en difer', 'entes par', 'tes']
# 10 letras = ['hola amigo', 's voy a di', 'vidir esta', ' frase en ', 'diferentes', ' partes']
# 11 letras = ['hola amigos', ' voy a divi', 'dir esta fr', 'ase en dife', 'rentes part', 'es']
# 12 letras = ['hola amigos ', 'voy a dividi', 'r esta frase', ' en diferent', 'es partes']
# 13 letras = ['hola amigos v', 'oy a dividir ', 'esta frase en', ' diferentes p', 'artes']
# 14 letras = ['hola amigos vo', 'y a dividir es', 'ta frase en di', 'ferentes parte', 's']
# 15 letras = ['hola amigos voy', ' a dividir esta', ' frase en difer', 'entes partes']