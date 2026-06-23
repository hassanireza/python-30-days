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
