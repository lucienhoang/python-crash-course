from collections import OrderedDict

glossary = OrderedDict()

glossary["range()"] = "return a list of key-value pairs"
glossary["tuple"] = "return a list of key-value pairs"
glossary["items()"] = "return a list of key-value pairs"
glossary["keys()"] = "return a list of keys"
glossary["values()"] = "return a list of values"


for key, meaning in glossary.items():
    print(f"Key: {key} -> meaning: {meaning}")

# Key: range() -> meaning: return a list of key-value pairs
# Key: tuple -> meaning: return a list of key-value pairs
# Key: items() -> meaning: return a list of key-value pairs
# Key: keys() -> meaning: return a list of keys
# Key: values() -> meaning: return a list of values
