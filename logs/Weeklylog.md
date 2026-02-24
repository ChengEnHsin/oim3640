# Weekly log Chapter 5-7 Conditionals, Recursion, and Return Values 

## What I learned this week

This week helped me move from just writing code that runs to actually understanding how Python structures logic.

In Chapter 5, I practiced conditionals and recursion. I feel more comfortable with Boolean expressions and nested `if` statements. Recursion was especially interesting because it showed how a function can call itself as long as there is a clear base case. When I understand the base case and the smaller repeating step, recursion makes sense.

In Chapter 6, I really understood the difference between `print()` and `return`. Before, I thought they were almost the same. Now I know that `print()` just displays something, but `return` gives a value back so it can be stored, reused, or combined with other logic. That changed how I think about writing functions.

In Chapter 7, I learned how `while` loops work and how iteration depends on updating variables correctly. I practiced thinking about how the loop condition eventually becomes False so the program does not run forever.

Overall, this week was about understanding structure and logic more than just syntax.

## Code/work I'm proud of (optional)

I am proud of my Ackermann function because it forced me to carefully follow the recursive definition and think about structure.

```python
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
```

This showed me how powerful recursion is and how quickly it grows. When I tried `ackermann(5, 5)`, it basically pushed Python to its recursion limit, which made the concept very real.

## Challenges I faced

The hardest part this week was putting all the logic together. Each concept makes sense when it is explained in class. When the professor walks through examples step by step, I understand it. But when I try to write code on my own in the notebooks, it becomes confusing.

There are so many rules, structures, and vocabulary terms at once. Conditional logic, recursion, return values, loop structure, base case, accumulator, Boolean expressions. Sometimes I understand each piece individually, but when I try to see the bigger picture, I feel overwhelmed.

It is especially hard to connect:
- When to use conditionals inside loops  
- When to return versus print  
- How recursion fits into the overall structure of a program  

I realized that my difficulty is not syntax. It is seeing how everything connects together. I am trying to slow down and think about the structure first before writing code.

## AI usage (if any)

I used AI to clarify vocabulary and explain concepts in simpler language when I felt overwhelmed by textbook terms.

I also used AI to turn my bullet point notes into complete sentences. During class, I try to pay attention while taking notes, so my notes are usually simplified and fragmented. After class, I used AI to expand those bullet points into clearer explanations so I could better understand the full concept.

Sometimes I pasted my code and asked why it was not working. I made sure to rewrite the solution in my own words and test it myself instead of copying directly. AI helped me organize my thinking, but I still made sure I understood everything before moving on.

## Questions for next time

How can I better see the big picture of how all these concepts connect  
How do I practice structuring logic before jumping into writing code  
Is there a framework for deciding which structure to use first  

I want to become more confident working independently without feeling lost once I am outside the classroom explanation.