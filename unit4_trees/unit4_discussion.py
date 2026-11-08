"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        """
        TODO (Student):
        Store the node's value and initialize references
        to the left and right child nodes.
        """

        # Create a node and initialize left/right references
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        """
        TODO (Student):
        Initialize an empty Binary Search Tree.
        """

        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Don't execute _insert_recursive if value is None
        if value is None:
            return

        # If the tree is empty, insert the value as the root.
        # Otherwise, execute _insert_recursive
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # Insert smaller values into the left subtree
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        # Insert larger values into the right subtree
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

        # Return the updated node reference
        # If value == node.value, nothing is inserted and the node reference is returned
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is often more efficient than linear search because it often has to access less nodes
        # Linear search has to touch  every node until it finds the search or touches every single node
        # BST uses comparisons to remove subtrees from the equation, making it so it only touches some nodes

        # Value is not found if value = none or the tree is empty
        if value is None or self.root is None:
            return False

        # Return True if found, False if not found
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # Search to the left for values < node, search to the right if values > node
        # If a leaf is reached, and the value isn't the leaf, return false
        if value < node.value:
            if node.left is None:
                return False
            else:
                return self._search_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                return False
            else:
                return self._search_recursive(node.right, value)

        # Return true if found
        return True

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Empty list
        values = []

        # Add the values to the list
        self._inorder_recursive(self.root, values)

        # Return sorted list
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # Searching an empty tree
        if node is None:
            return

        # Append items in ascending order
        # Visits left subtree first for smaller values, working its way to the right while appending each
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    bst = BST()

    # Insert values into both left and right subtrees.
    # BST comparisons allow entire subtrees to be skipped during searches.
    print("> inserted_values = [42, 19, 73, 8, 31, 64, 91, 27, 68]")
    inserted_values = [42, 19, 73, 8, 31, 64, 91, 27, 68]

    for value in inserted_values:
        bst.insert(value)

    print("Inserted values:", inserted_values)

    # Verify root and child nodes.
    assert bst.root.value == 42
    assert bst.root.left.value == 19
    assert bst.root.right.value == 73
    assert bst.root.left.right.left.value == 27
    assert bst.root.right.left.right.value == 68
    print("Tree construction tests passed.")


    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order traversal visits the left subtree, current node,
    # and right subtree, sorting values in ascending order.
    in_order = bst.inorder()

    print("> in_order == [8, 19, 27, 31, 42, 64, 68, 73, 91]")
    print("In-order traversal:", in_order)

    assert in_order == [8, 19, 27, 31, 42, 64, 68, 73, 91]

    print("In-order traversal test passed.")


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # 27 and 68 should return True since they exist
    assert bst.search(27) is True
    assert bst.search(68) is True

    print("- [True] -")
    print(f"bst.search(27): {bst.search(27)}"
          f"\nbst.search(68): {bst.search(68)}")

    # 16 and 85 should return False since they do not exist
    assert bst.search(16) is False
    assert bst.search(85) is False

    print("- [False] -")
    print(f"bst.search(16): {bst.search(16)}"
          f"\nbst.search(85): {bst.search(85)}")
    print("Search tests passed.")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Test inserting duplicates.
    # The BST should ignore duplicates and make no changes.
    bst.insert(31)
    bst.insert(42)

    expected_values = [8, 19, 27, 31, 42, 64, 68, 73, 91]

    assert bst.inorder() == expected_values

    print(f"After duplicate bst.inorder(): {bst.inorder()}")
    print("Duplicate insertion test passed.")


if __name__ == "__main__":
    main()