name = "Sid" # string
age = 32 #int
account_balance = 10000.239 # float
is_hdfc_account = True # boolean

print(name)
print(age)
print(account_balance)
print(is_hdfc_account)

print("===============================")
# concat of string and int, float and bool is not possible in python  
# converted int, bool, and flot to string to print in a meaningful sentence

print("My name is " + name + " and I am " + str(age) + " old.")
print("I have a HDFC banck account " + str(is_hdfc_account) + " and I have balance amount of RS." + str(account_balance))
