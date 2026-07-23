guest_lists = ["Dung Dung", "BongBang", "Thao Dung"]
print(guest_lists)
# ['Dung Dung', 'BongBang', 'Thao Dung']

stay_home = guest_lists.pop()
message = "Sorry " + stay_home.title() + ", I can't invite you"
print(message)
# Sorry Thao Dung, I can't invite you

stay_home = guest_lists.pop()
message = "Sorry " + stay_home.title() + ", I can't invite you"
print(message)
# Sorry Bongbang, I can't invite you

del guest_lists[0]
print("Lists of Guest:")
print(guest_lists)
# Lists of Guest:
# []
