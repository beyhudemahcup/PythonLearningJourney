import requests
import json


api_key = "e62ce1a82a5b79c95844d639"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

conversions = {
    "USD": ["TRY", "EUR", "GBP", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS"],
    "TRY": ["USD", "EUR", "GBP", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS"],
    "EUR": ["USD", "TRY", "GBP", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS"],
    "GBP": ["USD", "TRY", "EUR", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS"],
    "AED": ["USD", "TRY", "EUR", "GBP", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS"],
    "AFN": ["USD", "TRY", "EUR", "GBP", "AED", "ALL", "AMD", "ANG", "AOA", "ARS"],
    "ALL": ["USD", "TRY", "EUR", "GBP", "AED", "AFN", "AMD", "ANG", "AOA", "ARS"],
    "AMD": ["USD", "TRY", "EUR", "GBP", "AED", "AFN", "ALL", "ANG", "AOA", "ARS"],
    "ANG": ["USD", "TRY", "EUR", "GBP", "AED", "AFN", "ALL", "AMD", "AOA", "ARS"],
    "AOA": ["USD", "TRY", "EUR", "GBP", "AED", "AFN", "ALL", "AMD", "ANG", "ARS"],
    "ARS": ["USD", "TRY", "EUR", "GBP", "AED", "AFN", "ALL", "AMD", "ANG", "AOA"]
}

exchange_currency = input("Enter your currency's abbreviation?\nUSD-TRY-EUR-GBP-AED-AFN-ALL-AMD-ANG-AOA-ARS\n->").upper()

if exchange_currency in conversions:
    options = '-'.join(conversions[exchange_currency])
    convert_currency = input(f"Enter your desired currency's abbreviation?\n{options}\n-> ").upper()
else:
    print("Invalid currency abbreviation.")

amount = int(input(f"How much {exchange_currency} would you like to exchange?\n->"))

result = requests.get(api_url + exchange_currency)

result_json = json.loads(result.text)

# returns exchange rate directly
exchange_rate = result_json["conversion_rates"][convert_currency]

calculated_exchange_rate = exchange_rate * amount
print(f"1 {exchange_currency} = {exchange_rate} {convert_currency}\n")

print(f"Your amount in {convert_currency} is {calculated_exchange_rate:.2f}")












