def validBraces(string):
    braces = "(){}[]"
    stack = []
    for c in string:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if not stack:
                return False
            if stack[-1] != braces[braces.index(c)-1]:
                return False
            else:
                stack.pop()
    if not stack:
        return True
    else:
        return False