nums = [1,2,3,4,5,6,7,8]
names = ["sid", "ram", "laxmi", "Vijaya"]

# for num in nums:
# for name in names:
#     print(name)

# for num in range(5):
#     print(num)

# for name in range(len(names)):
#     print(names[name])

for name in range(len(names)):
    if names[name] == "laxmi":
        print(f"Found laxmi {name}")