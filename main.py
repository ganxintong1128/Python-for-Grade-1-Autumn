# Test code for IEEE course final project
# Fan Cheng, 2024

import minimatrix as mm
import random

# Test your code here!
# The following code is only for your reference
# Please write the test code yourself

a = mm.narray((4, 5))
print(a)

a = mm.I(10)
print(a)

print(a)
print(a.shape())
# print(a.reshape((2, 6)))

ma1 = mm.Matrix(dim=(2, 3))
ma2 = mm.Matrix(dim=(3, 4))

# print(ma1 * ma2)

print("=" * 50)
print("1. 测试 Matrix 类基本功能（3×3矩阵）")
mat = mm.Matrix(data=[[1, 2, 3], [6, 5, 4], [7, 8, 9]])
print("原始矩阵：")
print(mat)
print("形状：", mat.shape())
print("行列式：", mat.det())
print("秩：", mat.rank())
print("转置：")
print(mat.T())
print("按行求和（axis=1）：")
print(mat.sum(axis=1))
print("按列求和（axis=0）：")
print(mat.sum(axis=0))
print("所有元素求和（axis=None）：")
print(mat.sum())
print("矩阵平方（mat^2）：")
print(mat**2)
print("矩阵乘法（mat.dot(mat)）：")
print(mat.dot(mat))
print("Kronecker积（mat × I(2)）：")
print(mat.Kronecker_product(mm.I(2)))
print("切片测试（mat[1:, :2]）：")
print(mat[1:, :2])
print("索引测试（mat[1,2]）：", mat[1, 2])

# 测试赋值功能
mat_copy = mat.copy()
mat_copy[0, 0] = 100
mat_copy[1:, 2:] = mm.Matrix(data=[[99], [88]])
print("赋值后矩阵：")
print(mat_copy)

print("\n" + "=" * 50)
print("2. 测试 arange 和 reshape")
m24 = mm.arange(0, 24, 1)
print("arange(0,24,1) 生成的1×24矩阵：")
print(m24)
print("reshape((3,8))：")
print(m24.reshape((3, 8)))
print("reshape((24,1))：")
print(m24.reshape((24, 1)))
print("reshape((4,6))：")
print(m24.reshape((4, 6)))

print("\n" + "=" * 50)
print("3. 测试 zeros 和 zeros_like")
zero_33 = mm.zeros((3, 3))
print("zeros((3,3))：")
print(zero_33)
zero_like_m24 = mm.zeros_like(m24)
print("zeros_like(m24)（形状与m24相同）：")
print(zero_like_m24)
print("zeros_like(m24) 形状：", zero_like_m24.shape())

print("\n" + "=" * 50)
print("4. 测试 ones 和 ones_like")
one_33 = mm.ones((3, 3))
print("ones((3,3))：")
print(one_33)
one_like_m24 = mm.ones_like(m24)
print("ones_like(m24)（形状与m24相同）：")
print(one_like_m24)
print("ones_like(m24) 形状：", one_like_m24.shape())

print("\n" + "=" * 50)
print("5. 测试 nrandom 和 nrandom_like")
rand_33 = mm.nrandom((3, 3))
print("nrandom((3,3))：")
print(rand_33)
rand_like_m24 = mm.nrandom_like(m24)
print("nrandom_like(m24)（形状与m24相同）：")
print(rand_like_m24)
print("nrandom_like(m24) 形状：", rand_like_m24.shape())

print("\n" + "=" * 50)
print("6. 测试最小二乘法")
# 设置随机种子以保证结果可复现
random.seed(42)
mm.random.seed(42)

m = 1000  # 样本数
n = 100  # 特征数

# 生成数据（保持不变）
X = mm.nrandom((m, n))
w_true = mm.nrandom((n, 1))
e_data = [[random.random() - 0.5 for _ in range(1)] for _ in range(m)]
e = mm.Matrix(data=e_data)
Y = X.dot(w_true) + e

# 调用最小二乘法
w_hat = X.least_squares(Y)

# 计算误差（保持不变）
error = w_hat - w_true
error_norm = (error * error).sum()[0, 0]
w_true_norm = (w_true * w_true).sum()[0, 0]

print(f"真实w的前5个元素：")
print(w_true[:5, :])
print(f"估计w的前5个元素：")
print(w_hat[:5, :])
print(f"估计误差（元素平方和）：{error_norm:.6f}")
print(f"相对误差：{error_norm / w_true_norm:.6f}")

print("所有测试完成！")
print("=" * 50)
