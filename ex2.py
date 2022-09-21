import argparse
import math
import operator

parser = argparse.ArgumentParser()
parser.add_argument("f")
parser.add_argument("a", nargs="+", type=int)
args = parser.parse_args()

try:
    function = getattr(math, args.f)
    print(function(*args.a))
except AttributeError:
    try:
        function = getattr(operator, args.f)
        print(function(*args.a))
    except AttributeError:
        print("Unknown function")
