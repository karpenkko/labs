import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", type=int)
parser.add_argument("-w", nargs="+", type=int)
parser.add_argument("-n", type=int)
args = parser.parse_args()

def knapsack(W, w, n):
    matrix = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif w[i - 1] <= j:
                matrix[i][j] = max(w[i - 1] + matrix[i - 1][j - w[i - 1]], matrix[i - 1][j])
            else:
                matrix[i][j] = matrix[i - 1][j]

    return matrix[n][W]

print(knapsack(args.v, args.w, args.n))
















