# function hoisting is not possible in python
# wel_come()


def wel_come(firstName, lastName):
    print(f"Hi {firstName} {lastName}")
    print("Wel come to CTS")

# wel_come()

#To check order of execution
# print("Start")
# wel_come("Amazon", "com")
# wel_come("com", "Amazon") #It will work correctly i.e lastName takes value of firstName and viceversa
# wel_come(lastName="com", firstName="Amazon")
# print("End")

def send_mail():
    returned_value = amazon_greeting(False, "John")
    print(returned_value)
    print("Send mail...")                                                                         

def amazon_greeting(is_buyer, name):
    print("Hello "+name)
    if(is_buyer): 
        return "Wel come to Amazon BUYER Family!!"
    else:
        return "Wel come to Amazon Vendor Family!!"

# amazon_greeting(False, "John")

send_mail()