is_learned_python = True
is_degree = False

#Loical and operator
# if is_learned_python and is_degree:
#     print("Shortlisted for the interview")

#Loical or operator
# if is_learned_python or is_degree:
#     print("Shortlisted for the interview")

#Loical not operator
if is_learned_python and not is_degree:
    print("Shortlisted for the interview")

else:
    print("Best of luck!!!!")

#comparison operator

student_marks = 35

#student passed scenario
# if student_marks >= 25:
#     print("Passed")
#student failed scenario
# if student_marks <= 25:
#     print("Passed")

# if student_marks == 35:
#     print("Passed")
if student_marks != 35:
    print("Passed")
else:
    print("Failed")


# Exceresise KM to Miles -> Miles to KM

distance = float(input("Enter the distance covered in: "))
unit = input("Type of unit eighter K or M: ")

if unit.upper() == "K":
    converted = distance/1.609
    print(f"You have covered {converted} miles")
elif unit.upper() == "M":
      converted = distance * 1.609
      print(f"You have covered {converted} KM's")
else:
    print("wrong input")
