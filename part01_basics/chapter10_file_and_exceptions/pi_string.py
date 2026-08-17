# Working with File's content
from decimal import Decimal

file_path_2 = (
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/pi_digits.txt"
)

with open(file_path_2) as file_object:
    lines = file_object.readlines()

pi_srting = ""
for line in lines:
    pi_srting += line.strip()

print(pi_srting)
# 3.141592653589793238462643383279
print(len(pi_srting))
# 32
pi_number = Decimal(pi_srting)
print(pi_number + 1)
# 4.141592653589793238462643383
