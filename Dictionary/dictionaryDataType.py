#Adhar details dictionary
# my_adhar = {
#     "applicant_name": "Sid",
#     "mobile_number": 123467890,
#     "email_id":  "Sid@gmail.com",
#     "surname": "abc"
# }

# print(my_adhar)

# my_adhar["age"] = 34
# print(my_adhar)

# print(my_adhar["email_id"])
# # print(my_adhar["photo"])
# print(my_adhar.get("photo", "Kye does not exist"))


#Design English to Kannada translator dictionary

my_dict = {
    "there": "alli",
    "here": "elli",
    "one": 1
} 

user_input_word = input("Enter english word I will tell you kannada meaning of it: ")

words = user_input_word.split()

for word in words:
    print(my_dict.get(word, "Does not exist"))