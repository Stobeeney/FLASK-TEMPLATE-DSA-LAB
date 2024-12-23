class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_data = self.top
        self.top = self.top.next
        popped_data.next = None
        return popped_data.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):
        return self.top is None


def precedence(operator):
  """Return the precedence level of an operator."""
  if operator in ['+', '-']:
      return 1
  if operator in ['*', '/']:
      return 2
  if operator == '^':
      return 3
  return 0

def infix_to_postfix(expression):
    """
    Convert an infix expression to postfix notation step-by-step procedure.

    Arguments:
        expression (str): The infix expression.

    Returns:
        list: A list of strings, each representing a step in the postfix conversion.
    """

    #Initialization
    output = []
    stack = Stack()
    steps = []

    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
            steps.append("".join(output))
        elif char in '+-*/^':  # Operator
            while (not stack.is_empty() and
                   precedence(stack.peek()) >= precedence(char)):
                output.append(stack.pop())
                steps.append("".join(output))
            stack.push(char)
        elif char == '(':  # Left parenthesis
            stack.push(char)
        elif char == ')':  # Right parenthesis
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
                steps.append("".join(output))
            stack.pop()  # Pop '('

    # Pop remaining operators from the stack
    while not stack.is_empty():
        output.append(stack.pop())
        steps.append("".join(output))

    return steps