# 🌐 Day 36 - Website Status Checker

A Python program that checks whether a website is up and running, returning the status code and response time.

## 🎯 Objective

To create a Website Status Checker that helps users monitor website availability and performance.

## 🛠️ Concepts Used

- API Handling (HTTP Requests)  
- Time Measurement  
- Conditional Statements  
- Exception Handling  
- User Input  
- Data Display  

## 📚 Required Libraries

This project uses the third‑party `requests` library.  

Install it using:

```bash
pip install requests
```

## ⚙️ How It Works

1. The user enters a website URL.  
2. If the URL does not start with `http://` or `https://`, the program automatically adds `https://`.  
3. The program sends a request to the website using `requests.get()`.  
4. Response time is calculated in milliseconds.  
5. The HTTP status code is checked:  
   - **200–399** → Website is UP ✅  
   - **400–499** → Client Error ⚠️  
   - **500–599** → Server Error ❌  
   - Others → Unknown Status ❓  
6. Results are displayed with status, code, and response time.  
7. Errors (e.g., unreachable site) are handled gracefully.

## 💻 Example Output

```text
Enter website URL (e.g., https://www.google.com): https://www.example.com

=== Website Status Checker ===
URL           : https://www.example.com
Status Code   : 200
Status        : ✅ Website is UP and running!
Response Time : 123.45 ms
```

*If the site is unreachable, the program displays: ❌ Website is DOWN or not reachable!*

## 🧠 What I Learned

- Sending HTTP requests with `requests`  
- Measuring response time using `time`  
- Handling different HTTP status codes  
- Managing exceptions for robust code  
- Building a practical monitoring tool  

## ▶️ How to Run

```bash
python main.py
```

Make sure you have internet access and the `requests` library installed.

## 📁 Project Structure

```text
Day36_WebsiteStatusChecker/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 36/50** — Learn • Build • Improve


