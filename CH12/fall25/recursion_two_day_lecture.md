# Two-Day Recursion Lecture Plan (Fully Expanded)

## Lecture Day 1 — Introduction to Recursion
### Main Goal
Students grasp what recursion is, why a base case is necessary, and how a function “shrinks” its input until stopping.

---

## 1. Warm-Up (3–5 min)
### Talking Points
- Recursion is when something is defined in terms of itself.
- Examples in nature and math help make the idea intuitive.
- Computers can model this pattern through functions that call themselves.

### Discussion Prompt
“Where have you seen something that contains a smaller version of itself?”

Common answers:
- Russian nesting dolls  
- Folders containing subfolders  
- Branching plants or tree limbs  
- Mathematical patterns (fractals)

---

## 2. What Recursion Is (10–12 min)
Use slides 3–5.

### Live Code (display only)
```python
def countdown(n):
    if n == 0:
        # Base case: stop when n reaches 0
        print("Blast off!")
        return

    # Recursive case: print n and call countdown on a smaller value
    print(n)
    countdown(n - 1)
```

### Talking Points
- Each call prints, then calls itself again.
- The function stops when the base case is reached.
- This creates a “call stack” of waiting function calls.

### Discussion Prompt
“What happens if we never reduce n?”

Answer: infinite recursion → Python stops with a recursion depth error.

---

## 3. Base Case vs Recursive Case (10 min)

### Talking Points
- Every recursive function must have a **base case** to avoid infinite recursion.
- The recursive case must always move the problem toward the base case.
- This is the biggest conceptual hurdle for beginners.

Example:
- Base case: `if n == 0: return`
- Recursive case: call with `n-1`

---

## 4. Factorial Example (10–12 min)

### Live Code (display only)
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Talking Points
- Factorial has a natural recursive definition.
- Demonstrate call expansion:
  - factorial(5) → 5 * factorial(4) → 5 * 4 * factorial(3) → …

### Discussion Prompt
“Why does factorial need a base case?”

Answers:
- Mathematical definition  
- Prevents infinite recursion  
- Gives recursion something to return

---

## 5. Day 1 Activity (10–15 min)

### Activity Prompt
Write a recursive function `countdown(n)` that prints n down to 1, then prints "Blast off!".

Expected structure:
```python
def countdown(n):
    if n == 0:
        # Base case: stop when n reaches 0
        print("Blast off!")
        return

    # Recursive case: print n and call countdown on a smaller value
    print(n)
    countdown(n - 1)
```

### Common correction:
Do NOT write `print(countdown(...))`.

---

## 6. Homework Help Session
Students work on their programming assignment with instructor support.

---

# Lecture Day 2 — Applying Recursion
### Main Goal
Students apply recursion to lists, numeric decomposition, GCD, and conceptual examples.

---

## 1. Recap (5 min)

### Ask:
- “What two things must every recursive function have?”
- “Why must the recursive case shrink the input?”
- “What happens when recursion hits the base case?”

---

## 2. List Range Sum (10 min)

### Live Code (display only)
```python
def range_sum(lst, start, end):
    if start > end:
        return 0
    return lst[start] + range_sum(lst, start + 1, end)
```

### Talking Points
- This is recursion over a list segment.
- Only the index changes — not the list itself.

### Discussion Prompt
“Why does this function eventually stop?”

Because `start` increases each time until it exceeds `end`.

---

## 3. Fibonacci (10–12 min)

### Live Code (display only)
```python
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)
```

### Talking Points
- This is **branching recursion**.
- Much slower than factorial because it recalculates values repeatedly.
- Forms a recursion tree.

### Discussion Prompt
“Why is Fibonacci so slow compared to factorial?”

Because it redoes the same work many times.

---

## 4. GCD (8–10 min)

### Live Code (display only)
```python
def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)
```

### Talking Points
- Highly efficient recursive function.
- Each call shrinks the pair `(x, y)` significantly.

### Discussion Prompt
“Why does gcd(x, y) always terminate?”

Because the remainder continually decreases toward 0.

---

## 5. Towers of Hanoi (8–10 min)

### Live Code (display only)
```python
def move_discs(n, from_peg, to_peg, temp_peg):
    if n > 0:
        move_discs(n - 1, from_peg, temp_peg, to_peg)
        print(f"Move disc from {from_peg} to {to_peg}")
        move_discs(n - 1, temp_peg, to_peg, from_peg)
```

### Talking Points
- Classic example of breaking a large problem into smaller versions.
- Hard to implement iteratively.

### Discussion Prompt
“Why do we move the top n-1 discs twice?”

To clear the bottom disc, move it, then rebuild the stack.

---

## 6. Day 2 Activity (10–15 min)

### Activity Prompt
Write a recursive function `sum_digits(n)` that sums the digits of a positive integer.

Expected solution:
```python
def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)
```

### Talking Points
- Base case: single-digit number  
- Recursive case: strip last digit and shrink the integer

---

## 7. Homework Help Session
Remainder of class for assignment support.

---

# Summary

### Day 1 Key Learning
- What recursion is  
- Base case vs recursive case  
- Linear recursion  
- First hands-on activity  

### Day 2 Key Learning
- Recursion on lists and numbers  
- Branching recursion  
- Efficient recursion (GCD)  
- Conceptual recursion (Hanoi)  
- Second hands-on activity

