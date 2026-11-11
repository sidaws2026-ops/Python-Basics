string1 = 'HIHello'
print(string1)
string1 = 'HI\nHello'
print("New line: " + string1)
string1 = 'HI\tHello'
print("Tab: " + string1)
string1 = 'HI\'Hello'
print("Single quote: " + string1)

string2 = "KAR"
string3 = "NATAK"

print("String concat: " + string2 + string3)

address = '''
AT Post: ABCD
PIN Code: 123456
House No: 123
Near XYZ temple ABCD
'''

print("Address is: "+ address)

string4 = "Python course " \
          "in kannda"
print(string4)


string5 = "Python course in kannada"
print(string5[5:11])
print(string5[7:11])
print(string5[:])
print(string5[7:-1])

formatted_string = f"Bangalore is the capital of {string2}{string3}"
print(formatted_string)