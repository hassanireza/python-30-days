# Day 21 🧬 - OOP: Inheritance & Polymorphism

<div align="center">

| [← Day 20: Previous Lesson](../day-20/README.md) | [🏠 Home](../../README.md) | [Day 22: Next Lesson →](../day-22/README.md) |
|:---|:---:|---:|

</div>

---

## Overview

Inheritance lets you build new classes on top of existing ones, reusing and extending their behavior. Polymorphism means different classes can share the same interface.

**What you will learn today:**

- Inheritance: `class Child(Parent)`
- Calling parent methods with `super()`
- Overriding methods
- Multiple inheritance (and when to avoid it)
- `isinstance()` and `issubclass()`
- Abstract base classes with `abc`

---

## Key Concepts

| Concept | Description |
|---|---|
| `inheritance` | A class can inherit all attributes and methods from a parent class. The child can override or extend them. |
| `super()` | Calls a method from the parent class. Essential when overriding `__init__` to properly initialize the parent. |
| `polymorphism` | Different classes can implement the same method name. Code that calls `animal.speak()` works for any animal type. |
| `ABC` | Abstract Base Class from the `abc` module. Forces subclasses to implement specific methods. |

---

## Code Examples

### Inheritance

```python
class Animal:
    """Base class for all animals."""

    def __init__(self, name: str, sound: str) -> None:
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}!"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.name!r})"


class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Woof")     # Call parent __init__

    def fetch(self, item: str) -> str:
        return f"{self.name} fetches the {item}!"


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, "Meow")

    def speak(self) -> str:                # Override parent method
        return f"{self.name} says {self.sound}... and ignores you."


# Polymorphism in action
animals: list[Animal] = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for animal in animals:
    print(animal.speak())   # Each calls its own version of speak()
```

### Abstract Base Classes

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract shape. All subclasses MUST implement area() and perimeter()."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        ...

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        ...

    def describe(self) -> str:
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius
```

---

## Today's Project: Animal Kingdom

> Build an animal class hierarchy with a base `Animal` class and multiple subclasses, each with unique behaviors.

**View the full project:** [project/solution.py](./project/solution.py)

```python
"""
Day 21 Project: Animal Kingdom
================================
Polymorphic animal class hierarchy.
"""
from abc import ABC, abstractmethod
import math


class Animal(ABC):
    """Abstract base class for all animals."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self._hunger = 5   # 0 (full) to 10 (starving)

    @property
    def hunger(self) -> int:
        return self._hunger

    @abstractmethod
    def speak(self) -> str:
        """Return the animal's vocalization."""
        ...

    @abstractmethod
    def move(self) -> str:
        """Return a description of how the animal moves."""
        ...

    def eat(self, food: str) -> str:
        self._hunger = max(0, self._hunger - 3)
        return f"{self.name} eats {food}. Hunger: {self._hunger}/10"

    def __str__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r}, age={self.age})"


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)
        self.breed = breed

    def speak(self) -> str:
        return f"{self.name} barks: WOOF WOOF!"

    def move(self) -> str:
        return f"{self.name} runs happily toward you."

    def fetch(self, item: str) -> str:
        return f"{self.name} ({self.breed}) fetches the {item}!"


class Cat(Animal):
    def __init__(self, name: str, age: int, indoor: bool = True) -> None:
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self) -> str:
        return f"{self.name} meows softly... then walks away."

    def move(self) -> str:
        return f"{self.name} slinks silently across the room."

    def purr(self) -> str:
        return f"{self.name} purrs contentedly."


class Bird(Animal):
    def __init__(self, name: str, age: int, can_fly: bool = True) -> None:
        super().__init__(name, age)
        self.can_fly = can_fly

    def speak(self) -> str:
        return f"{self.name} chirps melodically."

    def move(self) -> str:
        if self.can_fly:
            return f"{self.name} soars gracefully through the air."
        return f"{self.name} waddles along the ground."


def run_zoo(animals: list[Animal]) -> None:
    """Demonstrate polymorphism: same interface, different behaviors."""
    print("\n--- Zoo Report ---")
    for animal in animals:
        print(f"\n{animal}")
        print(f"  {animal.speak()}")
        print(f"  {animal.move()}")
        print(f"  {animal.eat('food')}")


def main() -> None:
    print("=" * 50)
    print("          ANIMAL KINGDOM")
    print("=" * 50)

    zoo: list[Animal] = [
        Dog("Rex", 3, "German Shepherd"),
        Cat("Whiskers", 5),
        Bird("Tweety", 2, can_fly=True),
        Dog("Buddy", 7, "Labrador"),
        Bird("Pingu", 4, can_fly=False),
    ]

    run_zoo(zoo)

    print(f"\n--- Type Checking ---")
    for animal in zoo:
        print(f"  {animal.name}: Dog? {isinstance(animal, Dog)}, Animal? {isinstance(animal, Animal)}")


if __name__ == "__main__":
    main()
```

---

## Knowledge Check

Before moving on, make sure you can explain each concept without looking at the lesson.

---

<div align="center">

| [← Day 20: Previous Lesson](../day-20/README.md) | [🏠 Home](../../README.md) | [Day 22: Next Lesson →](../day-22/README.md) |
|:---|:---:|---:|

</div>
