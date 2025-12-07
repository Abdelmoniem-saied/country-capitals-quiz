# 🌍 Country Capitals Quiz

Generate fully randomized quizzes about world capitals — perfect for classrooms, training programs, and testing environments.

---

## 📌 Overview

This Python project automatically generates multiple unique quizzes and answer sheets based on a country data file.

Each student receives:

- A quiz with randomized question order  
- Multiple-choice answers (A/B/C/D)  
- A separate answer key  

This makes it impossible for students to cheat since every quiz is different.

---

## 🚀 Features

- ✔ Parses `country_data.txt` into a dictionary  
- ✔ Generates **N quizzes** based on user input  
- ✔ Randomizes:
  - Order of questions  
  - Multiple-choice options  
- ✔ Produces:
  - `question1.txt`, `question2.txt`, ...  
  - `answers1.txt`, `answers2.txt`, ...  
- ✔ Automatically deletes old quiz files  
- ✔ Simple, clean Python implementation  

---

📦 Country Capitals Quiz
│
├── main.py               # Main program logic
├── country_data.txt      # Source data (countries + capitals)
├── question1.txt         # Auto-generated quiz (example)
├── answers1.txt          # Auto-generated answer key (example)
└── README.md             # Documentation



---

## 🧠 How It Works

### 1️⃣ User Input  
The program prompts for:
- Number of students  
- Number of questions per quiz  

---

### 2️⃣ Parsing the Data  
Reads `country_data.txt` and creates a dictionary like:

```python
{
    "Egypt": "Cairo",
    "France": "Paris",
    "Japan": "Tokyo",
    ...
}

### 3️⃣ Generating Quizzes

For each student:

- Creates a quiz file  
- Shuffles the list of countries  
- Generates 4-option multiple-choice answers  

---

### 4️⃣ Generating Answer Keys

Creates a separate file containing:

```text
1. B
2. D
3. A
...





