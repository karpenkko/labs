import argparse
import math
import operator

parser = argparse.ArgumentParser()
parser.add_argument("f")
parser.add_argument("a", nargs="+", type=int)
args = parser.parse_args()

def check(function, arguments):
    try:
        func = getattr(operator, function, False)
        if func:
            return func(*arguments)

        func = getattr(math, function, False)
        if func:
            return func(*arguments)
    except:
        return False


result = check(args.f, args.a)
if result:
    print(result)
else:
    print("Incorrect input")




