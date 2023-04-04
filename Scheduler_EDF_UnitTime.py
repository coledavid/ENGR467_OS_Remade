import math
import sys

from matplotlib import pyplot as plt

import Task

# Test Tasks
t1 = Task.Task(1, 3.0, 1.0, 10)
t2 = Task.Task(2, 4.0, 2.0, 15)
t3 = Task.Task(3, 3.0, 1.0, 5)
t4 = Task.Task(4, 6.0, 5.0, 30)
list1 = [t1, t2, t3, t4]


# pstate_in = [1, 0.8, .6, .5, .4]


# Class to schedule task including all functions related to calculations
class Scheduler:
    TBS_Tasks = []
    P_Tasks = []
    hyp_per = 0
    deadlines = []
    final_output = []  # Output list
    current_run = 0
    ps_recalc = -1
    pstate_in = []
    error = ""

    # task_start = 0

    def __init__(self, list, p_states):
        self.pstate_in = p_states  # Input frequency
        self.TBS_Tasks = list
        self.P_Tasks = []
        self.hyp_per = 0
        self.deadlines = []
        self.final_output = []
        self.current_run = 0
        self.ps_recalc = -1
        self.error = ""
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
        if len(self.pstate_in) < 5:
            for i in range(0, 4):
                self.pstate_in.append(self.pstate_in[len(self.pstate_in) - 1])
        if utilisation > self.pstate_in[0]:
            print("Worst case under-scheduled")
            return self.pstate_in[0]
        elif utilisation > self.pstate_in[1]:
            return self.pstate_in[0]
        elif utilisation > self.pstate_in[2]:
            return self.pstate_in[1]
        elif utilisation > self.pstate_in[3]:
            return self.pstate_in[2]
        elif utilisation > self.pstate_in[4]:
            return self.pstate_in[3]
        else:
            return self.pstate_in[0]

    def ps_update(self):
        if self.deadlines[0] == 0:
            self.ps_recalc = 1
        else:
            self.ps_recalc = -1

    def hyper_period(self):  # Calculate hyper period based on task periods
        lcm = 1
        for i in range(0, len(self.TBS_Tasks)):
            self.P_Tasks.append(int(self.TBS_Tasks[i].period))
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
                self.error = f"Underscheduled by Task {self.deadlines[i].id} at time unit {self.current_run}"
                ## self.final_output = error_msg
                print(self.final_output)
                ## sys.exit(error_msg)  # Missed deadline
                # quit()
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
            # ps_tmp = f"P-State is {self.deadlines[current_task].task_util}"
            ps_tmp = {self.deadlines[current_task].task_util}
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
            # ps_tmp = f"P-State is {self.deadlines[current_task].task_util}"
            ps_tmp = {self.deadlines[current_task].task_util}
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
            # print(self.deadlines[current_task].t_left, " Util ", self.deadlines[current_task].task_util)
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

    def adjust_final_output_for_preemption(self, final_output):
        adjusted_output = []

        for task_output in final_output:
            task_id, start_time, end_time, p_state = task_output
            segments = [(start_time, end_time)]

            for prev_task_output in adjusted_output:
                prev_task_id, prev_start_time, prev_end_time, prev_p_state = prev_task_output
                new_segments = []

                for seg_start, seg_end in segments:
                    if prev_start_time < seg_end and prev_end_time > seg_start:
                        if seg_start < prev_start_time:
                            new_segments.append((seg_start, prev_start_time))
                        if seg_end > prev_end_time:
                            new_segments.append((prev_end_time, seg_end))
                    else:
                        new_segments.append((seg_start, seg_end))

                segments = new_segments

            for seg_start, seg_end in segments:
                adjusted_output.append([task_id, seg_start, seg_end, p_state])

        return adjusted_output

    def plot_output(self):
        task_ids = list(set([task_output[0] for task_output in self.final_output]))
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        task_colors = {task_id: colors[i % len(colors)] for i, task_id in enumerate(task_ids)}
        ##New Line added###
        p_state_display = {}

        num_tasks = len(task_ids)
        fig, axes = plt.subplots(nrows=num_tasks, sharex=True, sharey=True)
        fig.subplots_adjust(hspace=0.5)
        fig.suptitle("Cycle Conserving EDF Scheduling")

        for task_id in task_ids:
            task_outputs = [task_output for task_output in self.final_output if task_output[0] == task_id]
            ##New line added##
            p_state_per_task = []
            for task_output in task_outputs:
                start_time = task_output[1]
                end_time = task_output[2]
                p_state = float(list(task_output[3])[0])
                ##New line added
                p_state_per_task.append(p_state)
                p_state_display[task_id] = p_state_per_task

                color = task_colors[task_id]
                bar_height = p_state
                axes[task_id - 1].barh(0, end_time - start_time, left=start_time, height=bar_height, color=color, align='edge')

                axes[task_id - 1].set_ylim(0, 1)
        ##New for loop##
        for i, ax in enumerate(axes):
            task_id = i + 1
            p_state = p_state_display[task_id]
            ax.set_ylabel(f"Task {task_id}")
            ax_right = ax.twinx()
            ax_right.set_ylabel(f"P-state")
            ax_right.yaxis.set_label_position("right")
            ax_right.yaxis.tick_right()
            ax_right.set_ylim(ax.get_ylim())

        ###New line added###
        p_state_str = '\n'.join([f'Task {k}: {v}' for k, v in p_state_display.items()])
        axes[-1].set_xlabel(f"Time and P-state\n {p_state_str} ")
        fig.subplots_adjust(bottom=0.2)
        axes[-1].set_xlabel(f"Time, \nP-state is {p_state_display}")
        plt.xlim(0, self.hyp_per)
        plt.show()

# a = Scheduler(list1, [1, 0.8, .6, .5, .4])
# a.final_output = a.adjust_final_output_for_preemption(a.final_output)
# a.plot_output()
