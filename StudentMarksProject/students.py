def calculate_highest_score(students_list):
    
    highest_score_in_maths = 0
    highest_score_in_maths_student_name = ""

    for student in students_list:
        if student.get("Maths") > highest_score_in_maths:
            highest_score_in_maths = student.get("Maths")
            highest_score_in_maths_student_name = student.get("name")

    print(f"Highest score in maths is {highest_score_in_maths} taken by {highest_score_in_maths_student_name}")




student_1 = {
"Maths": 45,
"Social": 80,
"Science": 82,
"name": "John"
}

student_2 = {
"Maths": 65,
"Social": 75,
"Science": 90,
"name": "Root"
}

student_3 = {
"Maths": 95,
"Social": 70,
"Science": 96,
"name": "Jimmy"
}

student_list = [student_1, student_2, student_3]
calculate_highest_score(student_list)