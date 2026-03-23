# Framework for IEEE course final project
# Fan Cheng, 2022
# 1. 导入原生 random 模块并起别名（唯一入口，避免所有冲突）
import random as natran


# 2. 自定义 Random 类：封装种子控制和随机数生成
class Random:
    def seed(self, seed_val):
        """设置随机数种子（转发到原生 random 模块）"""
        # 明确调用原生模块的 seed 方法（用别名 natran）
        natran.seed(seed_val)

    def random(self):
        """生成 [0,1) 随机数（转发到原生 random 模块）"""
        # 明确调用原生模块的 random 方法（用别名 natran）
        return natran.random()


# 3. 实例化自定义 Random 类：外部通过 mm.random 访问
random = Random()


class Matrix:
    r"""
    自定义的二维矩阵类
    Args:
        data: 一个二维的嵌套列表，表示矩阵的数据。即 data[i][j] 表示矩阵第 i+1 行第 j+1 列处的元素。
              当参数 data 不为 None 时，应根据参数 data 确定矩阵的形状。默认值: None
        dim: 一个元组 (n, m) 表示矩阵是 n 行 m 列, 当参数 data 为 None 时，根据该参数确定矩阵的形状；
             当参数 data 不为 None 时，忽略该参数。如果 data 和 dim 同时为 None, 应抛出异常。默认值: None
        init_value: 当提供的 data 参数为 None 时，使用该 init_value 初始化一个 n 行 m 列的矩阵，
                    即矩阵各元素均为 init_value. 当参数 data 不为 None 时，忽略该参数。 默认值: 0

    Attributes:
        dim: 一个元组 (n, m) 表示矩阵的形状
        data: 一个二维的嵌套列表，表示矩阵的数据
    """

    def __init__(self, data=None, dim=None, init_value=0):
        if data is None and dim is None:
            raise ValueError("data 和 dim 不能同时为 None")
        if data is not None:
            # 验证 data 是二维列表
            if not isinstance(data, list) or not all(
                isinstance(row, list) for row in data
            ):
                raise TypeError("data 必须是二维嵌套列表")

            row_length = len(data[0])
            self.data = [row.copy() for row in data]
            self.dim = (len(data), row_length)
        else:
            n, m = dim
            self.data = [[init_value for _ in range(m)] for _ in range(n)]
            self.dim = (n, m)

    def shape(self):
        r"""
        返回矩阵的形状 dim
        """
        return self.dim

    def reshape(self, newdim):
        # dim=(n,m) n行m列
        r"""
        将矩阵从(n,m)维拉伸为newdim=(n1,m1)
        该函数不改变 self

        Args:
            newdim: 一个元组 (n1, m1) 表示拉伸后的矩阵形状。如果 n1 * m1 不等于 self.dim[0] * self.dim[1],
                    应抛出异常

        Returns:
            Matrix: 一个 Matrix 类型的返回结果, 表示 reshape 得到的结果
        """
        n, m = self.dim
        n1, m1 = newdim
        if n1 * m1 != n * m:
            raise ValueError("形状不匹配")

        new_list = []
        for row in self.data:
            for elem in row:
                new_list.append(elem)
        new_data = [new_list[i * m1 : (i + 1) * m1] for i in range(n1)]

        return Matrix(data=new_data)

    def dot(self, other):
        r"""
        矩阵乘法：矩阵乘以矩阵
        按照公式 A[i, j] = \sum_k B[i, k] * C[k, j] 计算 A = B.dot(C)
        Args:
            other: 参与运算的另一个 Matrix 实例

        Returns:
            Matrix: 计算结果
        """
        n1, m1 = self.dim
        n2, m2 = other.dim
        if m1 != n2:
            raise ValueError("矩阵形状不匹配")

        result_data = [[0 for i in range(m2)] for j in range(n1)]

        # 矩阵乘法核心计算
        for i in range(n1):
            for k in range(m1):
                if self.data[i][k] == 0:
                    continue  # 优化：跳过零元素
                for j in range(m2):
                    result_data[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(data=result_data)

    def T(self):
        r"""
        矩阵的转置
        Returns:
            Matrix: 矩阵的转置
        """
        m, n = self.dim
        T_data = [[self.data[i][j] for i in range(m)] for j in range(n)]
        return Matrix(data=T_data)

    def sum(self, axis=None):
        r"""
        根据指定的坐标轴对矩阵元素进行求和
        Args:
            axis: 一个整数，或者 None. 默认值: None
                  axis = 0 表示对矩阵进行按列求和，得到形状为 (1, self.dim[1]) 的矩阵
                  axis = 1 表示对矩阵进行按行求和，得到形状为 (self.dim[0], 1) 的矩阵
                  axis = None 表示对矩阵全部元素进行求和，得到形状为 (1, 1) 的矩阵

        Returns:
            Matrix: 一个 Matrix 类的实例，表示求和结果
        """
        n, m = self.dim
        if axis is None:
            # 所有元素求和
            total = sum(sum(row) for row in self.data)
            return Matrix(data=[[total]])
        elif axis == 0:
            # 按列求和
            column_sum = [sum(self.data[i][j] for i in range(n)) for j in range(m)]
            return Matrix(data=[column_sum])
        elif axis == 1:
            # 按行求和
            row_sum = [[sum(row)] for row in self.data]
            return Matrix(data=row_sum)

    def copy(self):
        r"""
        返回matrix的一个备份
        Returns:
            Matrix: 一个self的备份
        """
        return Matrix(data=[row.copy() for row in self.data])

    def Kronecker_product(self, other):
        r"""
        计算两个矩阵的Kronecker积
        Args:
            other: 参与运算的另一个 Matrix
        Returns:
            Matrix: Kronecker product 的计算结果
        """
        n1, m1 = self.dim
        n2, m2 = other.dim
        result_data = [[0 for _ in range(m1 * m2)] for _ in range(n1 * n2)]

        for result_row in range(n1 * n2):
            for result_column in range(m1 * m2):
                # A的行索引：
                i = result_row // n2
                # B的行索引：
                k = result_row % n2
                # A的列索引：
                j = result_column // m2
                # B的列索引：
                l = result_column % m2

                # Kronecker积：A[i][j] * B[k][l]
                result_data[result_row][result_column] = (
                    self.data[i][j] * other.data[k][l]
                )

        return Matrix(data=result_data)

    def __getitem__(self, key):
        r"""
        实现 Matrix 的索引功能
        """

        row_idx, col_idx = key
        n, m = self.dim

        # 处理行索引
        if isinstance(row_idx, int):
            row_start = row_idx
            row_end = row_idx + 1
        elif isinstance(row_idx, slice):
            row_start = row_idx.start if row_idx.start is not None else 0
            row_end = row_idx.stop if row_idx.stop is not None else n
            row_start = max(0, row_start)
            row_end = min(n, row_end)

        # 处理列索引
        if isinstance(col_idx, int):
            col_start = col_idx
            col_end = col_idx + 1
        elif isinstance(col_idx, slice):
            col_start = col_idx.start if col_idx.start is not None else 0
            col_end = col_idx.stop if col_idx.stop is not None else m
            col_start = max(0, col_start)
            col_end = min(m, col_end)

        # 单元素索引
        if row_end - row_start == 1 and col_end - col_start == 1:
            return self.data[row_start][col_start]
        # 矩阵切片
        else:
            sliced_data = [
                row[col_start:col_end] for row in self.data[row_start:row_end]
            ]
            return Matrix(data=sliced_data)

    def __setitem__(self, key, value):
        r"""
        实现 Matrix 的赋值功能
        """

        row_idx, col_idx = key
        n, m = self.dim

        # 处理行索引
        if isinstance(row_idx, int):
            row_start = row_idx
            row_end = row_idx + 1
        elif isinstance(row_idx, slice):
            row_start = row_idx.start if row_idx.start is not None else 0
            row_end = row_idx.stop if row_idx.stop is not None else n
            row_start = max(0, row_start)
            row_end = min(n, row_end)

        # 处理列索引
        if isinstance(col_idx, int):
            col_start = col_idx
            col_end = col_idx + 1
        elif isinstance(col_idx, slice):
            col_start = col_idx.start if col_idx.start is not None else 0
            col_end = col_idx.stop if col_idx.stop is not None else m
            col_start = max(0, col_start)
            col_end = min(m, col_end)

        # 验证赋值范围
        rows_needed = row_end - row_start
        cols_needed = col_end - col_start

        # 单元素赋值
        if rows_needed == 1 and cols_needed == 1:
            self.data[row_start][col_start] = value
        # 矩阵切片赋值
        else:
            val_n, val_m = value.dim
            if val_n != rows_needed or val_m != cols_needed:
                raise ValueError("赋值矩阵形状与目标切片形状不匹配")

            for i in range(rows_needed):
                for j in range(cols_needed):
                    self.data[row_start + i][col_start + j] = value.data[i][j]

    def __pow__(self, power):
        r"""
        矩阵的power次幂,power为自然数
        """

        n, m = self.dim
        if n != m:
            raise ValueError("只有方阵才能进行幂运算")

        result = I(n)
        base = self.copy()
        while power > 0:
            if power % 2 == 1:
                result = result.dot(base)
            base = base.dot(base)
            power = power // 2
        return result

    def __add__(self, other):
        r"""
        两个矩阵相加
        """
        if self.dim != other.dim:
            raise ValueError("矩阵形状不匹配")

        n, m = self.dim
        result_data = [
            [self.data[i][j] + other.data[i][j] for j in range(m)] for i in range(n)
        ]
        return Matrix(data=result_data)

    def __sub__(self, other):
        r"""
        两个矩阵相减
        """
        if self.dim != other.dim:
            raise ValueError("矩阵形状不匹配")

        n, m = self.dim
        result_data = [
            [self.data[i][j] - other.data[i][j] for j in range(m)] for i in range(n)
        ]
        return Matrix(data=result_data)

    def __mul__(self, other):
        r"""
        支持：
        1. 矩阵 × 标量（所有元素乘以标量）
        2. 矩阵 × 矩阵（Hadamard积，对应元素相乘）
        """
        # 情况1：矩阵 × 标量（other是数字）
        if isinstance(other, (int, float)):
            n, m = self.dim
            result_data = [
                [self.data[i][j] * other for j in range(m)] for i in range(n)
            ]
            return Matrix(data=result_data)
        # 情况2：矩阵 × 矩阵（Hadamard积）
        elif isinstance(other, Matrix):
            if self.dim != other.dim:
                raise ValueError("Hadamard积要求矩阵形状完全相同")
            result_data = [
                [self.data[i][j] * other.data[i][j] for j in range(self.dim[1])]
                for i in range(self.dim[0])
            ]
            return Matrix(data=result_data)
        else:
            raise TypeError(f"不支持 Matrix 与 {type(other)} 的乘法运算")

    def __rmul__(self, other):
        r"""
        支持：标量 × 矩阵（调用 __mul__ 复用逻辑，保证交换律）
        """
        # 标量 × 矩阵 等价于 矩阵 × 标量，直接复用 __mul__ 方法
        return self.__mul__(other)

    def __len__(self):
        r"""
        返回矩阵元素的数目
        """
        length = self.dim[0] * self.dim[1]
        return length

    def minor_matrix(self, i, j):
        """生成去掉第i行和第j列的矩阵"""
        n = self.dim[0]
        if self.dim[0] != self.dim[1]:
            raise ValueError("只有方阵才能生成余子式矩阵")
        if not (0 <= i < n and 0 <= j < n):
            raise IndexError(f"索引 i={i}, j={j} 超出矩阵范围 [0, {n-1}]")

        minor_data = [
            [self.data[a][b] for b in range(n) if b != j] for a in range(n) if a != i
        ]
        minor_mat = Matrix(data=minor_data)
        return minor_mat

    def gauss_elim(self, mode="det"):
        """
        【类私有方法】通用高斯消元函数（优化版：全选主元+数值稳定）
        支持 det/inv/rank 三种模式
        Args:
            mode: 消元模式，可选 "det" / "inv" / "rank"
        Returns:
            mode="det": (upper_mat, swap_count, col_swaps) → 上三角矩阵、行交换次数、列交换次数
            mode="inv": reduced_mat → 简化行阶梯形增广矩阵
            mode="rank": echelon_mat → 行阶梯形矩阵
        Raises:
            ValueError: 模式错误或矩阵格式错误
        """
        valid_modes = ["det", "inv", "rank"]
        if mode not in valid_modes:
            raise ValueError(f"mode 必须是 {valid_modes} 中的一种")

        n, m = self.dim
        if mode == "inv":
            if n != m:
                raise ValueError("只有方阵才能求逆")
            mat_data = []
            for i in range(n):
                row = self.data[i].copy()
                row.extend([1.0 if i == j else 0.0 for j in range(n)])
                mat_data.append(row)
            mat_n, mat_m = n, 2 * n
        else:
            mat_data = [row.copy() for row in self.data]
            mat_n, mat_m = n, m

        mat = mat_data
        swap_count = 0  # 行交换次数（用于行列式符号）
        col_swaps = []  # 列交换记录（用于行列式符号）

        for col in range(min(mat_n, mat_m)):
            # 全选主元：找到当前列及右侧所有列、当前行及下方所有行中的最大元素
            max_val = 0
            pivot_row = -1
            pivot_col = -1
            for r in range(col, mat_n):
                for c in range(col, mat_m):
                    if abs(mat[r][c]) > abs(max_val):
                        max_val = mat[r][c]
                        pivot_row = r
                        pivot_col = c

            # 若所有剩余元素都是0，说明矩阵奇异（或秩不足）
            if abs(max_val) < 1e-12:
                if mode == "det":
                    return mat, swap_count, col_swaps
                elif mode == "inv":
                    raise ValueError("奇异矩阵无法求逆")
                else:
                    continue

            # 交换行（当前行与主元行）
            if pivot_row != col:
                mat[col], mat[pivot_row] = mat[pivot_row], mat[col]
                swap_count += 1

            # 交换列（仅行列式和求逆模式需要，记录列交换用于修正行列式符号）
            if pivot_col != col and mode in ["det", "inv"]:
                for r in range(mat_n):
                    mat[r][col], mat[r][pivot_col] = mat[r][pivot_col], mat[r][col]
                col_swaps.append((col, pivot_col))  # 记录列交换

            # 主元归一化（提高数值稳定性）
            pivot = mat[col][col]
            if abs(pivot) > 1e-12:
                for j in range(col, mat_m):
                    mat[col][j] /= pivot

            # 消元：将主元下方/所有行的当前列元素变为0
            for row in range(mat_n):
                if row != col and abs(mat[row][col]) > 1e-12:
                    factor = mat[row][col]
                    for j in range(col, mat_m):
                        mat[row][j] -= factor * mat[col][j]

        if mode == "det":
            return mat, swap_count, col_swaps
        elif mode == "inv":
            # 还原列交换（求逆模式需将列交换恢复）
            for col1, col2 in reversed(col_swaps):
                for r in range(mat_n):
                    mat[r][col1], mat[r][col2] = mat[r][col2], mat[r][col1]
            return mat
        else:
            return mat

    def det(self):
        """
        调用通用高斯消元函数(det模式)计算行列式（适配全选主元）
        """
        n, m = self.dim
        if n != m:
            raise ValueError("只有方阵才能计算行列式！")
        upper_mat, swap_count, col_swaps = self.gauss_elim(mode="det")
        det_val = 1.0
        for i in range(n):
            det_val *= upper_mat[i][i]
            if abs(det_val) < 1e-12:
                return 0.0
        # 列交换次数影响行列式符号（每交换一次列，符号取反）
        col_swap_count = len(col_swaps)
        return det_val * ((-1) ** (swap_count + col_swap_count))

    def inverse(self):
        """
        调用通用高斯消元函数(inv模式)计算逆矩阵
        """
        n, m = self.dim
        if n != m:
            raise ValueError("只有方阵才能求逆")
        reduced_aug = self.gauss_elim(mode="inv")
        inv_data = [row[n:] for row in reduced_aug]
        return Matrix(data=inv_data)

    def least_squares(self, Y):
        r"""
        普通最小二乘估计（OLS）：求解模型 Y = X @ w + e 的最优参数 w
        公式：w_hat = (X^T X)^{-1} X^T Y
        Args:
            Y: 响应变量矩阵（形状：(m, 1)，m为样本数）
        Returns:
            Matrix: 参数估计值 w_hat（形状：(n, 1)，n为特征数）
        Raises:
            ValueError: 矩阵形状不匹配 / 奇异矩阵无法求逆
        """
        X = self  # self 是特征矩阵 X (m×n)
        m, n = X.dim
        y_m, y_n = Y.dim

        # 验证形状：Y必须是列向量，且样本数与X一致
        if y_n != 1 or y_m != m:
            raise ValueError(f"Y形状必须为({m}, 1)，实际为({y_m}, {y_n})")

        # 计算 X^T X 和 X^T Y
        X_T = X.T()
        X_T_X = X_T.dot(X)
        X_T_Y = X_T.dot(Y)

        # 直接求 X^T X 的逆（优化后的高斯消元会处理数值稳定性）
        try:
            X_T_X_inv = X_T_X.inverse()
        except ValueError as e:
            raise ValueError(
                "X^T X 是奇异矩阵，无法求逆，请增加样本数或减少特征数"
            ) from e

        # 计算参数估计值
        w_hat = X_T_X_inv.dot(X_T_Y)
        return w_hat

    def rank(self):
        """计算矩阵的秩"""
        echelon_mat = self.gauss_elim(mode="rank")
        rank_val = 0
        for row in echelon_mat:
            if any(abs(elem) > 1e-12 for elem in row):
                rank_val += 1
        return rank_val

    def __str__(self):
        r"""
        格式化矩阵字符串输出
        """
        if self.dim == (0, 0):
            return "[]"

        # 找到所有元素的最大宽度（用于对齐）
        max_width = 0
        for row in self.data:
            for elem in row:
                elem_str = f"{elem:.6g}"
                max_width = max(max_width, len(elem_str))

        # 构造每行的字符串
        rows_str = []
        for row in self.data:
            row_elems = [f"{elem:.6g}".rjust(max_width) for elem in row]
            rows_str.append(f"[{ ' '.join(row_elems) }]")

        return "[\n " + "\n ".join(rows_str) + "\n]"


def I(n):
    r"""
    返回n*n的单位矩阵
    """
    if not isinstance(n, int) or n < 0:
        raise TypeError("n 必须是非负整数")
    data = [[1 if i == j else 0.0 for j in range(n)] for i in range(n)]
    return Matrix(data=data)


def narray(dim, init_value=1):
    r"""
    返回一个matrix,维数为dim,初始值为init_value
    """
    if (
        not isinstance(dim, tuple)
        or len(dim) != 2
        or not all(isinstance(x, int) and x >= 0 for x in dim)
    ):
        raise TypeError("dim 必须是包含两个非负整数的元组")
    return Matrix(dim=dim, init_value=init_value)


def arange(start, end, step):
    r"""
    返回一个1*n 的 Matrix,元素类同 range(start, end, step)
    """
    if not all(isinstance(x, (int, float)) for x in [start, end, step]):
        raise TypeError("start、end、step 必须是数字")
    if step == 0:
        raise ValueError("step 不能为0")

    # 生成序列
    arr = []
    current = start
    if step > 0:
        while current < end:
            arr.append(current)
            current += step
    else:
        while current > end:
            arr.append(current)
            current += step

    return Matrix(data=[arr])


def concatenate(items, axis=0):
    r"""
    将若干矩阵按照指定的方向拼接起来
    """
    if not isinstance(items, (list, tuple)) or len(items) == 0:
        raise ValueError("items 必须是包含至少一个 Matrix 的可迭代对象")
    if not all(isinstance(item, Matrix) for item in items):
        raise TypeError("items 中的所有元素必须是 Matrix 实例")
    if axis not in (0, 1):
        raise ValueError("axis 必须是 0 或 1")

    first = items[0]
    n0, m0 = first.dim

    if axis == 0:
        if not all(item.dim[1] == m0 for item in items):
            raise ValueError("按行拼接时，所有矩阵的列数必须相同")
        data = []
        for item in items:
            data.extend(item.data)
        return Matrix(data=data)
    else:
        if not all(item.dim[0] == n0 for item in items):
            raise ValueError("按列拼接时，所有矩阵的行数必须相同")
        data = []
        for i in range(n0):
            row = []
            for item in items:
                row.extend(item.data[i])
            data.append(row)
        return Matrix(data=data)


def vectorize(func):
    r"""
    将给定函数进行向量化
    """

    def vectorized_func(matrix):
        if not isinstance(matrix, Matrix):
            raise TypeError("参数必须是 Matrix 实例")
        data = [[func(elem) for elem in row] for row in matrix.data]
        return Matrix(data=data)

    return vectorized_func


def zeros(dim):
    r"""
    返回一个维数为dim 的全0 Matrix
    """
    return narray(dim, init_value=0)


def zeros_like(matrix):
    r"""
    返回一个形状和matrix一样的全0 Matrix
    """
    if not isinstance(matrix, Matrix):
        raise TypeError("matrix 必须是 Matrix 实例")
    return zeros(matrix.dim)


def ones(dim):
    r"""
    返回一个维数为dim 的全1 Matrix
    """
    return narray(dim, init_value=1)


def ones_like(matrix):
    r"""
    返回一个形状和matrix一样的全1 Matrix
    """
    if not isinstance(matrix, Matrix):
        raise TypeError("matrix 必须是 Matrix 实例")
    return ones(matrix.dim)


def nrandom(dim):
    r"""
    返回一个维数为dim 的随机 Matrix(元素范围[0,1))
    """
    if (
        not isinstance(dim, tuple)
        or len(dim) != 2
        or not all(isinstance(x, int) and x >= 0 for x in dim)
    ):
        raise TypeError("dim 必须是包含两个非负整数的元组")
    n, m = dim
    data = [[random.random() for _ in range(m)] for _ in range(n)]
    return Matrix(data=data)


def nrandom_like(matrix):
    r"""
    返回一个形状和matrix一样的随机 Matrix
    """
    if not isinstance(matrix, Matrix):
        raise TypeError("matrix 必须是 Matrix 实例")
    return nrandom(matrix.dim)
