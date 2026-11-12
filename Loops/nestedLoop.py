#Nested 2D list numbers exmple
# nums = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]

# print(nums[1][2])
# for num_list in nums:
#     print(num_list)
#     for num in num_list:
#         print(num)

#Nested 2D list strings exmple
cricket_teams = [
    ["Dhoni", "Virat", "Rohit"],
    ["Sachin", "Shewag", "Ganguly"],
    ["Kapil", "Amarnath", "Siddu"]
]

print(cricket_teams[2][1])

for cricket_team in cricket_teams:
    print(cricket_team)
    for ind_player in cricket_team:
        print(ind_player)