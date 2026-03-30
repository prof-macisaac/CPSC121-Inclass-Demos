# **Chapter 10 Live Lecture Demonstration Plan**
**Topic:** Classes and Object-Oriented Programming  
**Length:** ≈ 55 minutes  
**Goal:** Students will learn how Python classes define and protect data, use accessor and mutator methods, and pass objects as arguments.

---

## **1. Warm-Up and Framing (5 min)**
**Prompt (to students):**  
> “Up to now, our programs used variables and functions. What problems might appear when a program needs to manage several related things—like multiple pets, cars, or coins—each with its own data?”

**Student-facing points**
- Functions alone can’t easily keep track of which data belongs to which item.  
- A *class* is a pattern for creating similar objects.  
- An *object* is a single, self-contained unit that stores data and the actions that work on that data.  

**Instructor note (C++ analogy):**  
Compare this to defining a class in C++ with member variables and methods, but emphasize that Python does not use type declarations or semicolons.

---

## **2. Procedural vs. Object-Oriented Example (10 min)**

### **Step 2A – Procedural Version**
```python
import random  # always import at the top

def toss(sideup):
    """Return 'Heads' or 'Tails' after a simulated toss."""
    if random.randint(0, 1) == 0:
        sideup = 'Heads'
    else:
        sideup = 'Tails'
    return sideup

sideup = 'Heads'
sideup = toss(sideup)
print(sideup)
```

**Explain to students**
- The data (`sideup`) is separate from the function (`toss`).  
- Every time you call `toss`, you must pass data in and get it back.  
- If we wanted several coins, we’d need multiple variables like `sideup1`, `sideup2`, etc.

**Instructor note:**  
Point out that this design relies on manually passing variables, similar to passing arguments to non-member functions in C++.

---

### **Step 2B – Object-Oriented Version**
```python
import random

class Coin:
    """Represents a coin that can be tossed."""

    def __init__(self):
        # runs automatically when a new Coin is created
        self.sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup

my_coin = Coin()
my_coin.toss()
print(my_coin.get_sideup())
```

**Explain to students**
- `class Coin:` defines a pattern for creating coin objects.  
- `__init__()` is called automatically when the object is created.  
- `self.sideup` is data stored *inside* the object.  
- Each object keeps its own copy of that data.

**Instructor note:**  
Relate `self` to the hidden `this` pointer in C++.  
Stress that `self` must appear explicitly in every method definition.

---

## **3. Creating and Using Instances (10 min)**
```python
coin1 = Coin()
coin2 = Coin()
coin3 = Coin()

coin1.toss()
coin2.toss()
coin3.toss()

print(coin1.get_sideup())
print(coin2.get_sideup())
print(coin3.get_sideup())
```

**Explain to students**
- Each variable stores a different object.  
- Each object remembers its own `sideup` value.  
- Changing one object’s data doesn’t affect another.

**Instructor note:**  
Show `print(id(coin1))` to illustrate distinct memory references.  
Mention that objects are reference-based; variables hold object references, not copies.

---

## **4. Private Attributes and Accessors (10 min)**
```python
class Coin:
    def __init__(self):
        self.__sideup = 'Heads'   # private attribute

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup
```

**Explain to students**
- The double underscore makes the attribute private to the class.  
- Trying `print(my_coin.__sideup)` will cause an error.  
- We use a *getter* method to safely read its value.  
- These ideas support *data hiding*, protecting internal state from outside code.

**Instructor note:**  
Clarify that name-mangling is Python’s lightweight privacy system, not true enforcement like in C++.

---

## **5. Adding Parameters and `__str__` (10 min)**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Balance: ${self.__balance:.2f}"
```

```python
acct = BankAccount(100)
acct.deposit(50)
acct.withdraw(25)
print(acct)  # automatically calls __str__()
```

**Explain to students**
- The constructor can take parameters to initialize data.  
- Methods can require arguments, just like normal functions.  
- `__str__` defines what appears when printing an object.  
- Output formatting with `f"..."` makes strings easy to read.

**Instructor note:**  
Mention this parallels overloading `operator<<` in C++, but keep that comment to yourself if students haven’t studied operator overloading yet.

---

## **6. Accessor and Mutator Methods (Slide 24) — 10 min**

### **Demonstration**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        """Accessor (getter): returns the current balance."""
        return self.__balance

    def set_balance(self, new_balance):
        """Mutator (setter): safely update the balance."""
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative.")

    def __str__(self):
        return f"Balance: ${self.__balance:.2f}"
```

### **Student-Facing Explanation**
- **Accessors (getters)** safely read data from an object.  
- **Mutators (setters)** safely change data inside the object.  
- This approach controls how the data is used and prevents invalid changes.  
- Even though we could reach inside the object directly, it’s safer to define rules within the class.

