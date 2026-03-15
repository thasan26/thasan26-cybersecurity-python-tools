# thasan's Cybersecurity Python Tools

A beginner cybersecurity toolkit built using Python. This project demonstrates basic security concepts such as password strength checking, log analysis, and network port scanning.

Author: Tasfia Hasan

---

## Project Overview

This repository contains small Python tools designed to simulate common cybersecurity tasks. The goal of the project is to practice Python programming while learning basic security analysis techniques.

The tools included in this project help analyze passwords, server logs, and network ports, which are common tasks performed in cybersecurity and system administration.

---

## Tools Included

### 1. Password Strength Checker

This tool checks whether a password is strong, moderate, or weak based on several security rules.

The program checks:
- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Example usage:

Run the program using Python:

python password_checker.py

The program will ask the user to enter a password and will display whether the password is weak, moderate, or strong.

---

### 2. Log Analyzer

The log analyzer reads a server log file and analyzes the entries to identify patterns or suspicious activity.

Possible uses include:
- Counting repeated requests
- Identifying suspicious IP addresses
- Detecting unusual activity patterns in server logs

Run the program:

python log_analyzer.py

The tool reads data from the provided log file and prints analysis results.

---

### 3. Port Scanner

The port scanner checks which ports are open on a target system.

Open ports can reveal which services are running on a machine.

This tool demonstrates basic network scanning techniques used in cybersecurity.

Run the program:

python port_scanner.py

The program will scan ports and display which ones are open.

---

## Sample Data

The repository includes a sample file:

server_log.txt

This file is used by the log analyzer to demonstrate how log data can be analyzed.

---

## Technologies Used

This project was built using:

- Python
- Regular Expressions
- File Handling
- Socket Programming
- Basic Cybersecurity Concepts

---

## Learning Objectives

This project was created to practice and demonstrate:

- Python scripting
- Password security principles
- Log file analysis
- Network port scanning
- Basic cybersecurity concepts

---

## Future Improvements

Possible future improvements include:

- Adding a graphical user interface (GUI)
- Exporting results to a report file
- Adding more advanced log analysis
- Implementing vulnerability detection
- Creating automated security monitoring tools

---

## Disclaimer

This project was created for educational purposes only and should only be used in safe testing environments.
