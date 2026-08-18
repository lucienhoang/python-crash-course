from pathlib import Path

file_cat = Path(
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/cats.txt"
)
file_dog = Path(
    "D:/python-crash-course/part01_basics/chapter10_file_and_exceptions/dogs.txt"
)

for filename in [file_cat, file_dog]:
    try:
        with open(filename) as obj_file:
            print(obj_file.read())

    except FileNotFoundError:
        pass


# tom thomas tomcat
