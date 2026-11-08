# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

---------------------------
# Reflection

I learned how a BST organizes values based on comparisons. Smaller values are placed in the left subtree, and larger values are placed in the right subtree. I implemented recursive insertion, searching, and in-order traversal, then used assertions to verify the results.

The hardest part was understanding how recursion worked during in-order traversal. I understood why the method kept going left, but I initially didn't understand how execution returned to previous nodes and continued to the right. Walking through the recursive calls showed me that each call waits for the deeper call to finish.

Additionally, I learned that a BST can be more efficient than linear searches by reducing the number of values checked during a search, eliminating entire subtrees after comparisons. A linear search checks values one at a time. However, if values are inserted in ascending order in a BST, the BST can become unbalanced and perform similarly to a linked list.