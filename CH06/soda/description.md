


# Activity: Total Soda Case
## Input File

You are given a file named: `orders.txt`


The file contains soda names and case quantities on alternating lines:

**Example:**

```
Coke
10
Pepsi
25
Sprite
15
```

**Pattern:**

Soda name

Number of cases

Soda name

Number of cases

etc.

_Note: You will have to manually create this txt file. Create it in the same directory as your python file and then copy and paste the example. _

## Your Task

#### Write a program that:

- Opens orders.txt
- Reads through the entire file
- Calculates the total number of cases ordered
- Prints the total

#### Important

Use a loop to read through the file dynamically (do not assume how many entries exist).

Your program must not crash.

## Expected Output Format
Total Cases Ordered: 50


(The number will depend on the file.)

## Add-Ons (Optional Extensions)

If you finish early, extend your program to include the following (this is also good practice to get you ready for the quiz/exam!:

### 1️⃣ Error Checking When Reading Numbers

Use try/except when converting quantity lines to integers.

If a line cannot be converted to an int, skip it.

The program must not crash.

### 2️⃣ Track the Maximum Order

While reading the file:

- Keep track of the soda with the highest number of cases.
- Also keep track of how many cases that soda had.
- You should end up with:
```
Total cases ordered

Soda with the maximum cases

Number of cases for that soda
```

### 3️⃣ Write Results to a File

After printing your results to the screen, write them to a new file:

order_stats.txt


Format:
```
Total Cases Ordered: 50
Top Soda: Pepsi
Top Soda Cases: 25
```



