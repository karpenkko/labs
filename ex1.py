import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a")
parser.add_argument("operator")
parser.add_argument("b")
args = parser.parse_args()

f = args.a + args.operator + args.b
print(eval(f))
