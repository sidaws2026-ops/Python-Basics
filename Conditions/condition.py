is_distinction = True
is_passed = True
if is_distinction:
    print("Awsome you passed with distinction")

elif is_passed:
    print("Congradulations!!!!")
    print("You have passed the exam")

else:
    print("Sorry you failed...")
    print("Please retake the exam")


is_mobile_price = 15000
is_google_pay = True

if is_google_pay:
    discount = 0.2 * is_mobile_price
else:
    discount = 0.1 * is_mobile_price

print(f"Discount is: {discount}")
# print("Discount is:" +  discount) #Error due to string + number

