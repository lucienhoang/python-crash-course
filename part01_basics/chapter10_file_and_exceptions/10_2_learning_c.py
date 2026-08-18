file_path = "part01_basics/chapter10_file_and_exceptions/learning_python.txt"

# Method 2: Iterate over the file object to read the file line by line.
with open(file_path) as file_object:
    for line in file_object:
        line = line.replace("Python", "C")
        print(line.rstrip())

# In C, you can use dictionaries to store key-value pairs.
# In C, you can create classes to model real-world things.
# In C, you can import modules from the standard library to help you solve real-world problems.
# In C, you can organize your projectâ€™s structure in different ways. C provides many options for organizing your code efficiently.
