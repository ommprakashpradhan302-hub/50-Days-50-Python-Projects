# 🔗 Day 35 - URL Shortener

A Python program that converts long URLs into short links using the TinyURL API.

## 🎯 Objective

To create a URL Shortener that helps users generate compact links for easier sharing and accessibility.

## 🛠️ Concepts Used

- API Handling (HTTP Requests)  
- User Input  
- Error Handling  
- Data Display  
- String Validation  

## 📚 Required Libraries

This project uses the third‑party `requests` library.  

Install it using:

```bash
pip install requests
```

## ⚙️ How It Works

1. The user enters a long URL.  
2. The program validates that the URL starts with `http://` or `https://`.  
3. The program sends the URL to the TinyURL API.  
4. The API processes the request and returns a shortened URL.  
5. The shortened URL is displayed along with the original long URL.  
6. Errors (e.g., invalid URL or API issues) are handled gracefully.

## 💻 Example Output

```text
=== URL Shortener ===
Enter a long URL: https://www.example.com/tutorials/python-tutorial
Shortening URL, please wait...
✔ Short URL: https://tinyurl.com/3k8f7a2b
🔗 Long URL : https://www.example.com/tutorials/python-tutorial
```

*The shortened URL can be shared easily while still pointing to the original long URL.*

## 🧠 What I Learned

- Making API requests with `requests.get()`  
- Handling API responses and errors  
- Validating user input for proper URL format  
- Building a practical utility for link management  
- Automating real‑world tasks with Python

## ▶️ How to Run

```bash
python main.py
```

Make sure you have internet access and the `requests` library installed.

## 📁 Project Structure

```text
Day35_URLShortener/
│
├── main.py
└── README.md
```
#🚀 50 Days 50 Python Mini Projects
## 👨‍💻 Author

**Omm Prakash Pradhan**
B.Tech AI & ML Student

**Day 35/50** — Learn • Build • Improve