### **Interactive Discussion Prompt**
> “Why might it be risky to let another part of a program directly change the balance?”  
Guide students to answers like *it could accidentally set it to –100* or *it could skip validation.*

### **Short Exercise**
After showing `acct.set_balance(-50)` and explaining the result, ask students:  
> “How could we modify `set_balance` to warn the user but keep the old value?”

### **Instructor Notes**
- Accessor/mutator terminology is shared with many languages, but Python programmers often rely on property decorators later.  
- The key takeaway: *use methods to protect and validate data.*  
- Emphasize that this is the Python equivalent of encapsulation.

---

## **7. Passing Objects as Arguments (Slide 25) — 10 min**

### **Demonstration Example**
```python
class Coin:
    def __init__(self):
        self.sideup = "Heads"

    def toss(self):
        import random
        if random.randint(0, 1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup

def show_coin_status(coin_object):
    """Display which side is up."""
    print("Coin is showing:", coin_object.get_sideup())

def flip_coin(coin_object):
    """Simulate tossing the same coin object."""
    coin_object.toss()

my_coin = Coin()
show_coin_status(my_coin)
flip_coin(my_coin)
show_coin_status(my_coin)
```

### **Student-Facing Explanation**
- When you pass an object to a function, Python passes a **reference** to that object, *not* a copy.  
- This means both the original variable (`my_coin`) and the parameter (`coin_object`) point to the *same object in memory*.  
- If the function changes that object’s data (for example, calling `toss()`), the change is visible outside the function as well.

---

### **Interactive Demonstration — “Pass by Reference” Effect**
```python
def modify_object(obj):
    print("Inside modify_object, id(obj):", id(obj))
    obj.sideup = "Modified Inside Function"

coin_a = Coin()
print("Before call, id(coin_a):", id(coin_a))
modify_object(coin_a)
print("After call, id(coin_a):", id(coin_a))
print("After call, sideup:", coin_a.get_sideup())
```

**Expected Output (example)**
```
Before call, id(coin_a): 140705729204960
Inside modify_object, id(obj): 140705729204960
After call, id(coin_a): 140705729204960
After call, sideup: Modified Inside Function
```

**Explain to students**
- The `id()` function shows each object’s unique identity (its memory address).  
- Because the IDs match, `coin_a` and `obj` are references to the same object.  
- The update inside the function changes the same underlying data.

---

### **Key Takeaways for Students**
1. Objects in Python are **passed by reference** (technically *pass by object reference*).  
2. If a function modifies the object through its methods or attributes, the change persists.  
3. If a function reassigns the parameter to a new object (e.g., `obj = Coin()` inside the function), that reassignment affects only the local name, not the caller’s variable.

### **Instructor Notes**
- Clarify that Python always passes a reference to the object, not a pointer that can be reassigned externally.  
- If students ask, you can contrast this with C++:
  - Passing by value → copy is made.  
  - Passing by reference → function can change the caller’s data.  
  - Python’s behavior is like always passing by reference *to the object*, but variable names themselves are local references.  
- Encourage students to print `id()` values to visualize this concept.

---

## **8. Group Activity (10 min)**

**Student Prompt**  
> “Create a class named `Pet` with attributes `name` and `species`.  
> Include:  
> – a constructor (`__init__`)  
> – accessor and mutator methods for each attribute  
> – a `__str__()` method that prints a sentence about the pet.”  

Encourage testing:
```python
my_pet = Pet("Luna", "cat")
print(my_pet)
my_pet.set_name("Luna Belle")
print(my_pet.get_name())
```

**Instructor Tips**
- Walk students through verifying that each method uses `self.` correctly.  
- If time permits, pair up students and have one explain their code to another.  
- Reinforce the connection between this exercise and the encapsulation concepts just covered.

---

## **9. Wrap-Up (5 min)**
**Review Questions**
1. What do accessor and mutator methods do?  
2. What happens when you pass an object into a function?  
3. Why does the `self` keyword appear in every method?  
4. What does encapsulation mean in practical terms?  

**Wrap-Up Task**  
> “Write a short program that defines a simple class, creates two objects, and passes one object to a function that changes its data.”

---

## **Follow-Up Lab Suggestion**
*Mini Lab:*  
- Build a `Car` class with `make`, `model`, and `speed`.  
- Add `accelerate()` and `brake()` mutators that adjust `speed`.  
- Add `get_speed()` accessor and a `__str__()` method to display the car’s status after each action.  
- Pass the car object to a helper function `test_drive(car)` that calls the methods in sequence.

