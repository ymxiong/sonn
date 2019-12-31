import algorithm.line.structure.cell as c


class Observer:

    def __init__(self):
        self.target_cell_queue = []
        self.target_cell_set = set()
        self.active_cell_queue = []
        self.active_cell_set = set()
        self.round = 0
        self.cell_num = 100

    def push_active(self, cell):
        active_num = len(self.active_cell_set)
        self.active_cell_set.add(cell)
        if len(self.active_cell_set) != active_num:
            self.active_cell_queue.append(cell)

    def pop_active(self):
        cell = self.active_cell_queue.pop(0)
        return cell

    def push_target(self, cell):
        target_num = len(self.target_cell_set)
        self.target_cell_set.add(cell)
        if len(self.target_cell_set) != target_num:
            self.target_cell_queue.append(cell)

    def pop_target(self):
        cell = self.target_cell_queue.pop(0)
        return cell

    def init(self):
        self.round += 1
        print("============")
        print("<<<<<<<<<<<<Init=Round (", self.round, ")")

    def run(self):
        print("<<<Forward=Round (", self.round, ")")
        # 传播
        self.forward()
        print("<<<Propagate=Round (", self.round, ")")
        # 调整
        self.propagate()
        print("<<<Clean=Round (", self.round, ")")
        # 归零
        self.clean()
        print(">>>>>>>>>>>>End=Round (", self.round, ")")

    def forward(self):
        while len(self.active_cell_queue) > 0:
            cell = self.pop_active()
            print(cell.name + " value:", cell.active_value)
            cell.activation_next()

    def propagate(self):
        while len(self.target_cell_queue) > 0:
            cell = self.pop_target()
            cell.adjust()

    def clean(self):
        self.active_cell_queue.clear()
        self.active_cell_set.clear()
        self.target_cell_set.clear()

    def link(self, target):
        hidden_cell = c.FeatureCell("F" + str(self.cell_num), self)
        hidden_cell.next_cell_set.add(target)
        target.pre_cell_set.add(hidden_cell)
        for item in self.active_cell_set:
            item.next_cell_set.add(hidden_cell)
            hidden_cell.pre_cell_set.add(item)
