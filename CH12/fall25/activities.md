Here are some very *lightweight*, recursion-only participation activities you can drop straight into class or Canvas. All of them focus on **one tiny problem** with a clear base case + recursive step.

I’ll assume Python, but they’re easily portable.

---

## Activity 1: Tracing a Simple Countdown

**Goal:** See the *shape* of recursion without writing it yet.

**Prompt to students**

> Consider this function:
>
> ```python
> def countdown(n):
>     if n == 0:
>         print("Blastoff!")
>     else:
>         print(n)
>         countdown(n - 1)
> ```
>
> 1. What gets printed when we call `countdown(3)`?
> 2. In your own words, what is the **base case**? What is the **recursive step**?

Students can do this as a quick pair share or Canvas fill-in.

**Teacher notes / solution**

* Output:

  ```
  3
  2
  1
  Blastoff!
  ```
* Base case: when `n == 0`, just print `"Blastoff!"`, no more recursive call.
* Recursive step: print `n`, and then call `countdown(n - 1)`.

---

## Activity 2: Fill-in-the-Blanks – Sum 1..n

**Goal:** Help them see “problem broken into smaller subproblem”.

**Prompt to students**

> Fill in the missing pieces to make a recursive function that returns the sum
> `1 + 2 + 3 + ... + n`.
>
> ```python
> def sum_to_n(n):
>     # base case
>     if _____________________:
>         return _____________________
>     
>     # recursive step
>     # idea: sum_to_n(n) = n + sum_to_n(n-1)
>     return _____________________
> ```
>
> Test your function with:
>
> ```python
> print(sum_to_n(1))   # should be 1
> print(sum_to_n(4))   # should be 10
> ```

**Solution**

```python
def sum_to_n(n):
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)
```

(You can also use `if n == 0: return 0` if you prefer.)

---

## Activity 3: Recursive Length of a List

**Goal:** Apply recursion to a *non-numeric* structure they already know (lists).

**Prompt to students**

> Write a recursive function `my_len(lst)` that returns how many elements are in the list `lst`.
> You may **not** use `len()`.
>
> Hints:
>
> * Base case: the length of an empty list `[]` is 0.
> * Recursive step idea: the length of a non-empty list is
>   `1 + length_of_the_rest_of_the_list`.
>
> Start from this skeleton:
>
> ```python
> def my_len(lst):
>     if _____________________:      # base case
>         return _____________________
>
>     # recursive step
>     return _____________________
>
> print(my_len([]))          # 0
> print(my_len([10]))        # 1
> print(my_len([1, 2, 3]))   # 3
> ```

**Solution**

```python
def my_len(lst):
    if lst == []:
        return 0
    return 1 + my_len(lst[1:])
```

You can emphasize: each call “peels off” one element.

---

## Activity 4: Print Characters of a String One per Line

**Goal:** Another very simple, visual example; reinforces base/step.

**Prompt to students**

> Write a recursive function `print_chars(s)` that prints each character of the string `s` on its own line.
>
> Examples:
>
> ```python
> print_chars("cat")
> ```
>
> Should print:
>
> ```
> c
> a
> t
> ```
>
> Hints:
>
> * Base case: when the string is empty (`""`), do nothing.
> * Recursive step: print the first character, then recursively handle the rest.
>
> Skeleton:
>
> ```python
> def print_chars(s):
>     if _____________________:      # base case
>         return
>
>     print(____________________)    # first character
>     print_chars(________________)  # rest of the string
> ```

**Solution**

```python
def print_chars(s):
    if s == "":
        return
    print(s[0])
    print_chars(s[1:])
```

---

## Optional “Concept Check” Clicker / Canvas Question

You can also toss in a 1-minute MCQ:

> Consider:
>
> ```python
> def mystery(n):
>     if n == 0:
>         return 1
>     return 2 * mystery(n - 1)
> ```
>
> What does `mystery(n)` compute?
>
> A. The sum `1 + 2 + ... + n`
> B. The factorial of `n`
> C. The value `2^n`
> D. Always returns 1

Correct: **C** (`2^n`).

---

If you tell me which language / class level you’re targeting (121 vs 346, Python vs C), I can rewrite these into a ready-to-paste Canvas participation page with points and instructions.
