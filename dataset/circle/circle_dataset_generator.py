import math
import numpy as np

# 生成最大圈数
circle = 5
# 训练集圈数
draw_circle = 3
# 比例尺
scale = 0.01
# 最大绘制角度
cita = circle * 360
# 训练集最大绘制角度
draw_cita = draw_circle * 360
# 最大生成半径
r_max = scale * cita
# 测试集点数
test_node_num = 5000


def generate_train_set():
    # 训练集
    training_set = []

    # 构造训练集
    for alpha in range(0, draw_cita, 10):
        r = alpha * scale
        beta = alpha + 180

        x_alpha = r * math.cos(alpha / 180.0 * math.pi)
        y_alpha = r * math.sin(alpha / 180.0 * math.pi)
        training_set.append(np.array([x_alpha, y_alpha, 'A']))

        x_beta = r * math.cos(beta / 180.0 * math.pi)
        y_beta = r * math.sin(beta / 180.0 * math.pi)
        training_set.append(np.array([x_beta, y_beta, 'B']))
    return training_set


def generate_test_set():
    # 初始化训练集
    test_set = []
    node_total = 2 * r_max * np.random.rand(test_node_num, 2) - r_max
    for node_i in range(0, test_node_num):
        node_x = node_total[node_i][0]
        node_y = node_total[node_i][1]
        node_r = math.pow(math.pow(node_x, 2) + math.pow(node_y, 2), 0.5)
        node_cita = math.atan(node_y / node_x)
        if node_x < 0:
            node_cita += math.pi

        node_type = 'A'
        for i in range(0, 2 * circle):
            if ((node_cita / (2 * math.pi) * 360) - 90 + 360 * i) * scale > node_r > (
                    (node_cita / (2 * math.pi) * 360) - 270 + 360 * i) * scale:
                node_type = 'B'
        test_set.append(np.array([node_x, node_y, node_type]))
    return test_set


def generate_standard_split_line_set():
    line_up = []
    line_down = []
    # 构造训练集
    for alpha in range(0, cita, 10):
        r = alpha * scale
        beta = alpha + 180
        # 构造分界线
        m_alpha = alpha + 90
        m_beta = beta + 90
        x_m_alpha = r * math.cos(m_alpha / 180.0 * math.pi)
        y_m_alpha = r * math.sin(m_alpha / 180.0 * math.pi)
        x_m_beta = r * math.cos(m_beta / 180.0 * math.pi)
        y_m_beta = r * math.sin(m_beta / 180.0 * math.pi)
        line_up.append([x_m_alpha, y_m_alpha])
        line_down.append([x_m_beta, y_m_beta])
    # 绘制分割线
    line_down.reverse()
    line_down.extend(line_up)
    line = np.array(line_down)
    return line
