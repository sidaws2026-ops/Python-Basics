text = "Microdegree is learnng platform. Lerned AWS from  Microdegree"

count = 0
convert_to_list = text.split(" ")

for item in convert_to_list:
    if("Microdegree" == item):
        count+=1
       
print(count)  
   