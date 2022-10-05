import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a")
parser.add_argument("operator")
parser.add_argument("b")
args = parser.parse_args()

try:
    if args.a.isnumeric() and args.b.isnumeric():
        print(eval(f"{args.a} {args.operator} {args.b}"))
    else:
        print("Incorrect input of arguments")
except ZeroDivisionError:
    print("Division by zero")
except SyntaxError:
    print("Incorrect input of operator")
except:
    print("Error")



