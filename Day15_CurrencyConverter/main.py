import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_exchange_rates():
    try:
        response = requests.get(API_URL)
        data = response.json()
        return data["rates"]
    except Exception as e:
        print("⚠️ Error fetching exchange rates:", e)
        return None

def convert_currency(rates, from_curr, to_curr, amount):
    if from_curr not in rates or to_curr not in rates:
        return None
    
    # Convert amount from source currency to USD, then to target currency
    amount_in_usd = amount / rates[from_curr]
    converted_amount = amount_in_usd * rates[to_curr]
    return converted_amount

def main():
    print("💱 CURRENCY CONVERTER 💱")
    print("Base currency is USD (exchange rates are relative to USD)\n")

    rates = get_exchange_rates()
    if rates is None:
        return

    from_curr = input("👉 Enter source currency code (e.g., EUR): ").upper()
    to_curr = input("👉 Enter target currency code (e.g., INR): ").upper()

    try:
        amount = float(input("👉 Enter amount: "))
    except ValueError:
        print("⚠️ Invalid amount! Please enter a number.")
        return

    result = convert_currency(rates, from_curr, to_curr, amount)
    if result is None:
        print("⚠️ Invalid currency code(s)! Please try again.")
    else:
        print(f"✅ {amount} {from_curr} = {result:.2f} {to_curr}")

if __name__ == "__main__":
    main()
