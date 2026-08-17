# Relative file path
file_path_1 = "part01_basics/chapter10_file_and_exceptions/pi_digits.txt"

# Absolute file path
file_path_2 = (
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/pi_digits.txt"
)

with open(file_path_2) as file_object:
    contents = file_object.read()  # read entire file
    print(contents.rstrip())


#  3.1415926535
#    8979323846
#    2643383279
