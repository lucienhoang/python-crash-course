# Large Files: One Million Digits

file_path_2 = "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/pi_milion_digits.txt"

with open(file_path_2) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")  # string slicing
# 3.14159265358979323846264338327950288419716939937510...
print(len(pi_string))
# 1002

# readlines()
#     ↓
#   list
#     ↓
# ["line 1", "line 2", "line 3", ...]
#        ↑
#      each line is a str
