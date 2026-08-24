# 💱 Day 15 - Currency Converter

A Python Currency Converter that converts an amount from one currency to another using the latest exchange rates fetched from an online API.

## 🎯 Objective

To create a Currency Converter that allows users to convert an amount from one currency to another using up-to-date exchange rates.

## 🛠️ Concepts Used

- User Input
- Dictionaries
- API Requests
- JSON Data
- Conditional Statements
- Calculations
- Output Formatting
- Functions
- Error Handling

## 📚 Required Libraries

This project uses the third-party `requests` library.

Install it using:

```bash
pip install requests
```

## 🌐 API Used

The program fetches the latest exchange rates using an online Exchange Rate API. The rates are provided relative to USD.

## ⚙️ How It Works

1. The program requests the latest exchange rates from the API.
2. The API response is converted into JSON data.
3. The exchange-rate dictionary is extracted from the response.
4. The user enters the source currency code.
5. The user enters the target currency code.
6. The user enters the amount to convert.
7. The program converts the source amount to USD and then to the target currency.
8. The converted amount is displayed with two decimal places.
9. Invalid currency codes and invalid amounts are handled with error messages.

## 💻 Example Output

```text
💱 CURRENCY CONVERTER 💱
Base currency is USD (exchange rates are relative to USD)

Enter source currency code (e.g., EUR): EUR
Enter target currency code (e.g., INR): INR
Enter amount: 100

100.0 EUR = 8931.47 INR
```

*Exchange rates are live and may differ from the example output.*

## 🧠 What I Learned

- Working with APIs in Python
- Sending HTTP requests using `requests`
- Parsing JSON data
- Working with dictionaries
- Performing currency conversion calculations
- Handling invalid user input
- Building a practical real-world utility

## ▶️ How to Run

```bash
python main.py
```

Make sure you have an active internet connection because the program fetches exchange rates from an online API.

## 📁 Project Structure

```text
Day15_CurrencyConverter/
│
├── main.py
├── README.md
└── requirements.txt
```

## 📦 requirements.txt

```text
requests
```

## 🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 15/50** — Learn • Build • Improve
