def make_shirt(size, text):
    prompt = f"\nThe size of the shirt is: {size}."
    prompt += f"\nThe message printed on it: {text.title()}"
    print(prompt)


make_shirt("5", "Love ya!")
make_shirt(size="6", text="E dep lam")

# The size of the shirt is: 5.
# The message printed on it: Love Ya!

# The size of the shirt is: 6.
# The message printed on it: E Dep Lam
