import numpy as np  # 加载数学库用于函数描述
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

X = np.linspace(0, 0.08, 10000000)  # 将[1,10]区间均分为100个点，得到100个横坐标
Y = 1e7 * X * X * X * X - 1850000 * X * X * X + 82309 * X * X + 157.8 * X - 0.0198   # 求出100个点的纵坐标

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(X, Y, color="red", linewidth=1.0, linestyle="-")  # 将100个散点连在一起
# plt.title('这里写的是中文')
plt.xlabel('锯丝轴向方向/m')
plt.ylabel('压强/MPa')
plt.show()