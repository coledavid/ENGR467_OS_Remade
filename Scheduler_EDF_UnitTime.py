import math
import sys
import Task

# Test Tasks
t1 = Task.Task(1, 3.0, 1.0, 10)
t2 = Task.Task(2, 4.0, 2.0, 15)
t3 = Task.Task(3, 3.0, 1.0, 5)
t4 = Task.Task(4, 6.0, 5.0, 30)
list1 = [t1, t2, t3, t4]
pstate_in = [1, 0.8, .6, .5, .4]


# Class to schedule task including all functions related to calculations
class Scheduler:
    TBS_Tasks = []
    P_Tasks = []
    m_freq = 1  # REMIND USER TO ENTER AS DECIMAL NOT PERCENTAGE
    hyp_per = 0
    release_times_all = []
    release_times_task = []
    queue = []
    queue_ID = []
    deadlines = []
    final_output = []  # Output list
    current_run = 0
    ps_recalc = -1

    # task_start = 0

    def __init__(self, list, max_frequency):
        self.m_freq = max_frequency  # Input frequency
        self.TBS_Tasks = list
        self.hyper_period()
        self.sch()

    def task_util(self):
        t_util = 0  # initialize utilization to zero
        for i in range(0, len(self.TBS_Tasks)):  # add utilization of all tasks
            if self.TBS_Tasks[i].has_run:  # if task has run add it's actual time
                t_util += (self.TBS_Tasks[i].e_act / self.TBS_Tasks[i].period)
                # print(t_util)
            else:  # else add its worst case
                t_util += (self.TBS_Tasks[i].e_wor / self.TBS_Tasks[i].period)
                # print(t_util)
        return t_util

    def ps_select(self, utilisation):
        if utilisation > pstate_in[0]:
            print("Worst case under-scheduled")
            return pstate_in[0]
        elif utilisation > pstate_in[1]:
            return pstate_in[0]
        elif utilisation > pstate_in[2]:
            return pstate_in[1]
        elif utilisation > pstate_in[3]:
            return pstate_in[2]
        elif utilisation > pstate_in[4]:
            return pstate_in[3]
        else:
            return pstate_in[4]

    def ps_update(self):
        if self.deadlines[0] == 0:
            self.ps_recalc = 1
        else:
            self.ps_recalc = -1

    def hyper_period(self):  # Calculate hyper period based on task periods
        lcm = 1
        for i in range(0, len(self.TBS_Tasks)):
            self.P_Tasks.append(self.TBS_Tasks[i].period)
        for i in self.P_Tasks:
            lcm = lcm * i // math.gcd(lcm, i)
        self.hyp_per = lcm

    def deadline_init(self):
        self.deadlines = self.TBS_Tasks
        self.deadlines.sort()

    def deadline_update(self):
        for i in range(0, len(self.deadlines)):
            if self.deadlines[i].deadline == 0 and self.deadlines[i].has_run == False:
                print("Underscheduled")
                print(self.deadlines[i].has_run)
                print(self.deadlines[i].deadline)
                print(self.deadlines[i].id)
                print(self.final_output)
                error_msg = f"Underscheduled by Task {self.deadlines[i].id} at time unit {self.current_run}"
                ## self.final_output = error_msg
                print(self.final_output)
                sys.exit(error_msg)  # Missed deadline
            elif self.deadlines[i].deadline == 0 and self.deadlines[i].has_run == True:
                self.deadlines[i].reset()
            self.deadlines[i].deadline -= 1
            # print(self.deadlines[i].deadline) # TROUBLESHOOTING
        self.deadlines.sort()

    def find_cur(self, return_type):
        i = 0
        while i < len(self.deadlines):
            if not self.deadlines[i].has_run:
                if return_type == 1:
                    return self.deadlines[i]
                else:
                    return i
            i += 1
        return None

    def find_next(self, return_type):
        i = 0
        while i < len(self.deadlines):
            if not self.deadlines[i].has_run:
                if i + 1 < len(self.deadlines):
                    if return_type == 1:
                        return self.deadlines[i + 1]
                    else:
                        return i + 1
                else:
                    return None
            i += 1
        return None

    def run_task(self, current_task, task_start, current_run):
        tmp = []
        if self.deadlines[current_task].t_left / self.deadlines[current_task].task_util <= 0.99999:
            # print("RunTask < 1", self.deadlines[current_task].t_left / self.deadlines[current_task].task_util,
            #      " P-state ", self.deadlines[current_task].task_util, " ", self.deadlines[current_task].id,
            #      " current run ", current_run)
            self.deadlines[current_task].has_run = True
            ps_tmp = f"P-State is {self.deadlines[current_task].task_util}"
            tmp = [self.deadlines[current_task].id, self.deadlines[current_task].task_start,
                   current_run + self.deadlines[current_task].t_left / self.deadlines[current_task].task_util - 1,
                   ps_tmp]
            self.final_output.append(tmp)
            if self.find_cur(1) is not None:
                if not self.find_cur(1).pre:
                    self.deadlines[self.find_cur(0)].task_util = self.ps_select(self.task_util())
                    self.deadlines[self.find_cur(0)].task_start = current_run + self.deadlines[current_task].t_left / \
                                                                  self.deadlines[current_task].task_util - 1
            if self.find_cur(1) is not None:
                self.deadlines[self.find_cur(0)].t_left -= float(
                    (1 - (self.deadlines[current_task].t_left / self.deadlines[current_task].task_util)) *
                    self.deadlines[self.find_cur(0)].task_util)
        elif self.deadlines[current_task].t_left / self.deadlines[current_task].task_util == 1:
            # print("RunTask tl == 1", self.deadlines[current_task].t_left / self.deadlines[current_task].task_util,
            #      " P-state ", self.deadlines[current_task].task_util, " ", self.deadlines[current_task].id,
            #      " current run ", current_run)
            self.deadlines[current_task].has_run = True
            ps_tmp = f"P-State is {self.deadlines[current_task].task_util}"
            tmp = [self.deadlines[current_task].id, self.deadlines[current_task].task_start,
                   current_run + self.deadlines[current_task].t_left / self.deadlines[current_task].task_util - 1,
                   ps_tmp]
            self.final_output.append(tmp)
            if self.find_cur(1) is not None:
                if not self.find_cur(1).pre:
                    self.deadlines[self.find_cur(0)].task_util = self.ps_select(self.task_util())
                    self.deadlines[self.find_cur(0)].task_start = current_run + self.deadlines[current_task].t_left / \
                                                                  self.deadlines[current_task].task_util - 1
        else:
            # print("RunTask dec ", self.deadlines[current_task].t_left / self.deadlines[current_task].task_util,
            #      " P-state ", self.deadlines[current_task].task_util, " ", self.deadlines[current_task].id,
            #      " current run ", current_run)

            if self.deadlines[current_task].t_left == self.deadlines[current_task].e_act:
                self.deadlines[self.find_cur(0)].task_start = current_run - 1
            self.deadlines[current_task].t_left -= 1 * float(self.ps_select(self.task_util()))

    def sch(self):
        # self.task_start =0  # To keep track of task starting tim
        self.current_run = 1
        self.deadline_init()
        self.deadline_update()
        current_task = self.deadlines[0]
        self.deadlines[0].task_util = self.ps_select(self.task_util())
        while self.current_run <= self.hyp_per:
            # print("Current run ", current_run)
            # print("Current Deadline ", self.deadlines[0].deadline)
            if self.find_cur(1) is not None and current_task is not None:
                if current_task != self.find_cur(1):
                    current_task.pre = True
            current_task = self.find_cur(1)
            if self.ps_recalc == 1:
                self.deadlines[self.find_cur(0)].task_util = self.ps_select(self.task_util())
                # print(current_task.id, " ", current_task.task_util)
            if current_task is not None:
                self.run_task(self.find_cur(0), current_task.task_start, self.current_run)
            if self.deadlines[0].deadline == 0:
                self.deadlines[0].task_start = self.current_run

            self.deadline_update()
            self.ps_update()
            self.current_run += 1
        print(self.final_output)


a = Scheduler(list1, 1)
