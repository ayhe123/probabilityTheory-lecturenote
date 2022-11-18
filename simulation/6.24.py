"""
习题 6.24

Copyright 2022 ayhe123

此程序采用 CC-BY-4.0 许可证, 更多信息见 https://creativecommons.org/licenses/by/4.0
"""
from math import factorial
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

MAX_N = 40
K = 5
TESTS = 100000

answer = [factorial(2*n)/(factorial(n+K)*factorial(n-K)*2**(2*n))
          for n in range(K, MAX_N)]

rng = default_rng()
result = []
for num_of_toss in range(MAX_N):
    toss_a = rng.integers(2, size=(TESTS, num_of_toss))
    toss_b = rng.integers(2, size=(TESTS, num_of_toss))
    sum_a = toss_a.sum(1)
    sum_b = toss_b.sum(1)
    prob = np.count_nonzero(sum_a == sum_b + K) / sum_a.size
    result.append(prob)
plt.plot(range(K, MAX_N), result[K:], label='simulation')
plt.plot(range(K, MAX_N), answer, label='answer')
plt.legend()
plt.show()
