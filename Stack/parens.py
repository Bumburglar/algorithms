import Stack


def parens(parseString):
    s = Stack.Stack()
    balanced = True
    index = 0
    while index < len(parseString) and balanced:
        symbol = parseString[index]
        if symbol in '[{(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opener = '[{('
    closer = ']})'
    return opener.index(open) == closer.index(close)

print(parens("()()()()()()())))((())()))"))
print(parens("(((())()))"))
