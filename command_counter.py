num = 0
while True:
    s = input().split()
    a, b = s[0], s[-1]
    match a:
        case "zero":
            num *= 0
        case "add":
            num += int(b)
        case "minus":
            num -= int(b)
        case "mul":
            num *= int(b)
        case "div":
            num //= int(b)
        case "result":
            print(num)
        case "exit":
            exit()