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


class TargetObserver:
    def __init__(self):
        self.memory = set()

    def push(self, target):
        self.memory.add(target)

    def clean(self):
        self.memory.clear()


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

    def print(self):
        print("----->Print")
        print("f:", end='')
        for f in self.feature.memory:
            print(f.name, end=' ')
        print()

        print("a:", end='')
        for f in self.active_cell_set:
            print(f.name, end=' ')
        print()

        print("t:", end='')
        for f in self.target.memory:
            print(f.name, end=' ')
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
        self.target.push(cell)

    def activation(self):
        for f in self.feature.memory:
            f.forward_feature_value(1)
        for t in self.target.memory:
            t.set_target_value(1)
        self.forward()
        self.propagate()
        self.target.memory.clear()

    def forward(self):
        # 打印观察者状态
        self.print()
        print("----->Print activation:")
        # 遍历并激活激活队列中的元素
        while len(self.active_cell_queue) > 0:
            # 将激活细胞推进特征队列
            self.push_feature(self.pop_active().forward())

        print("----->End activation:")
        self.print()

    def propagate(self):
        print("----->Print propagate:")
        # 查看目标队列中的细胞是否激活
        for m in self.target.memory:
            # 若没有激活则构建关系
            if m.value == 0:
                self.build(m)
            # 调整目标
            self.push_active(m)
        while len(self.active_cell_queue) > 0:
            self.pop_active().propagate()
        print("----->End propagate:")
        self.print()

    def build(self, target):
        cell = Cell("HiddenCell_" + str(self.hidden_num), self, False)
        print("build HiddenCell_" + str(self.hidden_num))
        self.hidden_num += 1
        for f in self.feature.memory:
            f.output_to(cell)
        cell.output_to(target)
        self.push_feature(cell)

