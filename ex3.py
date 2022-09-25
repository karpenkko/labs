import argparse

parser = argparse.ArgumentParser()
parser.add_argument("formula", nargs="?")
args = parser.parse_args()

try:
    if args.formula[0].isdigit() and args.formula[-1].isdigit():
        if "++" in args.formula or "--" in args.formula:
            print("False / None")
        else:
            result = eval(args.formula)
            if result:
                print("True /", result)
    else:
        print("False / None")
except (NameError, TypeError):
    print("False / None")


