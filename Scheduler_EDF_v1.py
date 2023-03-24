import math
import sys
import Task

# Test Tasks
t1 = Task.Task(1, 3, 2, 6)
t2 = Task.Task(2, 3, 1, 10)
t3 = Task.Task(3, 2, 1, 15)
list1 = [t1, t2, t3]


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
    final_output = []

    def __init__(self, list, max_frequency):
        self.m_freq = max_frequency # Input frequency
        self.TBS_Tasks = list
        self.hyper_period()
        print(self.task_util())
        self.sch()
        
    def task_util(self):
        t_util = 0  # initialize utilization to zero
        for i in range(0, len(self.TBS_Tasks)):  # add utilization of all tasks
            if self.TBS_Tasks[i].has_run:  # if task has run add it's actual time
                t_util += (self.TBS_Tasks[i].e_act / self.TBS_Tasks[i].period)
                #print(t_util)
            else:  # else add its worst case
                t_util += (self.TBS_Tasks[i].e_wor / self.TBS_Tasks[i].period)
                #print(t_util)
        return t_util
        
    def hyper_period(self):  # Calculate hyper period based on task periods
        lcm = 1
        for i in range(0, len(self.TBS_Tasks)):
            self.P_Tasks.append(self.TBS_Tasks[i].period)
        for i in self.P_Tasks:
            lcm = lcm * i // math.gcd(lcm, i)
        self.hyp_per = lcm
        
    def get_release_times (self):
        for i in range (len(self.TBS_Tasks)):
            interim_release_times = []
            for j in range(0, self.hyp_per, self.TBS_Tasks[i].period):
                interim_release_times.append(j)
                if j not in self.release_times_all:
                    self.release_times_all.append(j)
            self.release_times_task.append(interim_release_times)
        self.release_times_all.sort()
        #print(self.release_times_all)
        #print(self.release_times_task)

                     
    def update_queue(self, current_run):
        print("DEADLINES")
        print(self.deadlines)
        # for i in range (len(self.deadlines)):
        #     if self.deadlines[i] == 0 :
        #         for task in self.TBS_Tasks:                                     
        #             if task.id == i+1:
        #                 self.queue.remove(task)
        #                 self.queue_ID.remove(task.id)
        #                 self.TBS_Task[task.id - 1].has_run = True
                        
        for task in self.TBS_Tasks:
            if task.t_left == 0 :
                self.queue.remove(task)
                self.queue_ID.remove(task.id)
                self.TBS_Tasks[task.id - 1].has_run = True
                self.TBS_Tasks[task.id - 1].t_left = -1
                self.deadlines[task.id - 1] = -1
        
        if current_run in self.release_times_all:                                        
            for task_number, release_time in enumerate(self.release_times_task):          
                if current_run in release_time:                                     
                    for task in self.TBS_Tasks:                                     
                        if task.id == task_number+1:
                            if task in self.queue:                                  
                                print("Missed Deadline")
                                self.queue = [-1]              
                                sys.exit()                                                
                            print ("Adding to queue " + str(task.id))
                            self.queue.append(task)
                            self.queue_ID.append(task.id)
                            self.deadlines[task.id-1] = current_run + task.period
                            self.TBS_Tasks[task.id - 1].has_run = False
                            self.TBS_Tasks[task.id - 1].t_left = self.TBS_Tasks[task.id - 1].e_act
        

                        
    def next_task_edf(self):
        try:
            earliest_deadline = min(x for x in self.deadlines if x > 0)
                        
            for i, deadline in enumerate(self.deadlines):
                if deadline == earliest_deadline:
                    next_task_id = i+1
                    print("NEXT TASK " + str(next_task_id))
            
            for task in self.TBS_Tasks:                                  
                if task.id == next_task_id:
                        next_task = task
        except:
            next_task = None
                    
        return next_task

    def sch(self):
        
        task_start = 0
        next_task = None
        current_task = None 
        current_run = 0
        
        # Initial deadlines
        for task in self.TBS_Tasks:
            self.deadlines.append(-1)
        
        self.get_release_times()
        
        #Main while loop 
        while (current_run <= self.hyp_per):
            print()
            print("OUTPUT")
            print(self.final_output)
            self.update_queue(current_run)
            next_task = self.next_task_edf()
           
            if next_task != current_task:
               if current_task is not None:

                    interim_task_info = []
                    interim_task_info.append(current_task.id)
                    interim_task_info.append(task_start)
                    interim_task_info.append(current_run)
                    self.final_output.append(interim_task_info)
                    
                    task_start = current_run
                    current_task = next_task
               else:
                    print ("else")
                    task_start = current_run
                    current_task = next_task
            
            
            
            if current_task is not None:          
                self.TBS_Tasks[current_task.id - 1].t_left -=1   
                self.deadlines = [x-1 for x in self.deadlines] 
            
            current_run += 1 
             
               


a = Scheduler(list1, 1)