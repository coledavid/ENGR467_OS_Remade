class Task:
    def __init__(self, worst, actual, period_in):  # Task input constructor
        self.e_wor = worst
        self.e_act = actual
        self.period = period_in # Implement comparator
        self.t_left = self.e_act # way to figure out if task has run this period
        self.has_run = False
