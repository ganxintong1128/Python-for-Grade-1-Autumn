from math import sin, cos  # 从math模块导入sin、cos函数

def our_decorator(func):
    def function_wrapper(x):
        # 调用原函数前的操作：打印函数名
        print("Before calling " + func.__name__)
        # 执行原函数，获取结果
        res = func(x)
        # 打印原函数的返回值
        print(res)
        # 调用原函数后的操作：打印函数名
        print("After calling " + func.__name__)
        return res
    return function_wrapper

sin = our_decorator(sin)  # 用装饰器包装sin，覆盖原sin
cos = our_decorator(cos)  # 用装饰器包装cos，覆盖原cos

for f in [sin, cos]:
    f(3.1415)  # 调用装饰后的sin、cos