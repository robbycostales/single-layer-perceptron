# Language: Python 3
#
# Author: Roop Pal, Robby Costales
# Date: 02 / 26 / 2017
#
# This program is a perceptron that is trained and tested on hard-coded rule.

import numpy as np
import random

growth_constant = .2		
n = 100000		# number of training set inputs / output pairings
m = 1000		# number of tests
dimension = 2	
ts_in = [[int(200 * random.random() - 100) for i in range(dimension)] for j in range(n)]    # generation of training set inputs

# Manual output calculation
ts_out = [[0] for _ in range(n)]    # initialize training set outputs

for i in range(n):  # sets the training set outputs
    if ts_in[i][0] > ts_in[i][1]:   # output is 1 when the first number in the pair is greater than the second
        ts_out[i][0] = 1

inp = [[int(200 * random.random() - 100) for i in range(dimension)] for j in range(m)]	# generates random inputs from -100 to 99

w = [(random.random() * 2 - 1) for i in range(dimension)]	# generates random weights

# Training perceptron
for i in range(n):  # adjusts weights based on training set
    output = 0
    if np.dot(ts_in[i], w) > 0:     # if the dot product of weights and inputs is greater than the threshold ...
        output = 1
    for j in range(dimension):      # adjust weight based on error, input, and growth constant
        w[j] += (ts_out[i][0] - output) * ts_in[i][j] * growth_constant


percent = 0
for i in inp:   # test perceptron against test inputs and calculate accuracy
    output = 0
    if (np.dot(i, w)) > 0:
        output = 1
    if i[0] > i[1]:
        expect_out = 1
    else:
        expect_out = 0
    if output == expect_out:
        percent += 1

print(w)
print((percent/len(inp) * 100), "%")
