import math
import numpy as np


x_max = 10
x_min = -10
x_split = 0

y_max = 10
y_min = -10
y_split = 0

train_size = 400
test_size = 100


def generate_train_set():
    # 训练集
    training_set = [
        np.array([1, 1, 'A']),
        np.array([1, 1, 'A']),
        # np.array([1, 1, 'A']),
        # np.array([-1, 1, 'B']),
        # np.array([-1, -1, 'A']),
        # np.array([1, -1, 'B']),
        # np.array([1, 1, 'A']),
        # np.array([-1, 1, 'B']),
        # np.array([-1, -1, 'A']),
        # np.array([1, -1, 'B']),
        # np.array([1, 1, 'A']),
        # np.array([-1, 1, 'B']),
        # np.array([-1, -1, 'A']),
        # np.array([1, -1, 'B']),
        # np.array([1, 1, 'A']),
        # np.array([-1, 1, 'B']),
        # np.array([-1, -1, 'A']),
        # np.array([1, -1, 'B']),
        # np.array([1, 1, 'A']),
        # np.array([-1, 1, 'B']),
        # np.array([-1, -1, 'A']),
        # np.array([1, -1, 'B']),
        # np.array([1, 1, 'A']),
        # np.array([-1, 1, 'B']),
        # np.array([-1, -1, 'A']),
        # np.array([1, -1, 'B']),
    ]
    # training_set = [
    #     np.array([1, 1, 'A']),
    #     np.array([2, 10, 'A']),
    #     np.array([10, 2, 'A']),
    #     np.array([-1, -1, 'A']),
    #     np.array([-2, -10, 'A']),
    #     np.array([-10, -2, 'A']),
    #     np.array([-1, 1, 'B']),
    #     np.array([-2, 10, 'B']),
    #     np.array([-10, 2, 'B']),
    #     np.array([1, -1, 'B']),
    #     np.array([2, -10, 'B']),
    #     np.array([10, -2, 'B'])]
    return training_set


def generate_test_set():
    # 训练集
    test_set = []
    node_total_x = np.random.rand(test_size) * (x_max - x_min) - (x_split - x_min)
    node_total_y = np.random.rand(test_size) * (y_max - y_min) - (y_split - y_min)
    # 构造训练集
    for i in range(0, test_size):
        if node_total_x[i] * node_total_y[i] > 0:
            tag = "A"
        else:
            tag = "B"
        test_set.append(np.array([node_total_x[i], node_total_y[i], tag]))

    return test_set


def generate_standard_split_line_set():
    lines = [
        np.array([[x_min, y_split], [x_max, y_split]]),
        np.array([[x_split, y_min], [x_split, y_max]])
    ]
    return lines
