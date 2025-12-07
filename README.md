🌍 Country Capitals Quiz

Generate fully randomized quizzes about world capitals — perfect for classrooms, training programs, and testing environments.

📌 Overview

This Python project automatically generates multiple unique quizzes and answer sheets based on a country data file.

Each student receives:

A quiz with randomized question order

Multiple-choice answers (A/B/C/D)

A separate answer key

This makes it impossible for students to cheat since every quiz is different.

🚀 Features

✔ Parses country_data.txt into a dictionary

✔ Generates N quizzes based on user input

✔ Randomizes:

Order of questions

Multiple-choice options

✔ Produces:

question1.txt, question2.txt, ...

answers1.txt, answers2.txt, ...

✔ Automatically deletes old quiz files

✔ Simple, clean Python implementation

📂 Project Structure
📦 Country Capitals Quiz
│
├── main.py               # Main program logic
├── country_data.txt      # Source data (countries + capitals)
├── question1.txt         # Auto-generated quiz (example)
├── answers1.txt          # Auto-generated answer key (example)
└── README.md             # Documentation

🧠 How It Works
1️⃣ User Input

The program prompts for:

Number of students

Number of questions per quiz

2️⃣ Parsing the Data

Reads country_data.txt and creates a dictionary like:

{
    "Egypt": "Cairo",
    "France": "Paris",
    "Japan": "Tokyo",
    ...
}

3️⃣ Generating Quizzes

For each student:

Creates a quiz file

Shuffles the list of countries

Generates 4-option multiple-choice answers

4️⃣ Generating Answer Keys

Creates a separate file containing:

1. B
2. D
3. A
...

🖥️ How to Run
python main.py


You will be asked:

how many question will be for each quiz:
how many student will participate in quiz:


Quiz and answer files will be created automatically.

📸 Example Output
Question File:
1. What is the capital city of Egypt?
    A. Cairo
    B. Rome
    C. Tunis
    D. Rabat

Answer File:
1. A
2. C
3. B
...

🛠️ Technologies Used

Python

File I/O

Random module

Text processing

📝 Possible Future Enhancements

Add difficulty levels

Export quizzes as PDF

Allow filtering by continent

Create a GUI version using Tkinter or PyQt

🤝 Contributing

Pull requests, improvements, and suggestions are welcome!

📜 License

Distributed under the MIT License.

⭐ If you like this project

Give it a star ⭐ on GitHub!
