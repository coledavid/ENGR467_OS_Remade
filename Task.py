class Task:
    def __init__(self, id, worst, actual, period_in):  # Task input constructor
        self.id = id 
        self.e_wor = worst
        self.e_act = actual
        self.period = period_in # Implement comparator
        self.t_left = self.e_act # way to figure out if task has run this period
        self.has_run = False
        self.deadline = period_in