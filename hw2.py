# 连续从控制台读入三个数（input()默认返回字符串类型）
a = input("请输入第一个数：")
b = input("请输入第二个数：")
c = input("请输入第三个数：")
# 分别将三个输入转换为int类型
a1 = int(a)
b1 = int(b)
c1 = int(c)
# 分别将三个输入转换为float类型
a2 = float(a)
b2 = float(b)
c2 = float(c)
# 一行输出int类型的三个数
print("转换为整型的结果：",a1,b1,c1)
# 一行输出float类型的三个数
print("转换为浮点型的结果：",a2,b2,c2)




import math  
def calculate_triangle(a, b, c):
    # 判断能否构成三角形 
    # 先确保三边均为正数，且最长边 < 另外两边之和
    sides = [a, b, c]
    max_side = max(sides)
    sum_other = sum(sides) - max_side  # 另外两边之和
    
    if a <= 0 or b <= 0 or c <= 0:
        return "错误：三角形边长必须为正数！"
    elif max_side >= sum_other:
        return "错误：给定三边无法构成三角形（最长边≥另外两边之和）！"
    # 计算核心参数 
    # 1. 半周长
    s = (a + b + c) / 2
    # 2. 三角形面积（海伦公式）
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    # 3. 三个内角的弧度值（余弦定理 + arccos，处理浮点数精度误差）
    # 用max(min(..., 1.0), -1.0)避免acos参数超出[-1,1]（浮点数计算误差导致）
    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    angle_A = math.acos(max(min(cos_A, 1.0), -1.0))  # 角A（对应边a）

    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    angle_B = math.acos(max(min(cos_B, 1.0), -1.0))  # 角B（对应边b）
    
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    angle_C = math.acos(max(min(cos_C, 1.0), -1.0))  # 角C（对应边c）
    
    # 4. 外接圆：半径R + 面积
    R = (a * b * c) / (4 * area)
    circle_out_area = math.pi * (R ** 2)
    
    # 5. 内切圆：半径r + 面积
    r = area / s
    circle_in_area = math.pi * (r ** 2)
    
    # 格式化输出（保留3位小数）
    result = f"""
三角形计算结果（边长：a={a:.3f}, b={b:.3f}, c={c:.3f}）：
1. 三角形面积：{area:.3f}
2. 内角弧度值：
   - 角A（对应边a）：{angle_A:.3f}
   - 角B（对应边b）：{angle_B:.3f}
   - 角C（对应边c）：{angle_C:.3f}
   （验证：内角和 ≈ {angle_A + angle_B + angle_C:.3f}，理论值≈{math.pi:.3f}）
3. 外接圆：
   - 半径：{R:.3f}
   - 面积：{circle_out_area:.3f}
4. 内切圆：
   - 半径：{r:.3f}
   - 面积：{circle_in_area:.3f}
    """
    return result

# 主程序：输入三边并调用函数 
if __name__ == "__main__":
    # 读取用户输入的三个边长（转换为浮点数）
    try:
        a = float(input("请输入三角形边长a："))
        b = float(input("请输入三角形边长b："))
        c = float(input("请输入三角形边长c："))
    except ValueError:
        print("错误：请输入合法的数字！")
    else:
        # 调用计算函数并打印结果
        print(calculate_triangle(a, b, c))


        

expr = input("请输入一个数学表达式（例如1+2+3、(10-2)*3等）：")

try:
    # 计算表达式的值
    result = eval(expr)
    
    # 按指定格式输出
    print(f"{expr} = {result}.")

except Exception as e:
    # 处理非法表达式
    print(f"错误：输入的数学表达式「{expr}」不合法，请重新输入有效的数学表达式（例如1+2*3、(5-1)/2）。")




try:
    # 读取输入并转换为float
    num1 = float(input("请输入第一个数："))
    num2 = float(input("请输入第二个数："))
    
    # 交换两个数的值（Python简洁写法，无需临时变量）
    # 交换前先保存原始值，用于输出对比（可选，增强可读性）
    original_num1, original_num2 = num1, num2
    num1, num2 = num2, num1  # 核心交换逻辑
    
    # 计算交换后“第一个数 - 第二个数”的差
    difference = num1 - num2
    
    # 格式化输出（清晰展示交换前后、差值）
    print(f"\n交换前：第一个数 = {original_num1:.2f}, 第二个数 = {original_num2:.2f}")
    print(f"交换后：第一个数 = {num1:.2f}, 第二个数 = {num2:.2f}")
    print(f"交换后，第一个数 - 第二个数 = {num1:.2f} - {num2:.2f} = {difference:.2f}")

