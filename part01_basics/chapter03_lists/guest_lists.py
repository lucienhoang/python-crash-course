guest_lists = ["Dung Dung", "BongBang", "Thao Dung"]
print(guest_lists)
# ['Dung Dung', 'BongBang', 'Thao Dung']

invite_message = "Welcome you to my dinner, Mr. " + guest_lists[0] + "!"
print(invite_message)
# Welcome you to my dinner, Mr. Dung Dung!

print("I'm afraid Mr." + guest_lists[1] + " can't make it tonight!")
# I'm afraid Mr.BongBang can't make it tonight!

guest_lists[1] = "Laurence"
print("So I will call Mr." + guest_lists[1] + " for instead hehe")
print(guest_lists)
# So I will call Mr.Laurence for instead hehe
# ['Dung Dung', 'Laurence', 'Thao Dung']

print(
    "My gosh, there is so much love in me so I thinking about bring more folks to the table"
)
guest_lists.insert(0, "Lovelace")
guest_lists.insert(2, "Bro")
guest_lists.append("Khoa")
print(guest_lists)

# My gosh, there is so much love in me so I thinking about bring more folks to the table
# ['Lovelace', 'Dung Dung', 'Bro', 'Laurence', 'Thao Dung', 'Khoa']

print("Hello Everyone")
# Hello Everyone
