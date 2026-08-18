file_path = "part01_basics/chapter10_file_and_exceptions/learning_python.txt"

# Method 1: Use read() to read the entire file as one string.
# with open(file_path) as file_object:
#     contents = file_object.read()

# print(contents)

# Method 2: Iterate over the file object to read the file line by line.
# with open(file_path) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# Method 3: Use readlines() to read all lines and store them in a list.
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# In Python, you can use dictionaries to store key-value pairs.
# In Python, you can create classes to model real-world things.
# In Python, you can import modules from the standard library to help you solve real-world problems.
# In Python, you can organize your projectâ€™s structure in different ways. Python provides many options for organizing your code efficiently.
