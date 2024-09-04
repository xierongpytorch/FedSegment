import Augmentor

# 创建管道
p = Augmentor.Pipeline("target_combined_shan_png")

# 指定对应的真实标签（掩码）文件夹
p.ground_truth("target_new_masks_shan")

# 添加建议的数据增强操作
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)
p.zoom_random(probability=0.5, percentage_area=0.8)
p.random_contrast(probability=0.5, min_factor=0.8, max_factor=1.2)
p.random_brightness(probability=0.5, min_factor=0.8, max_factor=1.2)
p.crop_random(probability=0.7, percentage_area=0.8)
p.random_distortion(probability=0.5, grid_width=4, grid_height=4, magnitude=8)

# 生成增强后的样本
p.sample(300)
