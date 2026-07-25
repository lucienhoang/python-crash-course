glossary = {
    "list": "collection of items",
    "range()": "generate a series of numbers",
    "tuple": "an immutable list",
}

glossary["items()"] = "return a list of key-value pairs"
glossary["keys()"] = "return a list of keys"
glossary["values()"] = "return a list of values"


for key, meaning in glossary.items():
    print(f"Key: {key} -> meaning: {meaning}")

# Key: list -> meaning: collection of items
# Key: range() -> meaning: generate a series of numbers
# Key: tuple -> meaning: an immutable list
# Key: items() -> meaning: return a list of key-value pairs
# Key: keys() -> meaning: return a list of keys
# Key: values() -> meaning: return a list of values
