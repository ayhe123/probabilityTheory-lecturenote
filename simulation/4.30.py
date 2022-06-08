"""
习题 4.30, 4.33

两个服从指数分布的变量的和, 最小值, 商得到的变量的分布
"""

import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt

LAMBDA_1 = 5
LAMBDA_2 = 20
TESTS = 100000

rng = default_rng()
x_1 = rng.exponential(1 / LAMBDA_1, TESTS)
x_2 = rng.exponential(1 / LAMBDA_2, TESTS)
y_0 = x_1 + x_2
y_1 = np.min([x_1, x_2], axis=0)
y_2 = x_1 / x_2

fig, axs = plt.subplots(2, 2)

# 直方图 x_1 + x_2
# 如果直方图的 bin 数不确定, 可以设置 bins='scott'
n, bins, patches = axs[0, 0].hist(
    y_0, density=True, bins='scott', histtype='stepfilled')

# 理论计算得到的分布 x_1 + x_2
y_hat0 = LAMBDA_1 * LAMBDA_2 / (LAMBDA_2 - LAMBDA_1) \
    * (np.exp(-LAMBDA_1 * bins) - np.exp(-LAMBDA_2 * bins))
axs[0, 0].plot(bins, y_hat0, '--')

# 直方图 min(x_1, x_2)
n, bins, patches = axs[0, 1].hist(
    y_1, density=True, bins='scott', histtype='stepfilled')

# 理论计算得到的分布 min(x_1, x_2)
y_hat1 = (LAMBDA_1 + LAMBDA_2) * np.exp(-(LAMBDA_1 + LAMBDA_2) * bins)
axs[0, 1].plot(bins, y_hat1, '--')

# 直方图 x_1 / x_2
# 对数坐标 log=True
n, bins, patches = axs[1, 0].hist(
    y_2, density=True, bins='scott', histtype='stepfilled', log=True)

# 理论计算得到的分布 x_1 / x_2
y_hat2 = LAMBDA_1 * LAMBDA_2 / (LAMBDA_1 * bins + LAMBDA_2) ** 2
axs[1, 0].loglog(bins, y_hat2, '--')

# 标签
axs[0, 0].set_xlabel('$X_1+X_2$')
axs[0, 0].set_ylabel('Probability Density')
axs[0, 1].set_xlabel('min$(X_1,X_2)$')
axs[0, 1].set_ylabel('Probability Density')
axs[1, 0].set_xlabel('$X_1/X_2$')
axs[1, 0].set_ylabel('Probability Density')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
