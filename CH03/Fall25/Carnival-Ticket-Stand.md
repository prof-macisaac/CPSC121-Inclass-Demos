# 🎡 Carnival Admission Program

## Objective

Write a Python program that calculates and displays the admission price for a carnival based on a visitor’s information.  
This assignment will help you practice **if/elif/else conditionals**, logical operators (`and`, `or`), and combining multiple rules.

---

## Admission Rules

Your program should apply the following rules in order:

- 👶 **Kids under 6** → Free admission
- 🎓 **Students**  
  - Weekdays → Free admission  
  - Weekends → $2 off
- 👴 **Seniors (65+)** → $3 off every day
- 💵 **Regular Admission Prices**  
  - Weekdays → $12  
  - Weekends → $17  

💰 All discounts are applied to the base ticket price.

---

## Program Requirements

1. Ask the user for:
   - Their age  
   - Whether they are a student (`yes`/`no`)
   - What day of the week it is

2. Apply the correct rules to determine the ticket cost.  

3. Print a clear message showing:
   - The user’s age, student/senior status  
   - The base ticket price  
   - Any discount applied  
   - The **final amount owed**  

---

## Example Runs

### Example 1

```
Enter your age: 4
Are you a student? (yes/no): no
What day of the week is it (mon, tues, wed, thurs, fri, sat, sun)? mon 

👶 Kids under 6 get in FREE!
Final Price: $0
```

### Example 2

```
Enter your age: 20
Are you a student? (yes/no): yes
What day of the week is it (mon, tues, wed, thurs, fri, sat, sun)? sun

Base price: $17
Student weekend discount: -$2
Final Price: $15
```
