import requests
import winsound
import yaml

# URL de la API de cambios de divisas
url = 'https://api.exchangerate-api.com/v4/latest/USD'

# si colocas la url saldra:
# {"provider":"https://www.exchangerate-api.com","WARNING_UPGRADE_TO_V6":"https://www.exchangerate-api.com/docs/free","terms":"https://www.exchangerate-api.com/terms","base":"USD","date":"2023-01-07","time_last_updated":1673049601,"rates":{"USD":1,"AED":3.67,"AFN":89.2,"ALL":108.3,"AMD":395.09,"ANG":1.79,"AOA":509.74,"ARS":178.59,"AUD":1.46,"AWG":1.79,"AZN":1.7,"BAM":1.84,"BBD":2,"BDT":102.68,"BGN":1.85,"BHD":0.376,"BIF":2058.43,"BMD":1,"BND":1.34,"BOB":6.92,"BRL":5.35,"BSD":1,"BTN":82.52,"BWP":12.85,"BYN":2.52,"BZD":2,"CAD":1.35,"CDF":2057.39,"CHF":0.93,"CLP":855.53,"CNY":6.85,"COP":4928.54,"CRC":591.69,"CUP":24,"CVE":103.9,"CZK":22.68,"DJF":177.72,"DKK":7.03,"DOP":56.27,"DZD":137.4,"EGP":25.1,"ERN":15,"ETB":53.64,"EUR":0.942,"FJD":2.2,"FKP":0.831,"FOK":7.03,"GBP":0.831,"GEL":2.7,"GGP":0.831,"GHS":10.29,"GIP":0.831,"GMD":63.07,"GNF":8706.83,"GTQ":7.85,"GYD":209.52,"HKD":7.81,"HNL":24.69,"HRK":7.1,"HTG":147.72,"HUF":373.29,"IDR":15632.44,"ILS":3.52,"IMP":0.831,"INR":82.52,"IQD":1460.52,"IRR":41998.01,"ISK":145.2,"JEP":0.831,"JMD":152.31,"JOD":0.709,"JPY":132.5,"KES":123.56,"KGS":85.57,"KHR":4134.53,"KID":1.46,"KMF":463.56,"KRW":1257.13,"KWD":0.307,"KYD":0.833,"KZT":465.1,"LAK":17162.42,"LBP":1507.5,"LKR":365.18,"LRD":154.84,"LSL":17.14,"LYD":4.81,"MAD":10.43,"MDL":19.22,"MGA":4481.12,"MKD":58.04,"MMK":2101.02,"MNT":3446.1,"MOP":8.04,"MRU":36.62,"MUR":43.84,"MVR":15.45,"MWK":1033.59,"MXN":19.18,"MYR":4.39,"MZN":64.14,"NAD":17.14,"NGN":449.41,"NIO":36.53,"NOK":10.05,"NPR":132.04,"NZD":1.58,"OMR":0.384,"PAB":1,"PEN":3.84,"PGK":3.53,"PHP":55.38,"PKR":227.15,"PLN":4.41,"PYG":7320.34,"QAR":3.64,"RON":4.63,"RSD":110.53,"RUB":72.49,"RWF":1103.37,"SAR":3.75,"SBD":8.4,"SCR":13.01,"SDG":546.95,"SEK":10.57,"SGD":1.34,"SHP":0.831,"SLE":18.97,"SLL":18974.76,"SOS":568.95,"SRD":31.67,"SSP":680.66,"STN":23.09,"SYP":2490.5,"SZL":17.14,"THB":33.88,"TJS":10.26,"TMT":3.5,"TND":3.13,"TOP":2.37,"TRY":18.77,"TTD":6.76,"TVD":1.46,"TWD":30.55,"TZS":2337.38,"UAH":36.76,"UGX":3718.79,"UYU":39.81,"UZS":11279.65,"VES":18.61,"VND":23491.54,"VUV":121.02,"WST":2.7,"XAF":618.09,"XCD":2.7,"XDR":0.748,"XOF":618.09,"XPF":112.44,"YER":250.48,"ZAR":17.17,"ZMW":18.25,"ZWL":698.32}}

# enviar una solicitud a la API y obtener la respuesta
response = requests.get(url)
if response.status_code == 200:
  print("Acceso Condedido\n")
  data_loaded = yaml.safe_load(response.text)
  print(f"data_loaded = {data_loaded} / len = {len(data_loaded['rates'])}")

  # obtener el valor de la moneda del diccionario de respuesta
  currency_value = data_loaded['rates']['EUR']

  # establecer el valor m�ximo permitido
  max_value = 0.9

  # si el valor de la moneda supera el valor m�ximo, reproducir un sonido de alarma
  if currency_value > max_value:
    winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
  else:
    print(f"Aun No ha llegado al valor maximo de {max_value}")
else:
  print("La URL no dio acceso 200")