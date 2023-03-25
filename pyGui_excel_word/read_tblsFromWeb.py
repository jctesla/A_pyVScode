import requests
import pandas as pd

url= 'https://www.openenglish.com/blog/es/verbos-mas-usados-en-ingles/'
html = requests.get(url).content
df_list = pd.read_html(html)

df = df_list[-1]
print(df)
df.to_csv('OutFromWeb.csv')



