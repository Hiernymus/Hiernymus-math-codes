from sage.all import *
import numpy as np

# 定义数组的大小
size = (11, 11)

# 创建一个全零的二维数组
images = np.zeros(size)

# 初始化第一行的中间元素为 1
images[0][0] = 1

# 生成杨辉三角
for step in range(1, size[0]):
    for left in range(1, size[1]):
        images[step][left] = images[step-1][left-1] + images[step-1][left]
        left = left + 1

images[0][0] = 0
# 显示结果
show(images)