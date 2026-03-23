import os
from pathlib import Path

def demo_file_operations():
    """演示Python文件读写的各种核心方法"""
    # ===================== 1. 路径处理（推荐pathlib）=====================
    print("="*50)
    print("1. 路径处理（pathlib）")
    print("="*50)
    # 创建路径对象（跨平台自动适配斜杠）
    data_dir = Path("demo_files")
    text_file = data_dir / "text_demo.txt"  # 文本文件路径
    binary_file = data_dir / "binary_demo.bin"  # 二进制文件路径
    copy_file = data_dir / "binary_copy.bin"  # 复制后的二进制文件

    # 确保目录存在（不存在则创建）
    data_dir.mkdir(exist_ok=True)
    print(f"工作目录: {os.getcwd()}")
    print(f"文本文件路径: {text_file}")
    print(f"二进制文件路径: {binary_file}")

    # ===================== 2. 文本文件写入（3种方式）=====================
    print("\n" + "="*50)
    print("2. 文本文件写入")
    print("="*50)

    # 方式1：open() + close()（基础版，需手动关闭）
    f1 = open(text_file, "w", encoding="utf-8")  # w模式：覆盖写入（无文件则创建）
    f1.write("第一行：手动open+close写入\n")  # write()：写入字符串（无自动换行）
    f1.writelines([
        "第二行：writelines写入列表\n",
        "第三行：中文测试（utf-8编码）\n",
        "第四行：数字123和符号！@#\n"
    ])  # writelines()：写入字符串列表（无自动换行）
    f1.close()  # 必须手动关闭，否则可能数据丢失
    print("✓ 方式1：open()+close() 写入完成")

    # 方式2：with语句（推荐，自动关闭文件）
    with open(text_file, "a", encoding="utf-8") as f2:  # a模式：追加写入
        f2.write("第五行：with语句追加写入（自动关闭）\n")
        f2.write("第六行：避免忘记close()的最佳实践\n")
    print("✓ 方式2：with语句 追加写入完成")

    # 方式3：w+模式（读写混合，覆盖原有内容）
    with open(text_file, "w+", encoding="utf-8") as f3:
        f3.write("重新写入：w+模式（读写混合）\n")
        f3.write("第二行：写完后移动指针到开头才能读取\n")
        f3.seek(0)  # 移动文件指针到开头（否则读取不到内容）
        content = f3.read()  # 读取全部内容
        print(f"✓ 方式3：w+模式读取内容：\n{content}")

    # ===================== 3. 文本文件读取（4种方式）=====================
    print("\n" + "="*50)
    print("3. 文本文件读取")
    print("="*50)

    with open(text_file, "r", encoding="utf-8") as f:
        # 方式1：read()：读取全部内容（返回字符串）
        print("✓ 方式1：read() 读取全部内容：")
        all_content = f.read()
        print(all_content)

        # 方式2：readline()：逐行读取（每次读1行，含换行符）
        f.seek(0)  # 重置指针到开头
        print("✓ 方式2：readline() 逐行读取：")
        line1 = f.readline()
        line2 = f.readline()
        print(f"第1行：{line1.strip()}")  # strip()去除换行符
        print(f"第2行：{line2.strip()}")

        # 方式3：readlines()：读取所有行（返回列表）
        f.seek(0)
        print("✓ 方式3：readlines() 读取所有行（列表）：")
        lines = f.readlines()
        print(lines)  # 每行末尾含\n
        # 处理列表：去除换行符
        clean_lines = [line.strip() for line in lines]
        print(f"处理后：{clean_lines}")

        # 方式4：文件对象迭代（最Pythonic，高效省内存）
        f.seek(0)
        print("✓ 方式4：文件对象迭代（逐行读取）：")
        for idx, line in enumerate(f, 1):
            print(f"第{idx}行：{line.strip()}")

    # ===================== 4. 二进制文件操作（读写+复制）=====================
    print("\n" + "="*50)
    print("4. 二进制文件操作（图片/视频/压缩包等）")
    print("="*50)

    # 写入二进制文件（模拟生成二进制数据）
    binary_data = b"\x00\x01\x02\x03\x04\x05\xff\xfe\xfd\xfc"  # 二进制字节流
    with open(binary_file, "wb") as f_bin:  # wb模式：二进制写入
        f_bin.write(binary_data)
    print(f"✓ 二进制文件写入完成（大小：{os.path.getsize(binary_file)}字节）")

    # 读取二进制文件并复制
    with open(binary_file, "rb") as f_in, open(copy_file, "wb") as f_out:
        # 缓冲区读取（大文件推荐，避免占用过多内存）
        buffer_size = 4  # 每次读取4字节
        while True:
            buf = f_in.read(buffer_size)  # 读取缓冲区大小的数据
            if not buf:  # 读取到EOF（文件结束），退出循环
                break
            f_out.write(buf)  # 写入目标文件
    print(f"✓ 二进制文件复制完成（目标文件：{copy_file}）")
    print(f"原文件数据：{list(binary_data)}")
    with open(copy_file, "rb") as f_check:
        print(f"复制后数据：{list(f_check.read())}")

    # ===================== 5. 其他常用模式与方法 =====================
    print("\n" + "="*50)
    print("5. 其他常用模式与方法")
    print("="*50)

    # a+模式：追加+读取（指针默认在文件末尾）
    with open(text_file, "a+", encoding="utf-8") as f:
        f.write("第七行：a+模式追加（指针在末尾）\n")
        f.seek(0)  # 移动指针到开头才能读取
        last_line = f.readlines()[-1]
        print(f"✓ a+模式追加后最后一行：{last_line.strip()}")

    # 指针操作：tell() + seek()
    with open(text_file, "r", encoding="utf-8") as f:
        print(f"✓ 初始指针位置：{f.tell()}")
        f.seek(10)  # 移动到第10字节位置
        print(f"移动到第10字节后，读取内容：{f.read(5)}")  # 从第10字节开始读5个字符
        print(f"当前指针位置：{f.tell()}")

    # ===================== 6. 文件属性与清理 =====================
    print("\n" + "="*50)
    print("6. 文件属性与清理")
    print("="*50)
    print(f"文本文件是否存在：{text_file.exists()}")
    print(f"文本文件大小：{os.path.getsize(text_file)}字节")
    print(f"二进制文件是否为文件：{binary_file.is_file()}")

    # 清理生成的文件（可选，注释后可保留文件查看结果）
    import shutil
    shutil.rmtree(data_dir)
    print(f"✓ 清理完成：删除目录 {data_dir}")

if __name__ == "__main__":
    demo_file_operations()