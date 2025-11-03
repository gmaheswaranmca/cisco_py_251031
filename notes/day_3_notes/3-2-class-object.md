## Introduction to OOP using Python

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of attributes (often called properties or fields), and code in the form of methods (functions associated with the object).

### Key Concepts of OOP

- **Class**: A blueprint for creating objects. Defines the structure and behavior (attributes and methods) that the objects created from the class will have.
- **Object**: An instance of a class. Each object can have unique attribute values but shares the structure and behavior defined by its class.
- **Encapsulation**: Bundling data and methods that operate on that data within one unit (class). It restricts direct access to some of the object's components.
- **Inheritance**: Mechanism by which one class can inherit attributes and methods from another class, promoting code reuse.
- **Polymorphism**: Ability to use a common interface for different data types. Methods can be overridden in derived classes to provide specific behavior.

### Why Use OOP in Python?

- **Modularity**: Code is organized into classes, making it easier to manage and maintain.
- **Reusability**: Classes can be reused across programs, and inheritance allows for extending existing code.
- **Maintainability**: Encapsulation helps protect data integrity and makes code easier to update.
- **Flexibility**: Polymorphism and dynamic binding allow for flexible and extensible code.

### Python and OOP

Python is a multi-paradigm language that supports OOP. Classes are defined using the `class` keyword, and objects are created by instantiating classes. Python's OOP model is simple and powerful, making it easy to create and manage complex systems.

#### Example

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy")
my_dog.bark()  # Output: Buddy says woof!
```

In this example:
- `Dog` is a class.
- `my_dog` is an object (instance) of the class `Dog`.
- `name` is an instance attribute.
- `bark` is a method.

OOP in Python encourages writing clean, reusable, and organized code, making it suitable for both small scripts and large applications.

```
```

## Classes and Class Attributes

### What is a Class?

A **class** in Python is a user-defined blueprint for creating objects. It encapsulates data (attributes) and behavior (methods) that are common to all objects of that type. Classes are defined using the `class` keyword.

```python
class Car:
    pass
```

### Class Attributes

**Class attributes** are variables that are shared among all instances of a class. They are defined within the class body but outside any instance methods. Class attributes are accessed using the class name or through instances (though all instances share the same value unless explicitly overridden).

#### Defining Class Attributes

```python
class Car:
    wheels = 4  # class attribute

    def __init__(self, color):
        self.color = color  # instance attribute
```

- `wheels` is a class attribute, shared by all `Car` objects.
- `color` is an instance attribute, unique to each object.

#### Accessing Class Attributes

```python
print(Car.wheels)  # Access via class: 4

car1 = Car("red")
car2 = Car("blue")
print(car1.wheels)  # Access via instance: 4
print(car2.wheels)  # Access via instance: 4
```

#### Modifying Class Attributes

Class attributes can be changed using the class name. Changing the attribute via the class affects all instances unless an instance overrides it.

```python
Car.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6
```

If you assign a value to a class attribute via an instance, it creates an instance attribute with the same name, shadowing the class attribute.

```python
car1.wheels = 8
print(car1.wheels)  # 8 (instance attribute)
print(car2.wheels)  # 6 (still class attribute)
print(Car.wheels)   # 6
```

### Use Cases for Class Attributes

- Storing constants or default values shared by all instances.
- Keeping track of data relevant to the class as a whole (e.g., counting instances).

#### Example: Counting Instances

```python
class Dog:
    count = 0  # class attribute

    def __init__(self, name):
        self.name = name
        Dog.count += 1

d1 = Dog("Fido")
d2 = Dog("Rex")
print(Dog.count)  # Output: 2
```

### Summary

- Class attributes are shared across all instances.
- They are defined directly in the class body.
- Useful for constants, default values, and class-wide data.
- Can be accessed and modified via the class or instances (with caveats).



```
```

## Instances and Instance Attributes

### What is an Instance?

An **instance** is a specific object created from a class. Each instance has its own unique identity and can hold data that is distinct from other instances of the same class.

```python
class Person:
    pass

p1 = Person()
p2 = Person()
```
Here, `p1` and `p2` are two separate instances of the `Person` class.

### Instance Attributes

**Instance attributes** are variables that belong to a specific object (instance) of a class. They are typically initialized in the `__init__` method and are unique to each instance.

#### Defining Instance Attributes

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # instance attribute
        self.age = age        # instance attribute
```
- `self.name` and `self.age` are instance attributes, unique to each `Person` object.

#### Accessing Instance Attributes

Instance attributes are accessed using the dot notation on the instance.

```python
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(p1.name)  # Alice
print(p2.name)  # Bob
```

