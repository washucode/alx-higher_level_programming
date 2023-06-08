#!/usr/bin/python3


def my_calculator():
    from calculator_1 import add, sub, mul, div
    import sys
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op == "+":
        res = add(a, b)
    elif op == "-":
        res = sub(a, b)
    elif op == "*":
        res = mul(a, b)
    elif op == "/":
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, op, b, res))


if __name__ == "__main__":
    my_calculator()
