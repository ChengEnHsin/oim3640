

mutable sequences review
- dictonaries are mutable sequences that store key-value pairs
- lists are mutable sequences that store ordered collections of items

 Chapter 10 Lists

## What I learned this week

This week focused on lists and how Python stores and manipulates collections of data. I learned that lists are mutable, which makes them very different from strings. I can change elements, add new ones, or remove them without creating a new object. That helped me understand why lists are useful when working with dynamic data.

I also practiced indexing and slicing. Indexing gives me a single element, while slicing returns a new list. Understanding how slicing works with start and end positions helped me avoid off by one errors. I also learned that lists can contain different data types, which makes them flexible but also requires careful thinking when processing them.

Another key concept was iteration. Looping through a list using a for loop feels much more natural now, especially compared to manually accessing elements. I also learned about common list methods like append, pop, remove, and sort. These methods made it easier to manipulate data without writing extra logic.

One idea that stood out to me was aliasing versus copying. If two variables reference the same list, changes to one affect the other. This was confusing at first, but it made me more aware of when I need to create a copy instead of just assigning a variable.

## Challenges I faced

One challenge was understanding the difference between modifying a list and creating a new one. I sometimes accidentally changed the original list when I did not mean to. Another challenge was keeping track of indexes, especially when slicing or removing elements.

I also found it tricky to debug when loops did not behave as expected. Sometimes the logic was correct, but I placed a line in the wrong part of the loop, which changed the output.

## AI usage (if any)

I used AI to clarify the difference between aliasing and copying lists. I also asked for examples of when to use list methods like append versus concatenation. I made sure to rewrite the examples myself and test them so I could understand the behavior instead of just copying code.

## Questions for next time

* When should I use a list versus other data structures like dictionaries or sets
* What is the most efficient way to remove duplicates from a list
* How do list operations scale with larger datasets
* When does it make sense to use built in functions instead of writing logic manually

