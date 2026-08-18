# Is Your Birthday Contained in Pi

file_path_2 = "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/pi_milion_digits.txt"

with open(file_path_2) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first thousand digits of pi.")
else:
    print("Your birthday does not appears in the first thousand digits of pi.")

# Enter your birthday, in the form mmddyy: 311595
# Your birthday appears in the first thousand digits of pi.
