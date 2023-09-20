# Down from URL a csv file.
import requests

def import_data_files():
  r = requests.get('https://raw.githubusercontent.com/anyoneai/notebooks/main/customers_and_orders/data/customers.csv')
  with open('customers.csv', 'wb') as f:          # ./sample_data/customers.csv'
    f.write(r.content)

  r = requests.get('https://raw.githubusercontent.com/anyoneai/notebooks/main/customers_and_orders/data/orders.csv')
  with open('orders.csv', 'wb') as f:             # './sample_data/orders.csv'
    f.write(r.content)
  
import_data_files()
print("Customers and orders CSV files have been added './sample_data'")