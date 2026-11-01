"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Existing elements are shifted to the right one
    # Insertion performance is slower when there are more values to shift
    print(f"> Inserting {value} at index {index}")
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Index validation prevents errors and accidental deletion of other elements
    print(f"> Deleting value at index {index}")

    index_out_of_range = index < 0 or index >= len(lst)
    if index_out_of_range:
        print(f"> No value found at index {index}")
        return None

    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because it only checks 1 element at a time
    # It scans sequentially until it finds the value (or doesn't find the value and reaches the end)
    for index, item in enumerate(lst):
        if item == value:
            return index

    return -1

def display(lst, message=""):
    print(f"List = {lst}")

    if message != "":
        print(message)
    else:
        print()

def create_receipt(meal, meal_addons):
    return (f"\n-- Receipt --"
            f"\nMeal: {meal}"
            f"\nMeal Addons: {meal_addons}"
            f"\n-------------\n")

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.



    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")
    # Creating List
    test_list = [2, 4, 8, 10]
    display(test_list)

    # Adding '0' to the beginning of the list
    # All other numbers are shifted
    insert_at(test_list, 0, 0)
    display(test_list)

    # Adding '6' in between '4' and '8'
    # All numbers 8 and after are shifted
    insert_at(test_list, 3, 6)
    display(test_list)

    # Adding '12' to the end of the list
    insert_at(test_list, len(test_list), 12)
    display(test_list)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    # Display List
    display(test_list)

    # Deleting '0' from list
    # All other numbers are shifted
    print(f"> Returned: {delete_at(test_list, 0)}")
    display(test_list)

    # Deleting '6' from list
    # All numbers 8 and after are shifted
    print(f"> Returned: {delete_at(test_list, 2)}")
    display(test_list)

    # Deleting '12' from list
    print(f"> Returned: {delete_at(test_list, 4)}")
    display(test_list)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")
    # Display List
    display(test_list)

    # Searching for a value that exists
    print(f"> Searching for '8' in list"
          f"\n- Index: {search_value(test_list, 8)}\n")

    # Searching for a value that doesn't exist
    print(f"> Searching for '6' in list"
          f"\n- Index: {search_value(test_list, 6)}")
    print("['Index: -1' means the value did not exist]")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # Edge Case: Delete using an invalid index
    print("\n== Deleting using an invalid index ==")
    display(test_list)
    print(f"> Returned: {delete_at(test_list, 5)}")

    display(test_list)

    # Edge Case: Insert into an empty list
    print("\n== Inserting into an empty list ==")
    test_list_2 = []
    display(test_list_2)

    insert_at(test_list_2, 0, 42)
    display(test_list_2)

    print("=== REAL WORLD SCENARIO==="
          "\nRECEIPT GENERATOR"
          "\nCustomer has made an online order")

    meal = "Subway Sandwich"

    meat = "Tuna"
    toast_status = "Not Toasted"
    addon_1 = "Bacon"
    addon_2 = "Cheddar"
    addon_3 = "Pickles"
    addon_4 = "Jalapenos"
    sauce = "Honey Mustard"

    meal_addons = [meat, toast_status, addon_1, addon_2, addon_3, addon_4, sauce]

    print(create_receipt(meal, meal_addons))

    print("> Customer made an online order that they would like to change now that they are at the store")
    print(f"> Customer wants:"
          f"\nChicken instead of {meat}"
          f"\nRanch instead of {sauce}"
          f"\nChicken, bacon, and Cheddar Toasted. Other items will be added after toasting"
          "\n(Items listed before 'Toasted' are items that will be toasted)\n")


    meat_index = search_value(meal_addons, meat)
    meat = "Chicken"
    if meat_index != -1:
        delete_at(meal_addons, meat_index)
        insert_at(meal_addons, meat_index, meat)

    sauce_index = search_value(meal_addons, sauce)
    sauce = "Ranch"
    if sauce_index != -1:
        delete_at(meal_addons, sauce_index)
        insert_at(meal_addons, sauce_index, sauce)

    delete_at(meal_addons, search_value(meal_addons, toast_status))
    for index, item in enumerate(meal_addons):
        if  (item == "Chicken" or item == "Bacon" or item == "Cheddar"):
            toast_index = index + 1

    toast_status = "Toasted"
    insert_at(meal_addons, toast_index, toast_status)

    print(create_receipt(meal, meal_addons))

if __name__ == "__main__":
    main()