import time
from feature import *


class FeatureObserver:
    def __init__(self):
        self.memory = set()

    def push(self, feature):
        self.memory.add(feature)

    def clean(self):
        self.memory.clear()

    def group_feature(self):
        for i in range(0, len(self.memory)):
            print(i)

    def set_zero(self):
        for item in self.memory:
            item.value = 0.0
            item.real = 0.0


class TargetObserver:
    def __init__(self):
        self.memory = set()

    def push(self, target):
        self.memory.add(target)

    def clean(self):
        self.set_zero()
        self.memory.clear()

    def set_zero(self):
        for item in self.memory:
            item.value = 0.0
            item.real = 0.0


class Observer:

    def __init__(self):
        self.feature = FeatureObserver()
        self.target = TargetObserver()
        self.active_cell_queue = []
        self.active_cell_set = set()
        self.hidden_num = 0

    def clean(self):
        self.feature.clean()
        self.target.clean()

    def set_zero(self):
        self.feature.set_zero()
        self.target.set_zero()

    def print(self):
        print("----->Print")
        print("f:", end='')
        for f in self.feature.memory:
            print(f.name, f.value, end=' ')
        print()

        print("a:", end='')
        for f in self.active_cell_set:
            print(f.name, f.value, end=' ')
        print()

        print("t:", end='')
        for f in self.target.memory:
            print(f.name, f.value, f.real, end=' ')
        print("\n----->Print")

    def push_feature(self, cell):
        self.feature.push(cell)

    def push_active(self, cell):
        active_num = len(self.active_cell_set)
        self.active_cell_set.add(cell)
        if len(self.active_cell_set) != active_num:
            self.active_cell_queue.append(cell)

    def pop_active(self):
        cell = self.active_cell_queue.pop(0)
        self.active_cell_set.remove(cell)
        return cell

    def push_target(self, cell):
        # TODO: 思考不清零保留上次传播结果会产生的现象
        cell.value = 0.0
        self.target.push(cell)

    def activation(self):
        for f in self.feature.memory:
            # TODO:激活值交给外部处理
            f.forward_feature_value(1.0)
        for t in self.target.memory:
            # TODO：目标值交给外部处理
            t.set_target_value(1.0)
        # 前馈
        self.forward()
        # 反馈
        self.propagate()
        # 归零
        self.set_zero()

    def forward(self):
        print("------------BEGIN FORWARD------------")
        # 打印观察者状态
        print("----->Print Before activation:")
        self.print()
        print("----->Print Activation:")
        # 遍历并激活激活队列中的元素
        while len(self.active_cell_queue) > 0:
            # 将激活细胞推进特征队列
            self.push_feature(self.pop_active().forward())

        print("----->End Activation:")
        print("----->Print End Activation:")
        self.print()
        print("-------------END FORWARD-------------")

    def propagate(self):
        print("------------BEGIN PROPAGATE------------")
        print("----->Print Propagate:")
        # 查看目标队列中的细胞是否激活
        for m in self.target.memory:
            # 若没有激活则构建关系
            if m.value == 0:
                self.build(m)
            # 调整目标
            self.push_active(m)
        while len(self.active_cell_queue) > 0:
            self.pop_active().propagate()
        print("----->End Propagate:")
        self.print()
        print("-------------END PROPAGATE-------------")

    def build(self, target):
        cell = Cell("HiddenCell_" + str(self.hidden_num), self, False)
        print("build HiddenCell_" + str(self.hidden_num))
        self.hidden_num += 1
        for f in self.feature.memory:
            f.output_to(cell)
        cell.output_to(target)
        self.push_feature(cell)

