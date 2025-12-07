import random
import os

for file_name in os.listdir():
    if file_name.endswith(".txt") and  not(file_name.startswith("country_data")):
        os.unlink(file_name)

question_count = int(input("how many question will be for each quiz: "))
student_count = int(input("how many student will participate in quiz: "))

countries = {}   

with open(r"udemy\Quiz using Files\country_data.txt", encoding="utf-8") as country_info:
    country_info.readline()
    for row in country_info:
        fields = row.rstrip().split(";")
        name , capital = fields[1:3]
        countries[name] = capital


for quiz_num in range(student_count):
    with open(f"question{quiz_num+1}.txt","w") as quiz_file:
        quiz_file.write('name:\n\nDate:\n\n')
        quiz_file.write(f'{' ' * 20} country capitals quiz (form{quiz_num+1})')
        quiz_file.write('\n\n')

        
        country_list= list(countries.keys())
        random.shuffle(country_list)
        

        for question_num in range(question_count):
            correct_answer=countries[country_list[question_num]]
            woring_answer=list(countries.values())
            del woring_answer[woring_answer.index(correct_answer)]
            


            woring_answer=random.sample(woring_answer,3)
            answer_options=woring_answer+[correct_answer]
            


            random.shuffle(answer_options)

            quiz_file.write(f"{question_num+1}.what is the capital city of {country_list[question_num]}?\n")



            for i in range(4):
                quiz_file.write(f"     {'ABCD'[i]}.{answer_options[i]}\n")
            quiz_file.write('\n')


            with open(f"answers{quiz_num+1}.txt","a") as answer_file:
                answer_file.write(f'{question_num+1}.{'ABCD'[answer_options.index(correct_answer)]}\n')  





