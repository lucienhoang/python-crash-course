def make_shirt(size="large", text="I love Python"):
    prompt = f"\nThe size of the shirt is: {size}."
    prompt += f"\nThe message printed on it: {text.title()}"
    print(prompt)


make_shirt()
make_shirt(size="medium")
make_shirt(size="anysize", text="Luci is the chosen one!")

# The size of the shirt is: large.
# The message printed on it: I Love Python

# The size of the shirt is: medium.
# The message printed on it: I Love Python

# The size of the shirt is: anysize.
# The message printed on it: Luci Is The Chosen One!
