# 🚀 APTS - API Performance Testing System (Version 1)

APTS is a lightweight CLI-based API performance testing tool built in Python.  
It allows developers to measure API response times, perform concurrent load testing, and generate performance ratings.

This project is designed as a foundational version (V1) of a larger system that will later include static code analysis and intelligent optimization suggestions.

---

## 🎯 Features (Version 1)

- ✅ Single API request performance analysis
- ✅ Concurrent load testing
- ✅ Average / Min / Max response time calculation
- ✅ Success rate calculation
- ✅ Performance rating system
- ✅ CLI-based interface
- ✅ Lightweight and framework independent

---

## 🧱 Project Structure


APTS/
│
├── apts/
│ ├── __init__.py
│ ├── cli.py
│ ├── request_sender.py
│ ├── load_tester.py
│ ├── metrics.py
│ ├── report.py
│
├── requirements.txt
├── main.py
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the repository


git clone <your-repo-url>
cd APTS


### 2️⃣ Create virtual environment (Recommended)


python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows


### 3️⃣ Install dependencies


pip install -r requirements.txt


---

## ▶️ Usage

### 🔹 Single Request Test


python main.py --url http://localhost:8000/users


### 🔹 Load Testing


python main.py --url http://localhost:8000/users
 --requests 200 --concurrency 20


---

## 🧪 Example with Public API


python main.py --url https://jsonplaceholder.typicode.com/posts
 --requests 100 --concurrency 10


---

## 📊 Sample Output

API Performance Report
URL: https://jsonplaceholder.typicode.com/posts

Total Requests: 100
Success Rate: 100.00%
Average Response Time: 0.1823 sec
Min Response Time: 0.1204 sec
Max Response Time: 0.4211 sec
Performance Rating: Excellent

---

## 📈 Performance Rating Criteria

| Average Response Time | Rating     |
|-----------------------|------------|
| < 200ms               | Excellent  |
| 200ms - 500ms         | Good       |
| 500ms - 1s            | Moderate   |
| > 1s                  | Poor       |

---

## 🛠 Technologies Used

- Python 3
- requests
- concurrent.futures (ThreadPoolExecutor)
- argparse
- statistics

---

## 🚀 Future Roadmap (Upcoming Versions)

### 🔹 Version 2
- Database query analysis
- Middleware integration for Django/FastAPI
- N+1 query detection
- JSON report export

### 🔹 Version 3
- Static code analysis using AST
- Optimization suggestion engine
- AI-powered code improvement recommendations
- Web dashboard interface

---

## 🎯 Why This Project?

APTS was built to:

- Understand real-world API performance bottlenecks
- Learn profiling and load testing techniques
- Build production-style CLI tools
- Showcase backend engineering capability

---

## 👨‍💻 Author

Rohit Jadhav  
Python Backend Developer  

---

## 📌 License

This project is for learning and portfolio purposes.