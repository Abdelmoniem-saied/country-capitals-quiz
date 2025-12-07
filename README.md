# Country Capitals Quiz

This Python project generates quizzes for finding capitals of countries.
It reads a `country_data.txt` file and generates N quiz files and answer files,
one per student, with randomized multiple-choice questions.

## How to run

1. Make sure Python 3 is installed.
2. Open terminal in project folder.
3. Run:
4. Enter number of questions and number of students when prompted.
5. Quiz and answer text files will be generated in the same folder.

## Files
- `main.py` : main program
- `country_data.txt` : source data (country;capital;...)
- Generated: `question1.txt`, `answers1.txt`, etc.

## License
MIT

__pycache__/
*.pyc
*.pyo
*.pyd
env/
venv/
*.txt
!country_data.txt
