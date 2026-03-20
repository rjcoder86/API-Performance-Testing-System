# 🚀 APTS - API Performance Testing System

APTS is a CLI-based API performance testing tool built in Python.  
It helps developers analyze API performance, simulate load, detect failures, and understand why APIs fail.

---

## 🎯 Features

- ✅ Supports GET, POST, PUT, DELETE APIs
- ✅ Concurrent load testing
- ✅ Response time analysis (avg, min, max)
- ✅ Success rate calculation
- ✅ Error classification (HTTP errors, timeout, connection issues)
- ✅ Authentication support (Bearer token)
- ✅ Custom headers support
- ✅ JSON request body support
- ✅ Performance rating system
- ✅ CLI-based lightweight tool

---

## 🧱 Project Structure
```
APTS/
│
├── apts/
│   ├── cli.py
│   ├── request_sender.py
│   ├── load_tester.py
│   ├── metrics.py
│   ├── report.py
│
├── main.py
├── requirements.txt
└── README.md
```


---

## ⚙️ Installation

### 1. Clone the repository

git clone <your-repo-url>
cd APTS


### 2. Create virtual environment (optional)


python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows


### 3. Install dependencies


pip install -r requirements.txt


---

## ▶️ Usage

### 🔹 Basic Syntax


python main.py --url <API_URL> [OPTIONS]


---

## 🧪 Examples

### 🔸 GET API


python main.py --url https://jsonplaceholder.typicode.com/posts


---

### 🔸 Load Testing


python main.py
--url https://jsonplaceholder.typicode.com/posts

--requests 100
--concurrency 10


---

### 🔸 Authenticated API


python main.py
--url http://localhost:8000/api/users/

--token YOUR_ACCESS_TOKEN


---

### 🔸 Authenticated API (Auto Login)


python main.py \
--url http://localhost:8000/api/users/ \
--login-url http://localhost:8000/api/login/ \
--credentials - {"username":YOUR_USERNAME, "password":PASSWORD}\
--token-field - Token field in login response


---

### 🔸 POST API


python main.py
--url http://localhost:8000/api/users/

--method POST
--data '{"name": "RJ"}'
--header "Content-Type: application/json"


---

### 🔸 PUT API


python main.py
--url http://localhost:8000/api/users/1/

--method PUT
--data '{"name": "Updated"}'


---

### 🔸 DELETE API


python main.py
--url http://localhost:8000/api/users/1/

--method DELETE


---

### 🔸 Custom Headers


python main.py
--url http://localhost:8000/api/data/

--header "Content-Type: application/json"
--header "X-API-KEY: abc123"


---

## 📊 Sample Output

🚀 Starting API Test...
Endpoint : http://localhost:8000/api/users/

Method : GET
Total Requests : 100
Concurrency : 10
Authentication : Enabled
Request Body : None
API Performance Report

Total Requests: 100
Success Rate: 85.00%

Why API is failing:
HTTP_401: 10 requests
HTTP_500: 5 requests

Average Response Time: 0.312 sec
Min Response Time: 0.120 sec
Max Response Time: 0.821 sec
Performance Rating: Good 👍


---

## 📈 Performance Rating Criteria

| Avg Response Time | Rating |
|------------------|--------|
| < 200 ms         | Excellent 🚀 |
| 200-500 ms       | Good 👍 |
| 500ms - 1s       | Moderate ⚡ |
| > 1s             | Poor 🐢 |

---

## ⚠️ Notes

- JSON body must be valid format
- Token should be passed without "Bearer" keyword (handled internally)
- For POST/PUT, ensure correct Content-Type header

---

## 🚀 Future Improvements

- 🔹 Auto login & token generation
- 🔹 API scenario testing (multi-step flow)
- 🔹 JSON report export
- 🔹 Web dashboard
- 🔹 AI-based optimization suggestions

---

## 👨‍💻 Author

Rohit Jadhav  
Python Backend Developer

---

## 📌 License

This project is for learning and portfolio purposes.