#### Modifying Instance Attributes

Instance attributes can be changed independently for each object.

```python
p1.age = 31
print(p1.age)  # 31
print(p2.age)  # 25
```

#### Dynamic Addition of Instance Attributes

You can add new attributes to an instance at runtime.

```python
p1.address = "123 Main St"
print(p1.address)  # 123 Main St
```
Other instances do not have this attribute unless explicitly added.

### Instance vs Class Attributes

- **Instance attributes** are unique to each object; changes affect only that object.
- **Class attributes** are shared among all instances unless shadowed by an instance attribute.

### Example: Using Instance Attributes

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 6)

print(rect1.area())  # 12
print(rect2.area())  # 30
```

### Summary

- Instances are individual objects created from a class.
- Instance attributes store data unique to each object.
- Defined in the `__init__` method or dynamically.
- Accessed and modified via the instance.
- Enable objects to maintain their own state.


```
```

## Binding and Method Invocation

### What is Binding?

**Binding** refers to the association between a method and the object (instance) it operates on. In Python, methods are functions defined inside a class. When accessed via an instance, they are automatically bound to that instance, meaning the instance is passed as the first argument (`self`).

### Method Invocation

**Method invocation** is the process of calling a method on an object. The syntax is `object.method(arguments)`. Python automatically passes the instance as the first argument to the method.

#### Example

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())  # Output: 78.5
```

Here, `area()` is invoked on the instance `c`. Python binds `c` to `self` inside the method.

### Bound vs Unbound Methods

- **Bound method**: Accessed via an instance, automatically receives the instance as `self`.
- **Unbound method**: Accessed via the class, requires the instance to be passed explicitly.

```python
print(Circle.area(c))  # Output: 78.5
```

### The `self` Parameter

- `self` is a reference to the current instance.
- It allows methods to access and modify instance attributes.

### Static and Class Methods

- **Instance methods**: First parameter is `self`.
- **Class methods**: Decorated with `@classmethod`, first parameter is `cls` (the class itself).
- **Static methods**: Decorated with `@staticmethod`, no automatic first parameter.

```python
class Example:
    @classmethod
    def show_class(cls):
        print("Class method:", cls)

    @staticmethod
    def show_static():
        print("Static method")

Example.show_class()   # Class method: <class '__main__.Example'>
Example.show_static()  # Static method
```

### Method Resolution Order (MRO)

When invoking a method, Python searches for it in the instance, then the class, then base classes (following MRO).

### Summary

- Binding links methods to instances or classes.
- Method invocation passes the instance or class automatically.
- Use `self` for instance methods, `cls` for class methods.
- Static methods do not receive automatic parameters.
- Understanding binding is key to using OOP features in Python effectively.


```
```


## Composition, Subclassing, and Derivation

### Composition

**Composition** is a design principle where a class contains objects of other classes as attributes, allowing complex types to be built from simpler ones. It models "has-a" relationships.

#### Example

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def drive(self):
        self.engine.start()
        print("Car is moving")
```

Here, `Car` is composed of an `Engine` object. Composition promotes code reuse and modularity.

### Subclassing

**Subclassing** is the process of creating a new class (subclass) that inherits attributes and methods from an existing class (base or parent class). The subclass can extend or override the behavior of the parent.

#### Example

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Subclassing
    def speak(self):
        print("Dog barks")
```

`Dog` is a subclass of `Animal` and overrides the `speak` method.

### Derivation

**Derivation** is another term for subclassing or inheritance. It refers to the creation of a new class based on an existing one, inheriting its properties and behaviors.

#### Multiple Inheritance

Python supports multiple inheritance, where a class can inherit from more than one parent class.

```python
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()   # Flying
d.swim()  # Swimming
```

### Benefits and Use Cases

- **Composition**: Preferred for code reuse and flexibility; changes in composed classes do not affect the containing class directly.
- **Subclassing/Derivation**: Useful for extending or customizing behavior; promotes code reuse through inheritance.

### Summary

- Composition builds complex objects from simpler ones.
- Subclassing/Derivation creates specialized classes from general ones.
- Use composition for "has-a" relationships, subclassing for "is-a" relationships.
- Both techniques are fundamental to OOP design in Python.

```
```


## Inheritance

### What is Inheritance?

**Inheritance** is a fundamental concept in object-oriented programming that allows a class (child or subclass) to inherit attributes and methods from another class (parent or superclass). It enables code reuse, extension, and organization of related classes.

### Types of Inheritance in Python

