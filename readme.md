# 🚀 Smart Error Log Analyser for DevOps

A lightweight and intelligent CLI tool designed to extract, group, and analyze error and warning messages from large log files—perfect for DevOps engineers and developers who need fast insights from noisy logs.

---

## 📌 Project Overview

**Smart Error Log Analyser** scans raw application/server log files, extracts lines with `ERROR` and `WARNING`, and clusters them by similarity using text fingerprinting techniques. The output is a clean, human-readable report that highlights:

- Unique error patterns
- Frequency of each error group
- Sample error messages from each group

---

## 💡 Key Features

- 🧠 **Fingerprint-based clustering** of similar log lines  
- 🔍 Extracts only relevant `ERROR` and `WARNING` lines  
- 📁 Supports custom input and output file paths via CLI  
- 📝 Generates organized TXT reports for quick review  
- 💥 Graceful error handling with clear terminal feedback

---

## 🛠️ Project Structure

📂 Smart Error Log Analyser/
- error_analyzer.py # Main CLI entry point
- utils.py # File reading and error extraction
- log_processor.py # Fingerprinting and clustering logic
- report_writer.py # Text report generation
- test_Main.txt # Sample log file
- README.md # Project documentation (you are here!)
