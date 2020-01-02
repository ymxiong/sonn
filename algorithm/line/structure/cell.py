import random
import numpy as np

adjust_rate = 0.1


class Cell:

    def __init__(self, name, observer, a, b):
        self.name = name
        self.observer = observer
        self.a = a
        self.b = b
        self.pre_cell_set = set()
        self.active_value = 0.0
        self.type = 0

    def accumulation(self, value):
        self.active_value += float(value)

    def clear_active_value(self):
        self.active_value = 0.0


class FeatureCell(Cell):

    def __init__(self, name, observer):
        super().__init__(name, observer, None, None)
        self.next_cell_set = set()
        self.w = []
        self.b = []

    def activation(self):
        self.observer.push_active(self)
        return self

    def activation_next(self):
        # 遍历下层细胞集合
        for i, cell in enumerate(self.next_cell_set):
            # 激活
            next_active = self.active_value * self.w[i] + self.b[i]
            cell.accumulation(next_active)
            if cell.type == 0:
                # 累计
                self.observer.push_active(cell)

        for item in self.next_cell_set:
            if item.type == 0:
                self.observer.push_active(item)
        return self

    def adjust_pre(self, value):
        for item in self.pre_cell_set:
            print(self.name, "adjust_pre:", self.name, "->", item.name, value)
        return self

    def link(self, target):
        self.next_cell_set.add(target)
        self.w.append(np.random.rand())
        self.b.append(np.random.rand())
        target.pre_cell_set.add(self)


class TargetCell(Cell):

    def __init__(self, name, observer):
        super().__init__(name, observer, None, None)
        self.target_value = 0
        self.type = 1

    def activation(self, value):
        self.target_value = value
        self.observer.push_target(self)
        return self

    def activation_next(self):
        pass

    def adjust(self):
        adjust_value = self.target_value - self.active_value
        print(self.name, "loss:", adjust_value)
        if len(self.pre_cell_set) == 0:
            self.observer.link(self)
        else:
            for item in self.pre_cell_set:
                # print("adjust item:", item)
                item.adjust_pre(adjust_value)
