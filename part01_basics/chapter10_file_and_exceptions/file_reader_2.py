# Reading line by line

file_path_2 = (
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/pi_digits.txt"
)
with open(file_path_2) as file_object:
    for line in file_object:
        print(line.rstrip())


#  3.1415926535
#    8979323846
#    2643383279
