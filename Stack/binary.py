import Stack


def convToBinary(num):
    s = Stack.Stack()
    div = int(num)
    out = ""
    while div > 0:
        s.push(int(div % 2))
        div = int(div) // 2
    for i in range(0, s.size()):
        out += str(s.pop())
    return out


def main():
    num = input("Input a number to convert to binary: ")
    print(convToBinary(num))

main()
