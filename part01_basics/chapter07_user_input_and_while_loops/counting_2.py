currrent_number = 0

while currrent_number < 10:
    currrent_number += 1
    if currrent_number % 2 == 0:
        continue

    print(currrent_number)

# If the modulo is 0, the continue statements tells Python
# to ignore the rest of the loop and returning to the beginning.

# 1
# 3
# 5
# 7
# 9
