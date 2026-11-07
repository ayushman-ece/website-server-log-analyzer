# 🛡️ Website Server Log Analyzer & Threat Detection System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Computing-013243?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)
![Status](https://img.shields.io/badge/Project-Completed-success)

A Python-based website server log analysis tool that monitors website traffic, identifies suspicious IP addresses, detects unusually high request activity, and generates traffic visualizations and security reports.

---

## 📌 Project Overview

Website servers continuously generate logs containing information about incoming requests, IP addresses, HTTP methods, response codes, and response times.

Analyzing these logs manually can be time-consuming.

This project automates the process using Python and data analysis libraries to help understand website traffic patterns and identify potentially suspicious activity.

## 🎯 Objectives

- Analyze website server logs automatically.
- Monitor incoming website requests.
- Identify active IP addresses.
- Analyze HTTP response status codes.
- Detect repeated failed requests.
- Identify unusually high request activity.
- Generate traffic visualization.
- Export traffic and security reports.

## ✨ Features

- **Log Data Validation:** Checks required columns, missing values, timestamps, IP addresses, and numeric fields.
- **Traffic Analysis:** Calculates total requests, unique IP addresses, and average response time.
- **IP Analysis:** Counts requests received from individual IP addresses.
- **HTTP Status Analysis:** Analyzes HTTP response codes.
- **Suspicious IP Detection:** Flags IP addresses with three or more failed requests (401 or 403).
- **High Activity Detection:** Identifies IP addresses making four or more requests in the analyzed dataset.
- **Traffic Visualization:** Generates a bar chart of requests by IP address.
- **CSV Report Generation:** Exports traffic and security analysis reports.

## ⚙️ Project Workflow

1. Load server log data from a CSV file.
2. Validate and clean the input data.
3. Analyze website traffic and request statistics.
4. Identify suspicious IP addresses.
5. Detect unusually high request activity.
6. Generate traffic visualization.
7. Export CSV reports.
8. Display the final analysis status.

## 🧠 Concepts Used

- Python Functions and Modular Programming
- Pandas DataFrames
- NumPy
- Data Grouping using `groupby()`
- Frequency Analysis using `value_counts()`
- IP Address Validation using `ipaddress`
- DateTime Handling
- Conditional Filtering
- Matplotlib Visualization
- CSV File Handling
- Exception Handling
- Basic Rule-Based Anomaly Detection

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| ipaddress | IP address validation |

## 📂 Project Structure

```text
server-log-analyzer/
│
├── main.py
├── analyzer.py
├── server_logs.csv
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

- `main.py` – Controls the complete project workflow.
- `analyzer.py` – Contains log validation, traffic analysis, detection, visualization, and report-generation functions.
- `server_logs.csv` – Sample website server log dataset.
- `requirements.txt` – Contains required Python libraries.
- `.gitignore` – Excludes virtual environments, cache files, and generated reports.
- `README.md` – Project documentation.

## 📊 Sample Analysis Results

Using the included sample dataset:

| Metric | Result |
|---|---:|
| Total Requests | 16 |
| Unique IP Addresses | 7 |
| Average Response Time | 183.75 ms |
| HTTP 200 Responses | 6 |
| HTTP 401 Responses | 4 |
| HTTP 403 Responses | 5 |
| HTTP 404 Responses | 1 |
| Suspicious IP Addresses | 2 |
| High-Activity IP Addresses | 3 |

## 📁 Generated Outputs

The project generates the following files:

| Output File | Description |
|---|---|
| `traffic_chart.png` | Website requests by IP address |
| `traffic_report.csv` | Request counts for individual IP addresses |
| `security_report.csv` | Suspicious IP and high-activity detection results |

## 🚀 Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/ayushman-ece/website-server-log-analyzer.git
```

### 2. Navigate to the project folder

```bash
cd website-server-log-analyzer
```

### 3. Create a virtual environment (optional)

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the project

```bash
python main.py
```

## 📦 Requirements

The project requires:

```text
pandas
numpy
matplotlib
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## 🔍 Detection Logic

### 1. Suspicious IP Detection

An IP address is flagged when it generates three or more failed requests with HTTP status codes:

- 401 – Unauthorized
- 403 – Forbidden

### 2. High Request Activity Detection

An IP address is flagged when it generates four or more requests in the analyzed dataset.

**Note:** These are basic rule-based detection methods. High request activity or repeated failed requests do not automatically prove malicious behavior.

## 📚 Learning Outcomes

Through this project, I learned:

- How to process and validate server log datasets.
- How to analyze website traffic using Pandas.
- How to group and summarize IP address activity.
- How HTTP status codes help identify failed requests.
- How to implement basic security detection rules.
- How to visualize traffic patterns.
- How to generate automated CSV reports.
- How to organize Python applications using modular programming.

## ⚠️ Limitations

- Uses a sample CSV dataset rather than live server logs.
- Detection thresholds are fixed.
- Does not perform real-time monitoring.
- Does not use machine learning for threat classification.
- High request volume alone cannot confirm an attack.
- Does not automatically block suspicious IP addresses.

## 🔮 Future Improvements

- Integrate real-time server log monitoring.
- Add time-window-based request analysis.
- Implement advanced anomaly detection.
- Integrate machine learning for threat classification.
- Build an interactive security dashboard.
- Add email or Telegram security alerts.
- Support larger server log datasets.

## 👨‍💻 Author

**Ayushman Tiwari**

- GitHub: [@ayushman-ece](https://github.com/ayushman-ece)

---

⭐ If you find this project useful, consider giving the repository a star!

**Project #84 — Website Server Log Analyzer & Threat Detection System**