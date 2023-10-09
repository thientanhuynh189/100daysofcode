# file1_list_final = []
# with open("file1.txt") as file1:
#     file1_list = file1.readlines()
#     for number in file1_list:
#         file1_list_final.append(number.strip())
#
# file2_list_final = []
# with open("file2.txt") as file2:
#     file2_list = file2.readlines()
#     for number in file2_list:
#         file2_list_final.append(number.strip())
#
# result = [number for number in file1_list_final if number in file2_list_final]
#
#
# # Write your code above 👆
#
# print(result)

# OR
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

print(result)