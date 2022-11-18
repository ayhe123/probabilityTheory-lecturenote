"""
引理 10.1

Copyright 2022 ayhe123

此程序采用 CC-BY-4.0 许可证, 更多信息见 https://creativecommons.org/licenses/by/4.0
"""

import math
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

LAMBDA = 5
VARS = 5  # 变量个数
TESTS = 100000

rng = default_rng()
xs = rng.exponential(1 / LAMBDA, (TESTS, VARS))
y = np.sum(xs, axis=1)

fig, ax = plt.subplots()

# 直方图
# 如果直方图的 bin 数不确定, 可以设置 bins='scott'
n, bins, patches = ax.hist(
    y, density=True, bins='scott', histtype='stepfilled')

# 理论计算得到的分布
y_hat = LAMBDA ** VARS / math.factorial(VARS - 1) \
    * np.exp(-LAMBDA * bins) * bins ** (VARS - 1)
ax.plot(bins, y_hat, '--')

# 标签
ax.set_xlabel(f'$X1+X2+\cdots+X{VARS}$')
ax.set_ylabel('Probability Density')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
