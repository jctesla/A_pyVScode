from datetime import datetime

# String de fecha
fecha_str = "09 oct 2024 08:32"

# Convertir el string a un objeto datetime
fecha = datetime.strptime(fecha_str, "%d %b %Y %H:%M")

# Extraer día, mes, hora y minuto
dia = fecha.day
mes = fecha.month  # El mes será un número (1-12)
hora = fecha.hour
minuto = fecha.minute

# Mostrar los resultados
print(f"Día: {dia}, Mes: {mes}, Hora: {hora}, Minuto: {minuto}")