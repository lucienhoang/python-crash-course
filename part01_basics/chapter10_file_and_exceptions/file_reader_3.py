# Making a List of Line from a Files

file_path_2 = (
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/pi_digits.txt"
)

with open(file_path_2) as file_object:
    lines = file_object.readlines()  # read all lines → list

for line in lines:
    print(line.rstrip())

#  3.1415926535
#    8979323846
#    2643383279
