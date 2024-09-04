import os
import subprocess

# 定义输入和输出文件夹的路径
input_dir = "input"
output_dir = "outputssss"

# 定义要执行的命令模板
cmd_template = "python scripts/text_editing_SD2.py --prompt '{prompt}' --init_image '{init_image}' --mask '{mask}' --output_path '{output_path}'"

# 定义不同的prompt
prompts = [
    "Substation Secondary Screen Cabinet",
    "Substation Secondary Screen Cabinet with a employee",
    "a employee in substation",
    "electrical equipment in substation",
    "substation"
]

# 遍历input文件夹中的所有子文件夹
for subdir in os.listdir(input_dir):
    subdir_path = os.path.join(input_dir, subdir)
    if os.path.isdir(subdir_path):
        # 对于每个子文件夹，假设jpg和png文件名相同
        for file in os.listdir(subdir_path):
            if file.endswith(".jpg"):
                base_name = os.path.splitext(file)[0]
                init_image = os.path.join(subdir_path, file)
                mask = os.path.join(subdir_path, base_name + ".png")

                # 确保输出文件夹存在
                output_subdir = os.path.join(output_dir, subdir)
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)

                # 对每个prompt执行命令
                for i, prompt in enumerate(prompts, start=1):
                    output_path = os.path.join(output_subdir, f"{i}.jpg")
                    cmd = cmd_template.format(prompt=prompt, init_image=init_image, mask=mask, output_path=output_path)
                    subprocess.run(cmd, shell=True)
