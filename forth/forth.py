class StackUnderflowError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Stack:
    """
    Stack class with required functions to do stack manipulations on objects

    Note:
    The functions pop, dup, swap and over may raise IndexError if the required number of elements are not available,
    Eg: pop and dup - In case when no elements are present, swap and over - when less than two elements present
    This is handled when these functions are called via objects in the evaluate function ( via Try-Except)
    """

    def __init__(self) -> None:
        self.elements = []

    def pop(self) -> int:
        return self.elements.pop()

    def push(self, data: int) -> None:
        self.elements.append(data)

    def dup(self) -> None:
        self.push(self.elements[-1])

    def swap(self) -> None:
        self.elements[-1], self.elements[-2] = self.elements[-2], self.elements[-1]

    def over(self) -> None:
        self.push(self.elements[-2])


def evaluate(input_data: list[str]) -> list[str]:
    """
    Math operations: Dict that holds strings for dunder methods for respective math operation.
    These are called when the stack encounters maths operators, using __getattribute__() method

    Similar is case for Stack operations, functions of Stack object are called using __getattribute__()
    """
    math_operations: dict = {
        "+": "__add__",
        "-": "__sub__",
        "*": "__mul__",
        "/": "__floordiv__",
    }
    stack_operations: dict = {
        "DUP": "dup",
        "DROP": "pop",
        "SWAP": "swap",
        "OVER": "over",
    }
    # user_defined used to store and check for user defined operations in given input line
    user_defined: dict = {}
    stack = Stack()

    def update_operations(operations: list[str]) -> str:
        """
        Takes a list of operations(words) to check if there is already an operation defined by user for the given word,
        Replaces given word as per user defined words, already present in the user_defined dict
        """
        for i, item in enumerate(operations):
            if item.upper() in user_defined.keys():
                operations[i] = user_defined[item.upper()]
        return operations

    for line in input_data:
        if line.startswith(":"):
            """
            If a line contains : word <definition> ; syntax that means this line wants to define a new collection of operations,
            using the native (maths and stack) or other user_defined operations. 
            Check for  new operation name, and the <definition> followed by new_op, and define it in user_defined dict.
            If the <definition> contains words previously defined by user, replace them too, by calling update_operations()
            """
            line = line.removeprefix(": ").removesuffix(" ;")
            new_op, *updates = line.split()
            if new_op.strip("-").isnumeric():
                raise ValueError("illegal operation")
            updated_op = " ".join(update_operations(updates))
            user_defined[new_op.upper()] = updated_op
            continue

        # For every line, check and update operation definitions as per user defined operations
        line = " ".join(update_operations(line.split()))
        for item in line.split():
            item = item.upper()

            if item.strip("-").isnumeric():
                stack.push(int(item))
            elif item in math_operations.keys():
                try:
                    # Since the operations below might raise Index error if stack empty (or insufficient items)
                    op1 = stack.pop()
                    op2 = stack.pop()
                except IndexError:
                    raise StackUnderflowError("Insufficient number of items in stack")

                if item == "/" and op1 == 0:
                    raise ZeroDivisionError("divide by zero")
                to_push = op2.__getattribute__(math_operations[item])(op1)
                stack.push(to_push)
            elif item in stack_operations.keys():
                try:
                    # Since the operation below might raise Index error if stack empty (or insufficient items)
                    stack.__getattribute__(stack_operations[item])()
                except IndexError:
                    raise StackUnderflowError("Insufficient number of items in stack")
            else:
                # Reaches here if a word is found which is not yet defined in the valid operations
                raise ValueError("undefined operation")

    return stack.elements
