import Stack


def parens(parseString):
    s = Stack.Stack()
    balanced = True
    index = 0
    while index < len(parseString) and balanced:
        symbol = parseString[index]
    if symbol == '(':
        s.push(symbol)
    else:
        if s.isEmpty():
            balanced = False
        else:
            s.pop()
    if balanced and s.isEmpty():
        return True
    else:
        return False
