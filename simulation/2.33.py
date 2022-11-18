"""
习题 2.33

Copyright 2022 ayhe123

2n+1 局 n+1 胜的比赛仿真

此程序采用 CC-BY-4.0 许可证, 更多信息见 https://creativecommons.org/licenses/by/4.0
"""

from collections import Counter
from numpy.random import default_rng
import matplotlib.pyplot as plt

MAX_N = 10
TESTS = 100000
P = 0.6

rng = default_rng()
ns = [2*x+1 for x in range(1, MAX_N)]


def competete_once(n):
    """competete once."""
    result = [0, 0]
    for _ in range(n):
        win = rng.uniform()
        if win < P:
            result[0] += 1
        else:
            result[1] += 1
        if result[0] >= n//2+1:
            return 1
        if result[1] >= n//2+1:
            return -1
    return 0


win_probs = []
for n in ns:
    print(n)
    result = [competete_once(n) for _ in range(TESTS)]
    count = Counter(result)
    win_probs.append(count[1] / (count[-1] + count[1]))

plt.stem(ns, win_probs)
plt.xlabel('Rounds')
plt.ylabel('Prob. of winning')
plt.show()
