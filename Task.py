class Task:
    def __init__(self, id, worst, actual, period_in):  # Task input constructor
        self.id = id 
        self.e_wor = float(worst)
        self.e_act = float(actual)
        self.period = period_in # Implement comparator
        self.t_left = float(self.e_act) # way to figure out if task has run this period
        self.has_run = False
        self.deadline = period_in
        self.task_start = float(0.0)
        self.task_util = float(1.0)
        self.pre = False

    def __lt__(self, other):
        return self.deadline < other.deadline

    def reset(self):
        self.deadline = self.period
        self.t_left = self.e_act
        self.has_run = False
        self.pre = False