cricketers = ["Sachin", "Dhoni", "Dravid", "Virat", "Kumble", "Gangualy"]
print(cricketers[4]) 
print(cricketers[:]) 
print(cricketers[1:5]) 
print(cricketers[-3]) 
cricketers[4] = "Anil"
print(cricketers)
heroes = ["Raj", "Shankarnag", "Vishnu", "Ambi", "Ravi", "Shivanna", "Ravi", "Punith"]

heroes.append("Uppi")
heroes.insert(2, "Ananthnag")
print(heroes.index("Ananthnag"))
print(heroes)
# heroes.index("Saddhu") # error use in another mehod as shown below
print("saddhu" in heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
print(heroes.count("Ravi"))
heroes_copy = heroes.copy()
print(heroes_copy)

cricketers.extend(heroes)
print(cricketers)

print(heroes.pop())
heroes.remove("Uppi")
print(heroes)

nums = [1, 2, 3, 4, 5, 20, 9, 24, 10]

nums.sort()
print(nums)

nums.reverse()
print(nums)

nums.clear()
print(nums)


#TOUPLE

my_marks = (70, 80, 90, 85, 80, 75)
# my_marks[2] = 99 # it will not work because touples are immutable
print(my_marks)

print(my_marks.count(80))
# print(my_marks)
print(my_marks.index(85))
