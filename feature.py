import random
import numpy as np


class Link:

    def __init__(self, source, to):
        self.w = random.random()
        self.b = random.random()
        self.source = source
        self.to = to

    def propagate_feature_value(self, value):
        self.source.propagate_feature_value(value)

    def forward_feature_value(self, value):
        self.to.forward_feature_value(
            self.w * value + self.b
        )


class Cell:

    def __init__(self, name, observer, is_target):
        self.name = name
        self.value = 0
        self.target_value = 0
        self.real = None
        self.observer = observer
        self.inputFrom = []
        self.outputTo = []
        self.is_target = is_target

    def forward(self):
        print(self.name, "active", self.value)
        # 传播到下一层
        for o in self.outputTo:
            o.forward_feature_value(
                np.tanh(self.value)
            )
        return self

    def propagate(self):
        self.value = 0
        print(self.name, "propagate", self.value)
        for i in self.inputFrom:
            i.propagate_feature_value(self.value)

    def forward_feature_value(self, value):
        self.value += value
        if self.is_target:
            self.target_value += value
        else:
            self.observer.push_active(self)
            self.observer.push_feature(self)
        return self

    def propagate_feature_value(self, value):
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
