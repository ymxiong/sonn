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
        self.active_value = 0
        self.type = 0


class FeatureCell(Cell):

    def __init__(self, name, observer):
        super().__init__(name, observer, None, None)
        self.next_cell_set = set()

    def activation(self, value):
        self.active_value = value
        self.observer.push_active(self)
        return self

    def activation_next(self):
        for item in self.next_cell_set:
            if item.type == 0:
                # print("activation_next:", self.name, "->", item.name)
                self.observer.push_active(item)

        return self

    def adjust_pre(self, value):
        for item in self.pre_cell_set:
            print("adjust_pre:", self.name, "->", item.name, value)
        return self


class TargetCell(Cell):

    def __init__(self, name, observer):
        super().__init__(name, observer, None, None)
        self.target_value = 0
        self.type = 1

    def activation(self, value):
        # print("target:", self.name, "value:", value)
        self.target_value = value
        self.observer.push_target(self)
        return self

    def activation_next(self):
        pass

    def adjust(self):
        adjust_value = self.target_value - self.active_value
        # print("adjust value:", adjust_value)
        if len(self.pre_cell_set) == 0:
            self.observer.link(self)
        else:
            for item in self.pre_cell_set:
                # print("adjust item:", item)
                item.adjust_pre(adjust_value)
