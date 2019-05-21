import random
import numpy as np


class Link:

    def __init__(self, source, to):
        self.w = random.random() * 0.5
        self.b = random.random() * 0.5
        self.source = source
        self.to = to

    def propagate_feature_value(self, value):
        self.w += value * self.w
        self.b += value * self.b
        self.source.propagate_feature_value(value)

    def forward_feature_value(self, value):
        self.to.forward_feature_value(
            self.w * value + self.b
        )


class Cell:

    def __init__(self, name, observer, is_target):
        self.name = name
        self.value = 0
        self.real = None
        self.observer = observer
        self.inputFrom = []
        self.outputTo = []
        self.is_target = is_target
        self.memory = []

    def forward(self):
        print(self.name, "active", self.value)
        # 传播到下一层
        self.memory.append(np.tanh(self.value))
        for o in self.outputTo:
            o.forward_feature_value(
                self.memory[-1]
            )
        return self

    def propagate(self):
        value = self.memory.pop()
        if self.is_target:
            print("ADJUST TARGET: " + self.name, self.real, self.value, self.real - self.value)
        else:
            print("ADJUST NORMAL: " + self.name, self.real, self.value, self.real - self.value)
        for i in self.inputFrom:
            i.propagate_feature_value(
                0.5 * (1-np.power(self.real - value, 2))
            )

    def forward_feature_value(self, value):
        self.value += value
        if self.is_target:
            print("IMPORTANT: " + self.name + " ADD " + str(value))
            print("REAL: " + str(self.real))
        else:
            self.observer.push_active(self)
            self.observer.push_feature(self)
        return self

    def propagate_feature_value(self, value):
        self.real = value
        self.observer.push_active(self)
        return self

    def set_target_value(self, real):
        self.real = real
        self.observer.push_target(self)
        return self

    def output_to(self, cell):
        link = Link(self, cell)
        self.outputTo.append(link)
        cell.inputFrom.append(link)


class CellGroup:
    def __init__(self, name, size, observer, is_target):
        self.name = name
        self.feature = []
        for i in range(0, size):
            self.feature.append(Cell(name + 'Cell_' + str(i), observer, is_target))

    def get_at(self, index):
        return self.feature[index]
