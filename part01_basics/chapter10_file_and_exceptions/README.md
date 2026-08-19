# Reading and Writing Files in Python

Python provides several simple ways to read and write files.

## 1. `read()`

Reads the **entire file** as one string.

```python
with open("file.txt") as file:
    content = file.read()

print(content)
```

Use `read()` when you want to work with the whole file as a single string.

---

## 2. `readline()`

Reads **one line at a time**.

```python
with open("file.txt") as file:
    line = file.readline()

print(line)
```

Use `readline()` when you want to read lines one by one.

---

## 3. `readlines()`

Reads all lines and returns a **list of strings**.

```python
with open("file.txt") as file:
    lines = file.readlines()

print(lines)
```

Example:

```python
['Hello\n', 'Python\n', 'World\n']
```

Use `readlines()` when you want to work with each line as a list element.

---

## Writing to a File

Use the `"w"` mode to write to a file.

```python
with open("file.txt", "w") as file:
    file.write("Hello, Python!")
```

⚠️ `"w"` **overwrites** the existing content.

To add content without deleting existing content, use `"a"`:

```python
with open("file.txt", "a") as file:
    file.write("\nNew line")
```

---

## Quick Summary

| Method / Mode | Purpose             | Returns     |
| ------------- | ------------------- | ----------- |
| `read()`      | Read the whole file | `str`       |
| `readline()`  | Read one line       | `str`       |
| `readlines()` | Read all lines      | `list[str]` |
| `"w"`         | Write / overwrite   | —           |
| `"a"`         | Append to file      | —           |

### Remember

- `read()` → **whole file**
- `readline()` → **one line**
- `readlines()` → **list of lines**
- `"w"` → **write / overwrite**
- `"a"` → **append**

- str is immutable, so string methods don't modify the original string; they return a new string instead.
- [View remember_me.py](./remember_me.py)
