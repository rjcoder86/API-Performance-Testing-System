# 🚀 API Performance Testing System (APTS)

APTS is a Python-based toolkit designed to **test, analyze, and optimize API performance**.

It evolves from a simple CLI-based load testing tool into a powerful **API profiling and optimization system**.

---

## 🎯 Vision

APTS aims to help developers and testers:

* Measure API performance under load
* Identify failure patterns and bottlenecks
* Detect inefficient database usage
* Suggest areas for optimization in backend code

---

## 🚀 Project Evolution

### 🔹 Version 1 – API Testing Engine

A CLI-based tool for testing API performance and reliability.

#### ✅ Features

* API testing (GET, POST, PUT, DELETE)
* Concurrent load testing
* Response time metrics (avg, min, max)
* Success rate calculation
* Error classification (401, 500, timeout, etc.)
* Authentication support:

  * Bearer token
  * Auto login via credentials
* Custom headers & JSON body support
* CLI-based execution with detailed output

👉 📂 [Explore Version 1](./version1)

---

### 🔹 Version 2 – API Optimization Engine (In Progress 🚧)

An internal profiling system to analyze backend API performance.

#### 🔥 Planned Features

* Decorator-based API profiling
* Execution time tracking
* Database query count analysis
* Slow query detection
* N+1 query identification (heuristic)
* Response size tracking
* Optimization suggestions:

  * `select_related` / `prefetch_related`
  * Query reduction strategies
* Developer-friendly performance reports

👉 📂 [Explore Version 2](./version2)

---

## 🧱 Project Structure

```
API-Performance-Testing-System/
│
├── version1/        # CLI-based API testing tool
├── version2/        # API profiling & optimization system
└── README.md        # Project overview
```

---

## 🧠 Key Concepts Used

* Multithreading (ThreadPoolExecutor)
* API request lifecycle handling
* Performance metrics calculation
* Error classification & observability
* CLI tool development
* Authentication workflows
* Django ORM query analysis (V2)
* Modular architecture design

---

## 💡 Why This Project?

Most API tools focus on either:

* Testing (like Postman), or
* Monitoring (like enterprise tools)

APTS aims to bridge the gap by providing:

👉 **Lightweight + Developer-friendly + Insight-driven API analysis**

---

## 🚀 Future Roadmap

* Scenario-based API workflows (multi-step testing)
* JSON report export
* Retry & stability testing
* AI-based optimization suggestions
* Web dashboard for visualization

---

## 👨‍💻 Author

**Rohit Jadhav**
Python Backend Developer

---

## 📌 License

This project is for learning, experimentation, and portfolio purposes.
