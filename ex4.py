import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", type=int)
parser.add_argument("-w", nargs="+", type=int)
parser.add_argument("-n", type=int)
args = parser.parse_args()

W = args.v
w = args.w
n = args.n

print(W, w, n)
















