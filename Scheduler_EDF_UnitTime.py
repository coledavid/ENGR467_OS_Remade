import math
import sys
import Task

# Test Tasks
t1 = Task.Task(1, 2, 1, 6)
t2 = Task.Task(2, 2, 1, 10)
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
    final_output = [] # Output list

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
    
    def ps_select(self, utilisation):
        utilisation = utilisation * 100
        p_state = []  # list to declare p_states: Item 1 represents name of state, Item 2 represents frequency of
        # operation
        if self.m_freq != 1:
            p_state.append("Custom Frequency")
            p_state.append(self.m_freq * 100)
        elif utilisation > 100:
            p_state.append("Underscheduled, utilisation too high")
            p_state.append(100)
            return p_state
        elif utilisation > 80:
            p_state.append("P0")
            p_state.append(100)
            return p_state
        elif utilisation > 60:
            p_state.append("P1")
            p_state.append(80)
            return p_state
        elif utilisation > 40:
            p_state.append("P2")
            p_state.append(60)
            return p_state
        elif utilisation > 20:
            p_state.append("P3")
            p_state.append(40)
            return p_state
        elif utilisation > 0:
            p_state.append("P4")
            p_state.append(20)
            return p_state
        else:
            p_state.append("Error in task input")
            p_state.append(20)
            return p_state
  
    def hyper_period(self):  # Calculate hyper period based on task periods
        lcm = 1
        for i in range(0, len(self.TBS_Tasks)):
            self.P_Tasks.append(self.TBS_Tasks[i].period)
        for i in self.P_Tasks:
            lcm = lcm * i // math.gcd(lcm, i)
        self.hyp_per = lcm
        
    # Function to get all release times
    # release_times_all : [list of all unique release times]
    # release_times_task: [[list], [of], [release], [times], [by], [task]]
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
                        
        # To remove task if no time left
        # Sets has run to True + t_left + deadline to -1
        for task in self.TBS_Tasks:
            if task.t_left == 0 :
                self.queue.remove(task)
                self.queue_ID.remove(task.id)
                self.TBS_Tasks[task.id - 1].has_run = True
                self.TBS_Tasks[task.id - 1].t_left = -1
                self.deadlines[task.id - 1] = -1
        
        # Based on current time, adds task to queue and resets params 
        
        # Check if current run has any releases
        if current_run in self.release_times_all:
            #Findinf which tasks are released at this time                                        
            for task_number, release_time in enumerate(self.release_times_task):          
                if current_run in release_time:                                     
                    for task in self.TBS_Tasks:                                     
                        if task.id == task_number+1:
                            # If task is added to queue twice, it means a deadline is missed
                            if task in self.queue:                                  
                                print("Missed Deadline")
                                self.queue = [-1]              
                                sys.exit()
                                                                                
                            print ("Adding to queue " + str(task.id))
                            self.queue.append(task)                                                 #   Queue of tasks
                            self.queue_ID.append(task.id)                                           #   Queue of task IDs
                            self.deadlines[task.id-1] = current_run + task.period                   #   Setting deadlines
                            self.TBS_Tasks[task.id - 1].has_run = False                         
                            self.TBS_Tasks[task.id - 1].t_left = self.TBS_Tasks[task.id - 1].e_act
        

    # Retuns the next task to be run 
    # Retuns None if there is no other task to be run in queue                 
    def next_task_edf(self):
        try:
            # Get the minimum deadline greater than 0
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

    # Main scheduler
    def sch(self):
    
        task_start = 0 # To keep track of task starting times
        next_task = None
        current_task = None 
        current_run = 0
        
        # Initial deadlines list
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
           
            # If current task is not the same as next task
            if next_task != current_task:
               if current_task is not None:

                    # Add all the details to output list
                    interim_task_info = []
                    interim_task_info.append(current_task.id)
                    interim_task_info.append(task_start)
                    interim_task_info.append(current_run)
                    self.final_output.append(interim_task_info)
                    
                    # Set next task as current task and set current time as task start time
                    task_start = current_run
                    current_task = next_task
               else:
                   # IF there was no task running currently 
                   # There is no info to append to the final output
                    print ("else")
                    task_start = current_run
                    current_task = next_task
            
            
            # Decrementing t left and deadlines
            if current_task is not None:          
                self.TBS_Tasks[current_task.id - 1].t_left -=1   
                self.deadlines = [x-1 for x in self.deadlines] 
            
            # Step
            current_run += 1 
             
a = Scheduler(list1, 1)