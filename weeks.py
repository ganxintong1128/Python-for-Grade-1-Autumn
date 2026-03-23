# from pathlib import Path

# data_folder = Path("source_data/text_files/")
# file_to_open = data_folder / "raw_data.txt"
# print(file_to_open)

# filename = Path("source_data/text_files/raw_data.txt")
# print(filename.name)
# print(filename.suffix)
# print(filename.stem)

# data_folder = Path("source_data/text_files/")
# file_to_open = data_folder / "raw_data.txt"

# if not filename.exists():
#     print("Oops, file doesn't exist!")
# else:
#     print("Yay, the file exists!")

# mf = open('test.txt','w')
# mf.write('My first file written from Python\n')
# mf.write('----------------------------\n')
# mf.write('Hello, world\n')
# mf.close()

# res = ['123','We','US Election']
# wf = open('wtest.txt','w+')
# wf.writelines(res)
# wf.close()



# rf = open('test.txt','r')
# while True:
#     line = rf.readline()
#     print(line,end='')
#     if len(line)==0:
#         break
# print()
# rf.close

# f = open('test.txt','r')
# while True:
#     line = f.readline()
#     l = list(line)
#     print(l)
#     if len(l)==0:
#         break
# f.close

# with open('test.txt','r') as f:
#     line = f.readlines()
#     print(line)

# with open('test.txt','a') as f:
#     num = f.write('add')
#     print(num)

# with open("test.txt", "rb") as f:
#     # 第一步：移动到开头第 5 字节
#     f.seek(5, 0)
#     print(f"当前指针：{f.tell()}")  # tell() 获取当前指针位置，输出 5
    
#     # 第二步：从当前位置再移动 2 字节
#     f.seek(2, 1)
#     print(f"移动后指针：{f.tell()}")  # 输出 7
#     print(f.read().decode("utf-8"))  # 输出：好

# class A: 
#     def __init__(s): 
#         s.a = 1 
# a = A() 
# print(a.a)

class B: 
    def f(self): 
        return 1 
b = B() 
b.f()
print(b)