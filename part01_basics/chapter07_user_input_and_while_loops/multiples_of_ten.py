number = input(
    "Enter a number, and i will tell you if your num is a multiples of ten or not: "
)

number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiples of ten")
else:
    print(f"The number {number} is not a multiples of ten")


# Enter a number, and i will tell you if your num is a multiples of ten or not: 30
# The number 30 is a multiples of ten
