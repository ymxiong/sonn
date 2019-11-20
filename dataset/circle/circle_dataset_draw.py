import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import dataset.circle.circle_dataset_generator as generator

plt.title(u'scatter')

training_set = generator.generate_train_set()
test_set = generator.generate_test_set()
line = generator.generate_standard_split_line_set()

# 绘制训练集
for item in training_set:
    if item[2] == 'A':
        plt.scatter(item[0], item[1], c='dodgerblue', marker='o', alpha=0.8, edgecolors='white')
    if item[2] == 'B':
        plt.scatter(item[0], item[1], c='sandybrown', marker='o', alpha=0.8, edgecolors='white')

# 绘制测试集
for item in test_set:
    if item[2] == 'A':
        plt.scatter(item[0], item[1], marker='v', c='dodgerblue')
    if item[2] == 'B':
        plt.scatter(item[0], item[1], marker='v', c='sandybrown')

# 绘制分割线
plt.plot(line[:, 0], line[:, 1], c='darkred', alpha=0.5)

plt.grid(True)
plt.show()
