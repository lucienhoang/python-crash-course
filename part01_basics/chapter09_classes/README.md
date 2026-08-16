# Where Should This Responsibility Live?

A useful question when designing classes in OOP:

> **Where should this responsibility live?**

Instead of only asking:

> “Can this method work in this class?”

Ask:

> **“Which object should be responsible for this behavior?”**

---

## Example: `Car`, `ElectricCar`, and `Battery`

```python
class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 70:
            miles_range = 240
        elif self.battery_size == 85:
            miles_range = 270

        return miles_range


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()
```

Here:

```python
self.battery = Battery()
```

means an `ElectricCar` **has a** `Battery`.

```text
ElectricCar
    │
    └── battery
          │
          └── Battery
```

If `get_range()` depends only on the battery's capacity:

```text
battery_size → range
```

then it makes sense for `Battery` to own `get_range()`.

```python
my_tesla.battery.get_range()
```

---

## But What If the Calculation Changes?

Suppose range depends on the entire car:

```text
Battery
+ Weight
+ Motor efficiency
+ Aerodynamics
+ Tire type
```

Now `Battery` does not have enough information to determine the range.

In that case, `get_range()` may belong in `ElectricCar`:

```python
class ElectricCar:
    def get_range(self):
        # Use battery + other car attributes
        ...
```

Because range is now a behavior of the **whole car**, not just the battery.

---

## Key Principle

It is **not** about how many cars we have.

It is about **responsibility**.

> **Put the responsibility where the relevant data and behavior naturally belong.**

Ask:

1. What does this object represent?
2. What data does it own?
3. Which object should be responsible for this behavior?
4. Which class has the information needed to perform it?

---

## IS-A vs HAS-A

### Inheritance — IS-A

```python
class ElectricCar(Car):
    ...
```

```text
ElectricCar IS-A Car
```

### Composition — HAS-A

```python
self.battery = Battery()
```

```text
ElectricCar HAS-A Battery
```

---

## Mental Model

When designing classes, remember:

> **“Where should this responsibility live?”**

This question helps keep classes **focused, organized, and easier to maintain**.