except ValueError:
    # 捕获“输入非数字”的错误
    print("错误：请输入合法的数字（整数或小数，例如3、5.2）！")





import math  

# 计算三角形面积 
def area(a, b, c):
    """
    计算三角形面积（海伦公式）
    参数：a, b, c - 三角形三边长度（正数）
    返回：合法时返回面积（float）；不合法时返回None
    """
    # 验证三边能否构成三角形（正数 + 最长边 < 另外两边之和）
    sides = [a, b, c]
    max_side = max(sides)
    sum_others = sum(sides) - max_side  # 另外两边之和
    
    if a <= 0 or b <= 0 or c <= 0:
        return None  # 边长为非正数，无效
    if max_side >= sum_others:
        return None  # 最长边≥另外两边之和，无法构成三角形
    
    # 海伦公式计算面积
    s = (a + b + c) / 2  # 半周长
    area_val = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area_val

# 计算三个内角的弧度值 
def angle(a, b, c):
    """
    计算三角形三个内角的弧度值（对应边a→角A，边b→角B，边c→角C）
    参数：a, b, c - 三角形三边长度（正数）
    返回：合法时返回元组(角A, 角B, 角C)；不合法时返回None
    """
    # 先通过面积函数验证三边合法性（避免重复代码）
    if area(a, b, c) is None:
        return None
    
    # 余弦定理计算每个角的余弦值，并用acos转弧度（处理浮点数精度误差）
    # 角A（对边a）：cosA = (b² + c² - a²)/(2bc)
    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_A = max(min(cos_A, 1.0), -1.0)  # 限制范围在[-1,1]，避免acos报错
    angle_A = math.acos(cos_A)
    
    # 角B（对边b）：cosB = (a² + c² - b²)/(2ac)
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    cos_B = max(min(cos_B, 1.0), -1.0)
    angle_B = math.acos(cos_B)
    
    # 角C（对边c）：cosC = (a² + b² - c²)/(2ab)
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    cos_C = max(min(cos_C, 1.0), -1.0)
    angle_C = math.acos(cos_C)
    
    return (angle_A, angle_B, angle_C)


# 计算外接圆参数（半径+面积） 
def circumcircle(a, b, c):
    """
    计算三角形外接圆的半径和面积
    参数：a, b, c - 三角形三边长度（正数）
    返回：合法时返回元组(外接圆半径, 外接圆面积)；不合法时返回None
    """
    area_val = area(a, b, c)
    if area_val is None:
        return None  # 三边无效，直接返回None
    
    # 外接圆半径公式：R = (a*b*c)/(4*面积)
    R = (a * b * c) / (4 * area_val)
    # 外接圆面积公式：π*R²
    circum_area = math.pi * (R ** 2)
    
    return (R, circum_area)


# 计算内切圆参数（半径+面积） 
def incircle(a, b, c):
    """
    计算三角形内切圆的半径和面积
    参数：a, b, c - 三角形三边长度（正数）
    返回：合法时返回元组(内切圆半径, 内切圆面积)；不合法时返回None
    """
    area_val = area(a, b, c)
    if area_val is None:
        return None  # 三边无效，直接返回None
    
    # 半周长
    s = (a + b + c) / 2
    # 内切圆半径公式：r = 面积 / 半周长
    r = area_val / s
    # 内切圆面积公式：π*r²
    in_area = math.pi * (r ** 2)
    
    return (r, in_area)


