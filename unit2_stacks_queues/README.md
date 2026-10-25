# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

---------------------------
# Reflection

This assignment taught me how stacks and queues work and how to implement both within a Python list. A stack allows LIFO (the item on top of the stack is what is removed first) while a queue allows FIFO (the first item introduced to the queue is the first item to be removed)

One challenge I encountered was figuring out how to loop through queues while removing values. At first, I used the length of the list as my loop condition, but since the list became shorter as I continued to remove items, the loop would end earlier than expected. I fixed this by using the is_empty() method. I also learned how to handle empty lists without causing errors.

For my real world applications, I created a card game where players draw cards from the top of a stack, representing LIFO. I also created a McDonald's ordering system where customers are served "first come first serve" (FIFO)