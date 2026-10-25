"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.list = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # Push supports LIFO by using append to make the value "Last In"
        # Later we can remove this value, meaning the last value added will be the first one out
        self.list.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # If the stack is empty, return "Nothing left to pop" instead of making an error
        if self.list == []:
            return "Nothing left to pop"

        return self.list.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # Peek looks at the last value in the list without removing it like pop would
        if self.list == []:
            return "List is empty"

        return self.list[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        return self.list == []

    def display(self, message=""):
        print(f"list = {self.list}")

        if message != "":
            print(message)
        else:
            print()


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.list = []

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # Enqueue supports FIFO by using append to add the value to the back of the queue
        # Later we'll remove the value from the front, meaning the first (oldest) value will be the first out
        self.list.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # If the queue is empty, return "Nothing left to dequeue" instead of making an error
        if self.list == []:
            return "Nothing left to dequeue"

        return self.list.pop(0)

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # Front looks at the first value in the list without removing it like dequeue would
        if self.list == []:
            return "List is empty"

        return self.list[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.

        return self.list == []

    def display(self, message=""):
        print(f"List = {self.list}")

        if message != "":
            print(message)
        else:
            print()

def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO (LIFO) ===")
    print("> Creating a Stack object")

    stack_demo = Stack()

    for value in [2, 4, 6, 8]:
        stack_demo.push(value)

    stack_demo.display()

    print("> push(10) [Last In]")
    stack_demo.push(10)
    stack_demo.display()

    print("> peek()")
    print(f"Last value in list: {stack_demo.peek()}\n")

    print("> pop() [Last In First Out]")
    stack_demo.pop()
    stack_demo.display()

    print("> pop() ALL\n"
          "> peek() while empty")
    while not stack_demo.is_empty():
        stack_demo.pop()

    print(f"{stack_demo.peek()}\n")

    print("> pop() while empty")
    print(f"{stack_demo.pop()}\n")

    print("> Create a stack with 1 item, remove it, verify stack is empty")
    stack_demo.push(2)
    stack_demo.display(">> pop()")
    stack_demo.pop()
    print(f"Stack Empty: {stack_demo.is_empty()}")

    print("\n=== STACK REAL-WORLD SCENARIO (LIFO) ===")
    print("> Three players are playing a card game")
    card_stack = Stack()

    for cards in ["Three of Hearts", "Ace of Spades", "Eight of Clubs"]:
        card_stack.push(cards)

    strongest_card = "Ace of Spades"
    player = 0
    while not card_stack.is_empty():
        player += 1
        card = card_stack.pop()
        print(f"Player {player} draws and plays {card} from the top of the deck")
        if card == strongest_card:
            winner = player


    print(f"\n{strongest_card} is the strongest card. Player {winner} wins.")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO (FIFO) ===")
    print("> Creating a Queue object")

    queue_demo = Queue()

    for value in [3, 6, 9, 12]:
        queue_demo.enqueue(value)

    queue_demo.display()

    print("> enqueue(15)")
    queue_demo.enqueue(15)
    queue_demo.display()

    print("> front()")
    print(f"First value in list: {queue_demo.front()}\n")

    print("> dequeue() [First In First Out]")
    queue_demo.dequeue()
    queue_demo.display()

    print("> dequeue() ALL\n"
          "> front() while empty")
    while not queue_demo.is_empty():
        queue_demo.dequeue()

    print(f"{queue_demo.front()}\n")

    print("> dequeue() while empty")
    print(f"{queue_demo.dequeue()}\n")

    print("> Create a Queue with 1 item, remove it, verify queue is empty")
    queue_demo.enqueue(3)
    queue_demo.display(">> dequeue()")
    queue_demo.dequeue()
    print(f"Queue Empty: {queue_demo.is_empty()}")

    print("\n=== QUEUE REAL-WORLD SCENARIO (FIFO) ===\n"
          "Three customers are ordering McDonalds")

    customer_queue = Queue()
    for customers in ["Brandon", "Barbara", "Brady"]:
        customer_queue.enqueue(customers)

    food_queue = Queue()
    for foods in ["Big Mac", "10 Piece Nuggets", "Chicken Wrap"]:
        food_queue.enqueue(foods)

    i = 0
    while i < len(customer_queue.list):
        print(f"{customer_queue.list[i]} Order #{i + 1}: {food_queue.list[i]}")
        i += 1
    print()

    print(f"{customer_queue.dequeue()} has received their order\n"
          f"Next Customer: {customer_queue.front()}")

if __name__ == "__main__":
    main()