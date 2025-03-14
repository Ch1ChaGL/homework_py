from collections import deque

def valid_braces(string: str) -> bool:
    stack = deque()
    close_braces = ')}]'
    open_braces = '({['
    for current_braces in string:

        if len(stack) == 0: stack.append(current_braces)
        if current_braces in close_braces:

            prev_braces = stack.pop()
            if  current_braces == ')' and prev_braces in '{[': return False
            if current_braces == '}' and prev_braces in '([': return False
            if current_braces == ']' and prev_braces in '{(': return False

        stack.append(current_braces)

    if stack.pop() in open_braces: return False
    return True

print(valid_braces("[({})](]"))