- **Single Inheritance**: A subclass inherits from one parent class.
- **Multiple Inheritance**: A subclass inherits from multiple parent classes.
- **Multilevel Inheritance**: A subclass inherits from a parent, which itself inherits from another class.
- **Hierarchical Inheritance**: Multiple subclasses inherit from a single parent class.

### Syntax

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    pass

c = Child()
c.greet()  # Output: Hello from Parent
```

### Overriding Methods

A subclass can override methods from its parent to provide specialized behavior.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

cat = Cat()
cat.speak()  # Output: Cat meows
```

### The `super()` Function

`super()` allows access to methods and attributes of the parent class, useful for extending or customizing inherited behavior.

```python
class Bird:
    def fly(self):
        print("Bird flies")

class Parrot(Bird):
    def fly(self):
        super().fly()
        print("Parrot flies in circles")

p = Parrot()
p.fly()
# Output:
# Bird flies
# Parrot flies in circles
```

### Inheritance and the `__init__` Method

If a subclass defines its own `__init__`, it should call the parent’s `__init__` using `super()` to ensure proper initialization.

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
```

### Method Resolution Order (MRO)

Python uses MRO to determine the order in which base classes are searched when executing a method. Use `ClassName.__mro__` or `help(ClassName)` to inspect MRO.

### Benefits of Inheritance

- **Code reuse**: Common functionality is defined once in the parent.
- **Extensibility**: Subclasses can extend or modify behavior.
- **Organization**: Related classes are grouped logically.

### Limitations

- Overuse can lead to complex hierarchies.
- Changes in parent classes can affect all subclasses.

### Summary

- Inheritance enables sharing and extension of code.
- Subclasses can override or extend parent behavior.
- Use `super()` for cooperative method calls.
- Supports multiple inheritance and MRO for method lookup.
- Essential for building scalable and maintainable OOP systems in Python.


```
```


## Built-in Functions for Classes, Instances, and Objects

Python provides several built-in functions that are useful for working with classes, instances, and objects. These functions help inspect, manipulate, and interact with objects at runtime.

### Common Built-in Functions

- **`type(obj)`**  
    Returns the type (class) of an object.
    ```python
    type(42)         # <class 'int'>
    type(my_object)  # <class '__main__.MyClass'>
    ```

- **`isinstance(obj, cls)`**  
    Checks if an object is an instance of a class or a tuple of classes.
    ```python
    isinstance(42, int)           # True
    isinstance(my_object, MyClass) # True
    ```

- **`issubclass(sub, super)`**  
    Checks if a class is a subclass of another class or a tuple of classes.
    ```python
    issubclass(bool, int)         # True
    issubclass(MyClass, object)   # True
    ```

- **`hasattr(obj, name)`**  
    Returns `True` if the object has an attribute with the given name.
    ```python
    hasattr(my_object, 'x')       # True or False
    ```

- **`getattr(obj, name[, default])`**  
    Gets the value of an attribute; returns `default` if not found.
    ```python
    getattr(my_object, 'x', 0)    # Returns value of x or 0
    ```

- **`setattr(obj, name, value)`**  
    Sets the value of an attribute.
    ```python
    setattr(my_object, 'x', 10)
    ```

- **`delattr(obj, name)`**  
    Deletes an attribute from an object.
    ```python
    delattr(my_object, 'x')
    ```

- **`dir(obj)`**  
    Returns a list of valid attributes and methods for the object.
    ```python
    dir(my_object)
    ```

- **`vars(obj)`**  
    Returns the `__dict__` attribute of an object, showing its instance attributes.
    ```python
    vars(my_object)
    ```

- **`callable(obj)`**  
    Checks if the object is callable (e.g., a function or method).
    ```python
    callable(my_function)         # True
    ```

### Special Functions and Attributes

- **`__class__`**  
    Every object has a `__class__` attribute pointing to its class.
    ```python
    obj.__class__
    ```

- **`__dict__`**  
    Dictionary of an object's writable attributes.
    ```python
    obj.__dict__
    ```

- **`__bases__`**  
    Tuple of base classes for a class.
    ```python
    MyClass.__bases__
    ```

### Use Cases

- **Introspection**: Discover object structure and capabilities at runtime.
- **Dynamic attribute access**: Manipulate attributes programmatically.
- **Type checking**: Ensure objects are of expected types for safety.

### Summary

Built-in functions make Python's OOP model flexible and dynamic, supporting introspection, attribute management, and type checking. They are essential tools for advanced object-oriented programming and metaprogramming.


```
```

## Overview of Built-in Python Classes and Modules

Python provides a rich set of built-in classes and modules that support object-oriented programming and facilitate development.

### Built-in Classes

- **Basic Data Types**:  
    - `int`, `float`, `complex`: Numeric types.
    - `str`: Immutable text sequences.
    - `list`, `tuple`, `set`, `dict`: Collection types.
    - `bool`: Boolean values.
- **Object Base Class**:  
    - All classes implicitly inherit from `object`, which provides default implementations for methods like `__str__`, `__repr__`, `__eq__`, etc.

### Common Built-in Modules for OOP

- **`collections`**:  
    Provides specialized container datatypes like `namedtuple`, `deque`, `Counter`, `OrderedDict`, `defaultdict`.
- **`abc` (Abstract Base Classes)**:  
    Allows creation of abstract classes and enforcement of method implementation in subclasses using `@abstractmethod`.
- **`dataclasses`**:  
    Simplifies creation of classes for storing data with automatic generation of methods like `__init__`, `__repr__`, and `__eq__`.
- **`types`**:  
    Contains definitions for dynamic type creation and inspection.
- **`enum`**:  
    Supports creation of enumerated constants.
- **`functools`**:  
    Provides higher-order functions and decorators, useful for method wrapping and class customization.

### Example: Using `dataclasses`

```python
from dataclasses import dataclass

