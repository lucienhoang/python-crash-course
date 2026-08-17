````markdown
# 🐍 Python Dictionary Looping Cheat Sheet

Quick reference for looping through dictionaries and lists of dictionaries.

---

## 1. Keys & Values

Use `.items()` when you need both the key and value.

```python
for key, value in my_dict.items():
    print(f"Key: {key} -> Value: {value}")
````

---

## 2. Keys Only

Use `.keys()` when you only need the keys.

```python
for key in my_dict.keys():
    print(key)
```

### Recommended

Python loops through keys by default, so `.keys()` can be omitted:

```python
for key in my_dict:
    print(key)
```

---

## 3. Values Only

Use `.values()` when you only need the values.

```python
for value in my_dict.values():
    print(value)
```

---

## 4. Remove Duplicate Values

Wrap `.values()` with `set()` to remove duplicates.

```python
for value in set(my_dict.values()):
    print(value)
```

---

# 🐾 List of Dictionaries

A list of dictionaries is useful for storing a collection of similar items.

```python
spike = {"name": "spike", "owner": "dung", "kind": "dog"}
tom = {"name": "tom", "owner": "khoa", "kind": "cat"}
jerry = {"name": "jerry", "owner": "laurence", "kind": "mouse"}

pets = [spike, tom, jerry]
```

---

## Variable Names vs. Data

Variable names exist only in the code.

If a name needs to be used as data, store it inside the dictionary:

```python
spike = {
    "name": "spike",
    "owner": "dung",
    "kind": "dog"
}
```

Here, `"name"` is the key and `"spike"` is the value.

---

## Clean Looping with `enumerate()`

Use `enumerate(..., start=1)` for automatic numbering.

Use `.title()` for cleaner text formatting.

```python
for index, pet in enumerate(pets, start=1):
    print(
        f"{index}. {pet['name'].title()} "
        f"is a {pet['kind']} living with {pet['owner'].title()}"
    )
```

### Output

```text
1. Spike is a Dog living with Dung
2. Tom is a Cat living with Khoa
3. Jerry is a Mouse living with Laurence
```

---

## 🧠 Quick Reference

| Goal              | Method              |
| ----------------- | ------------------- |
| Keys + values     | `.items()`          |
| Keys              | `.keys()` or `dict` |
| Values            | `.values()`         |
| Remove duplicates | `set()`             |
| Add index         | `enumerate()`       |
| Format text       | `.title()`          |

### Remember

```python
.items()     # keys + values
.keys()      # keys
.values()    # values
set()        # remove duplicates
enumerate()  # add index
```

:::
