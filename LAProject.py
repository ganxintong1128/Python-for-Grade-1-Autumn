import numpy as np
import sympy as sp  

# ========== 手动输入学号 + 双重校验（纯数字 + 长度合理） ==========
while True:
    student_id = input("请输入你的学号：").strip()
    # 校验1：必须为纯数字
    if not student_id.isdigit():
        print("错误：学号必须为纯数字！请重新输入。")
        continue
    # 校验2：学号长度不能过短（至少3位，避免生成序列过慢）
    if len(student_id) < 3:
        print("错误：学号长度过短，建议输入3位及以上数字！请重新输入。")
        continue
    break  # 校验通过，退出循环

# ========== 1. 生成 17x17 整数矩阵 ==========
digits = np.array([int(c) for c in student_id])
total_seq = []
power = 1

while len(total_seq) < 17 * 17:
    for d in digits:
        val = d ** power
        total_seq.extend([int(c) for c in str(val)])
    power += 1

# 构造 NumPy 整数矩阵 & SymPy 矩阵（用于整数行列式）
A_np = np.array(total_seq[:17*17]).reshape(17, 17).astype(np.int64)
A_sym = sp.Matrix(A_np.tolist())

# ========== 打印原始 17x17 整数矩阵 ==========
print("\n原始 17x17 整数矩阵 A：")
print(A_np)
print()

# ========== 计算精确整数行列式 ==========
det_A = A_sym.det()
print("17阶矩阵的精确整数行列式值：")
print(det_A)
print()

# ========== 纯 NumPy 行最简形 (RREF) 实现 + 去负零 ==========
def rref_numpy(matrix, tol=1e-10):
    mat = matrix.astype(np.float64).copy()
    rows, cols = mat.shape
    r = 0
    pivot_cols = []

    for c in range(cols):
        # 找主元
        pivot_row = np.argmax(np.abs(mat[r:rows, c]) > tol) + r
        if np.abs(mat[pivot_row, c]) < tol:
            continue
        
        # 交换行 + 记录主元列
        mat[[r, pivot_row]] = mat[[pivot_row, r]]
        pivot_cols.append(c)

        # 主元归一化
        pivot_val = mat[r, c]
        mat[r, :] /= pivot_val

        # 消去其他行
        for i in range(rows):
            if i != r and np.abs(mat[i, c]) > tol:
                mat[i, :] -= mat[i, c] * mat[r, :]
        r += 1
        if r >= rows:
            break
    
    # 去负零
    mat = np.where(mat == -0., 0., mat)
    return mat, pivot_cols

# 计算 RREF
H, pivot_cols = rref_numpy(A_np)
print("矩阵 A 的行最简形 (RREF)：")
print(np.round(H, 6))
print()

# ========== NumPy 零空间求解 (Ax=0 基础解系) ==========
def null_space_numpy(matrix, tol=1e-10):
    u, s, vh = np.linalg.svd(matrix.astype(np.float64))
    null_mask = s < tol
    null_basis = vh[null_mask].T
    # 去负零
    null_basis = np.where(null_basis == -0., 0., null_basis)
    return null_basis

null_basis = null_space_numpy(A_np)
print("Ax=0 的基础解系（列向量）：")
if null_basis.shape[1] == 0:
    print("只有零解 x = 0")
else:
    print(np.round(null_basis, 6))
    print("通解形式：x = k1*v1 + k2*v2 + ... + km*vm (k为任意实数)")
print()

# ========== NumPy 满秩分解 ==========
def full_rank_decompose(matrix, rref_mat, pivot_cols):
    rank = len(pivot_cols)
    # 列满秩矩阵 B (原矩阵主元列)
    B = matrix.astype(np.float64)[:, pivot_cols]
    # 行满秩矩阵 C (RREF 前 rank 行)
    C = rref_mat[:rank, :]
    # 去负零
    B = np.where(B == -0., 0., B)
    C = np.where(C == -0., 0., C)
    return B, C

B, C = full_rank_decompose(A_np, H, pivot_cols)
print("满秩分解结果 A = B @ C：")
print("B (列满秩 17×rank)：")
print(np.round(B, 6))
print("\nC (行满秩 rank×17)：")
print(np.round(C, 6))
print()

# ========== 列向量组的极大无关组 + 施密特正交化求标准正交组 ==========
def schmidt_orthogonalization(vectors, tol=1e-10):
    """
    施密特正交化 + 单位化，得到标准正交组
    :param vectors: 列向量组成的矩阵 (n×k)
    :return: 标准正交列向量矩阵 (n×k)
    """
    n, k = vectors.shape
    ortho_vectors = np.zeros_like(vectors, dtype=np.float64)
    
    for i in range(k):
        # 正交化
        ortho_vectors[:, i] = vectors[:, i]
        for j in range(i):
            proj = np.dot(ortho_vectors[:, j].T, vectors[:, i]) / np.dot(ortho_vectors[:, j].T, ortho_vectors[:, j])
            ortho_vectors[:, i] -= proj * ortho_vectors[:, j]
        
        # 避免零向量（浮点误差）
        if np.linalg.norm(ortho_vectors[:, i]) < tol:
            continue
        
        # 单位化
        ortho_vectors[:, i] /= np.linalg.norm(ortho_vectors[:, i])
    
    # 去除零向量列
    ortho_vectors = ortho_vectors[:, np.linalg.norm(ortho_vectors, axis=0) > tol]
    return ortho_vectors

# 极大无关组：主元列对应的原矩阵列向量
max_independent_cols = A_np.astype(np.float64)[:, pivot_cols]
print("A 的列向量组的一个极大无关组（主元列）：")
print(np.round(max_independent_cols, 6))

# 施密特正交化得到标准正交组
standard_ortho_group = schmidt_orthogonalization(max_independent_cols)
print("\n极大无关组的标准正交组：")
print(np.round(standard_ortho_group, 6))
print()

# ========== 求 A + A^T 的正、负惯性系数 ==========
def inertia_coefficients(matrix, tol=1e-10):
    """
    计算实对称矩阵的正负惯性系数（特征值正负个数）
    :param matrix: 实对称矩阵
    :return: positive, negative
    """
    # 计算特征值
    eig_vals = np.linalg.eigvals(matrix.astype(np.float64))
    # 统计正负特征值个数（排除零特征值）
    positive = np.sum(eig_vals > tol)
    negative = np.sum(eig_vals < -tol)
    return positive, negative

# 计算 A + A^T
A_plus_AT = A_np + A_np.T
# 计算正负惯性系数
pos_inertia, neg_inertia = inertia_coefficients(A_plus_AT)
print("矩阵 A + A^T：")
print(np.round(A_plus_AT, 6))
print(f"\nA + A^T 的正惯性系数：{pos_inertia}")
print(f"A + A^T 的负惯性系数：{neg_inertia}")