@dataclass
class Point:
        x: int
        y: int

p = Point(1, 2)
print(p)  # Output: Point(x=1, y=2)
```

### Example: Using `abc` for Abstract Classes

```python
from abc import ABC, abstractmethod

class Animal(ABC):
        @abstractmethod
        def speak(self):
                pass

class Dog(Animal):
        def speak(self):
                print("Woof!")
```

### Utility and Support

- **Introspection**: Built-in functions like `dir()`, `type()`, and modules like `inspect` help examine objects and classes at runtime.
- **Inheritance and Customization**: All user-defined classes inherit from `object`, enabling customization of behavior via special methods (`__init__`, `__str__`, etc.).
- **Standard Library Modules**: Many modules (e.g., `threading`, `logging`, `unittest`) are implemented using classes and encourage OOP practices.

### Summary

Python's built-in classes and modules provide foundational support for OOP, making it easy to create, extend, and manage objects. They offer ready-to-use data structures, abstract base classes, and utilities for introspection and customization, enabling robust and maintainable object-oriented designs.

```
```

## Classes and Objects in Python – Cheatsheet

### OOP Basics
- **Class**: Blueprint for objects; defines attributes and methods.
- **Object/Instance**: Created from a class; holds unique data.
- **Encapsulation**: Bundles data and methods; restricts direct access.
- **Inheritance**: Subclass inherits from parent; enables code reuse.
- **Polymorphism**: Same interface, different implementations.

### Classes & Class Attributes
- Defined with `class` keyword.
- **Class attributes**: Shared by all instances; defined in class body.
- Access via `ClassName.attr` or `instance.attr`.
- Changing via class affects all instances; changing via instance creates instance attribute.

### Instances & Instance Attributes
- Created by calling the class: `obj = ClassName()`.
- **Instance attributes**: Unique to each object; set in `__init__`.
- Access and modify via `obj.attr`.
- Can add attributes dynamically to instances.

### Binding & Method Invocation
- Methods are bound to instances (`self`) or classes (`cls`).
- Call with `obj.method()`; Python passes `self` automatically.
- Use `@classmethod` and `@staticmethod` for class/static methods.
- `super()` accesses parent methods.

### Composition, Subclassing, Derivation
- **Composition**: Class contains other class objects ("has-a").
- **Subclassing/Derivation**: Class inherits from another ("is-a").
- Multiple inheritance supported.
- Use composition for flexibility, subclassing for specialization.

### Inheritance
- Subclass inherits attributes/methods from parent.
- Can override parent methods.
- Use `super()` to call parent methods.
- Supports single, multiple, multilevel, hierarchical inheritance.
- MRO determines method lookup order.

### Built-in Functions
- `type(obj)`, `isinstance(obj, cls)`, `issubclass(sub, super)`
- `hasattr(obj, name)`, `getattr(obj, name)`, `setattr(obj, name, value)`, `delattr(obj, name)`
- `dir(obj)`, `vars(obj)`, `callable(obj)`
- Special: `__class__`, `__dict__`, `__bases__`

### Built-in Classes & Modules
- Data types: `int`, `float`, `str`, `list`, `dict`, etc.
- All classes inherit from `object`.
- Useful modules: `collections`, `abc`, `dataclasses`, `types`, `enum`, `functools`
- Introspection: `dir()`, `type()`, `inspect`
- Abstract classes: `abc.ABC`, `@abstractmethod`
- Data classes: `@dataclass`

---

**Tip:** Use OOP for modular, reusable, maintainable, and flexible code in Python.