# 主程序：调用函数并展示结果 
if __name__ == "__main__":
    try:
        # 1. 从控制台读取三边长度
        a = float(input("请输入三角形第一条边的长度："))
        b = float(input("请输入三角形第二条边的长度："))
        c = float(input("请输入三角形第三条边的长度："))
    except ValueError:
        # 处理“输入非数字”的错误
        print("\n错误：请输入合法的数字（例如3、4.5、5），不要输入文字或符号！")
    else:
        # 2. 调用各函数获取结果（先通过面积函数判断三边合法性）
        tri_area = area(a, b, c)
        if tri_area is None:
            print(f"\n错误：三边（{a:.3f}, {b:.3f}, {c:.3f}）无法构成有效的三角形！")
            print("    请确保三边均为正数，且任意两边之和大于第三边。")
        else:
            tri_angles = angle(a, b, c)
            circum_info = circumcircle(a, b, c)  # (外接圆半径, 外接圆面积)
            in_info = incircle(a, b, c)          # (内切圆半径, 内切圆面积)
            
            # 3. 按格式输出结果（保留三位小数）
            print("\n三角形相关参数计算结果（保留3位小数）")
            print("-" * 50)
            print(f"1. 三角形面积：{tri_area:.3f}")
            print(f"2. 三个内角的弧度值（对应边a、b、c）：")
            print(f"   角A（对边a）：{tri_angles[0]:.3f}")
            print(f"   角B（对边b）：{tri_angles[1]:.3f}")
            print(f"   角C（对边c）：{tri_angles[2]:.3f}")
            print(f"3. 外接圆：")
            print(f"   半径：{circum_info[0]:.3f} | 面积：{circum_info[1]:.3f}")
            print(f"4. 内切圆：")
            print(f"   半径：{in_info[0]:.3f} | 面积：{in_info[1]:.3f}")
            
            # 可选：验证内角和（理论值为π≈3.142，因浮点数误差可能略有偏差）
            angle_sum = sum(tri_angles)
            print(f"5. 内角和验证：{angle_sum:.3f}（理论值：{math.pi:.3f}）")
            print("-" * 50)




import math

def f(x1, y1, r1, x2, y2, r2):
    """
    判断两个圆的交点数目
    参数：
        x1, y1: 第一个圆的圆心坐标（float/int）
        r1: 第一个圆的半径（float/int，需为正数）
        x2, y2: 第二个圆的圆心坐标（float/int）
        r2: 第二个圆的半径（float/int，需为正数）
    返回：
        int: 交点数目（0、1）；若重合则返回字符串"无数个"；若圆无效返回0
    说明：
        处理浮点数精度误差（阈值1e-8），避免因计算误差导致判断错误
    """
    # 1. 先判断圆是否有效（半径必须为正数，非正半径则圆不存在）
    if r1 <= 1e-8 or r2 <= 1e-8:  # 用1e-8替代0，避免浮点数"0.00000001"被误判为有效
        return 0
    
    # 2. 计算两圆圆心距 d（两点间距离公式）
    dx = x2 - x1  # x方向距离
    dy = y2 - y1  # y方向距离
    d = math.sqrt(dx ** 2 + dy ** 2)  # 圆心距
    
    # 3. 计算半径和、半径差的绝对值
    r_sum = r1 + r2  # 半径和
    r_diff = abs(r1 - r2)  # 半径差的绝对值
    
    # 4. 处理浮点数精度：判断两个值是否"相等"（差值小于1e-8则认为相等）
    def is_equal(a, b):
        return abs(a - b) < 1e-8
    
    # 5. 根据位置关系判断交点数
    if is_equal(d, 0):  # 两圆圆心重合
        if is_equal(r1, r2):  # 半径也相等 → 两圆重合
            return "无数个"
        else:  # 半径不相等 → 内含（无交点）
            return 0
    elif is_equal(d, r_sum):  # 外切 → 1个交点
        return 1
    elif is_equal(d, r_diff):  # 内切 → 1个交点
        return 1
    elif d > r_sum:  # 外离 → 0个交点
        return 0
    elif d < r_diff:  # 内含（非重合） → 0个交点
        return 0
    else:  # 剩下的情况：r_diff < d < r_sum → 相交 → 2个交点
        return 2


# 主程序
if __name__ == "__main__":
    print("请输入两个圆的参数（圆心坐标和半径，用空格分隔，例如：0 0 1 2 0 1）")
    print("格式：圆1_x 圆1_y 圆1_r 圆2_x 圆2_y 圆2_r")
    
    try:
        # 读取用户输入并转换为浮点数（支持整数/小数）
        x1, y1, r1, x2, y2, r2 = map(float, input("请输入参数：").split())
        
        # 调用函数判断交点数
        intersection_count = f(x1, y1, r1, x2, y2, r2)
        
        # 格式化输出结果
        print(f"\n圆1：圆心({x1:.2f}, {y1:.2f})，半径{r1:.2f}")
        print(f"圆2：圆心({x2:.2f}, {y2:.2f})，半径{r2:.2f}")
        print(f"两圆的交点数目：{intersection_count}")
    
    except ValueError:
        # 处理输入格式错误（如输入非数字、参数个数不对）
        print("\n输入错误！请按格式输入6个数字（用空格分隔），例如：0 0 1 2 0 1")
    except Exception as e:
        # 捕获其他意外错误
        print(f"\n程序运行出错：{e}")