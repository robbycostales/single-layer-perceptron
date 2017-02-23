import numpy as np
import matplotlib.pyplot as plt
import random

growth_constant = .2
n = 100000
m = 1000
dimension = 2
ts_in = [[int(200 * random.random() - 100) for i in range(dimension)] for j in range(n)]

# Manual output calculation
ts_out = [[0] for _ in range(n)]

for i in range(n):
    if ts_in[i][0] > ts_in[i][1]:
        ts_out[i][0] = 1

inp = [[int(200 * random.random() - 100) for i in range(dimension)] for j in range(m)]

w = [(random.random() * 2 - 1) for i in range(dimension)]

# Training perceptron
for i in range(n):
    output = 0
    if np.dot(ts_in[i], w) > 0:
        output = 1
    for j in range(dimension):
        # if ts_out[i][0] - output >
        w[j] += (ts_out[i][0] - output) * ts_in[i][j] * growth_constant


percent = 0
for i in inp:
    output = 0
    if (np.dot(i, w)) > 0:
        output = 1
    expect_out = 0
    if i[0] > i[1]:
        expect_out = 1
    if output == expect_out:
        percent += 1

print(w)

print((percent/len(inp) * 100), "%")
