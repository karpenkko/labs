import argparse

parser = argparse.ArgumentParser()
parser.add_argument("formula", nargs="?")
args = parser.parse_args()

try:
    if "++" in args.formula or "--" in args.formula:
        print("False / None")
    else:
        result = eval(args.formula)
        if result:
            print("True /", result)
except NameError:
    print("False / None")
except TypeError:
    print("False / None")

