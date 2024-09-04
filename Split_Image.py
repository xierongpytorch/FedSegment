import os

# 定义输入和输出文件夹的路径
input_dir = "input"
output_dir = "outputssss"

# 遍历input文件夹中的所有内容
for root, dirs, files in os.walk(input_dir):
    # 遍历找到的每一个目录
    for name in dirs:
        # 构建在output文件夹中对应的目录路径
        dir_path = os.path.join(root, name).replace(input_dir, output_dir)

        # 如果目录不存在，则创建它
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"创建目录: {dir_path}")
        else:
            print(f"目录已存在: {dir_path}")
