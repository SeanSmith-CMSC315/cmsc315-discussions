# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

---------------------------
# Reflection

This assignment helped me understand how Python lists behave when values are inserted, deleted, or searched. I used insert() to add elements at different indexes, pop() to remove and return elements, and enumerate() to find the index of a matching value. I learned that inserting or deleting near the beginning of a list shifts other elements (causing more work). 

One challenge was understanding how enumerate() assigned both an index and an item during each loop. After seeing that it produced pairs of positions and values, I better understood the linear search function. I also learned why validating an index was important and why changing a variable did not automatically update an existing list or receipt string. 

For my real-world scenario, I created a Subway ordering system where a customer wanted to modify an existing order. My program searched for ingredients, deleted the original selections, and inserted replacements. This demonstrated how list operations could support an ordering system, but it also showed how performance could become slower with larger lists. Searching and shifting elements can take O(n) time, while insertion at the end can take O(1) time.