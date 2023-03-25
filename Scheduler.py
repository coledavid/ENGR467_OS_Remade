"""
import math
# import pandas as pd
import Task

# Test Tasks
t1 = Task.Task( 2, 1, 4)
t2 = Task.Task( 1, 2, 10)
t3 = Task.Task( 2, 1, 5)
list1 = [t1, t2, t3]


# Class to schedule task including all functions related to calculations
class Scheduler:
    TBS_Tasks = []
    P_Tasks = []
    m_freq = 1  # REMIND USER TO ENTER AS DECIMAL NOT PERCENTAGE
    hyp_per = 0

    def __init__(self, list, max_frequency):
        self.m_freq = max_frequency # Input frequency
        self.TBS_Tasks = list

        print(self.TBS_Tasks)
        self.hyper_period()
        print(self.task_util())
        print(self.ps_select(self.task_util()))
        self.task_sched()

    def hyper_period(self):  # Calculate hyper period based on task periods
        lcm = 1

        for i in range(0, len(self.TBS_Tasks)):
            self.P_Tasks.append(self.TBS_Tasks[i].period)

        for i in self.P_Tasks:
            lcm = lcm * i // math.gcd(lcm, i)
        self.hyp_per = lcm

    def task_util(self):
        t_util = 0  # initialize utilization to zero
        for i in range(0, len(self.TBS_Tasks)):  # add utilization of all tasks
            if self.TBS_Tasks[i].has_run:  # if task has run add it's actual time
                t_util += (self.TBS_Tasks[i].e_act / self.TBS_Tasks[i].period)
                print("UTIL: ",i,t_util)
            else:  # else add its worst case
                t_util += (self.TBS_Tasks[i].e_wor / self.TBS_Tasks[i].period)
                print("UTIL: ",i,t_util)
        return t_util


        
    #def next_task(self,time):
    
    def sch(self):
        # Find the minimum period of all tasks
        min_period = min(task.period for task in tasks)

        # Find all tasks that have the minimum period
        tasks_with_min_period = [task for task in tasks if task.period == min_period]

        # Print the task IDs and period
        print(f"The tasks with the lowest period ({min_period}) are:")
        for task in tasks_with_min_period:
            print(f"Task {task.id}")

    def task_sched(self):
        current_run = 0
        task_release_list = []
        all_release_times = []
        for i in range (len(self.TBS_Tasks)):
            interim_release_times = []
            for i in range(0, self.hyp_per, self.TBS_Tasks[i].period):
                interim_release_times.append(i)
                if i not in all_release_times:
                    all_release_times.append(i)
            
            task_release_list.append(interim_release_times)
            
        #print (task_release_list)
        #print (all_release_times)
        
        #exec(f'task_{i}_release = interim_release_times')
            
                
        
        # While(current_run <= self.hyp_per)
        
        
        # Sort tasks in order of ascending period
        # Schedule in order of list using ps_select(task_util(self))
        # When task has run i.e t_left (task variable) = 0 set has_run of that task to zero
        # To check whether a task has been released again initialize a separate
        # list of periods (only for has_run tasks) and take the modulus
        # current run time % task period. If this operation is zero the task is
        # re-released into the list of TBS_tasks and must be resorted.
        # create list(s) of completed tasks and their pstates.
        # output whether the tasks were feasibly scheduled.
        
        
        
        return -1


print("Start")
a = Scheduler(list1, 1)

        """
        

        
import math
import sys
# import pandas as pd
import Task

# Test Tasks
t1 = Task.Task(1, 3, 1, 6)
t2 = Task.Task(2, 3, 1, 10)
t3 = Task.Task(3, 2, 1, 15)
list1 = [t1, t2, t3]


# Class to schedule task including all functions related to calculations
class Scheduler:
    TBS_Tasks = []
    P_Tasks = []
    m_freq = 1  # REMIND USER TO ENTER AS DECIMAL NOT PERCENTAGE
    hyp_per = 0

    def __init__(self, list, max_frequency):
        self.m_freq = max_frequency # Input frequency
        self.TBS_Tasks = list

        #print(self.TBS_Tasks)
        self.hyper_period()
        #print(self.task_util())
        #print(self.ps_select(self.task_util()))
        self.sch()
        

    def hyper_period(self):  # Calculate hyper period based on task periods
        lcm = 1

        for i in range(0, len(self.TBS_Tasks)):
            self.P_Tasks.append(self.TBS_Tasks[i].period)

        for i in self.P_Tasks:
            lcm = lcm * i // math.gcd(lcm, i)
        self.hyp_per = lcm

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

    def sch(self):
        task_start = 0
        final_task_list = []
        next_task = None
        current_task = None 
        current_run = 0
        # Find the minimum period of all tasks
        min_period = min(task.period for task in self.TBS_Tasks)
        # Find all tasks that have the minimum period
        tasks_with_min_period = [task for task in self.TBS_Tasks if task.period == min_period]

        task_release_list = []
        all_release_times = []
        deadlines = []
        
        #Getting all the release times
        for i in range (len(self.TBS_Tasks)):
            interim_release_times = []
            for i in range(0, self.hyp_per, self.TBS_Tasks[i].period):
                interim_release_times.append(i)
                if i not in all_release_times:
                    all_release_times.append(i)
            
            task_release_list.append(interim_release_times)
        
        #current_task = tasks_with_min_period[0]
        task_queue = []
        task_queue_ID = []
        
        for task in self.TBS_Tasks:
            deadlines.append(-1)
        
        #Main while loop 
        while (current_run <= self.hyp_per):
            print ("current" + str(current_run))
            print (final_task_list)

            if current_task is not None:
                print ("current task = " + str(current_task.id))
            # MAKING THE QUEUE - INITIAL WORKING
            if current_run in all_release_times:                                        # If current time is in release times
                for task_number, release_time in enumerate(task_release_list):          # Iterate through the 2d list of the release times for each task

                    if current_run in release_time:                                     # If there is a match
                        for task in self.TBS_Tasks:                                     # Add the particular task to the queue
                            if task.id == task_number+1:
                                if task in task_queue:                                  # If task is already in the queue, AKA missed deadline
                                    print ("Missed deadline")
                                    print (final_task_list)
                                    sys.exit()                                                # Stop program
                                print ("appending " + str(task.id))
                                task_queue.append(task)
                                task_queue_ID.append(task.id)
                                deadlines[task.id-1] = current_run + task.period
                            
            
            
            
            
            # Selecting next task
            print ("deadlines")
            print (deadlines)
 
            earliest_deadline = min(x for x in deadlines if x > 0)
                    

            for i, val in enumerate(deadlines):
                if val == earliest_deadline:
                    next_task_id = i+1
                    print("NEXT TASK " + str(next_task_id))
            
            for task in self.TBS_Tasks:                                  
                if task.id == next_task_id:
                        next_task = task
            
            #print("NIndex " + str(next_task))
            #print("CIndex " + str(current_task))
            
            # Switching task + adding to final list
            if next_task != current_task:
                temp_task_info = []

                if current_task is not None:

                    temp_task_info.append(current_task.id)
                    temp_task_info.append(task_start)
                    temp_task_info.append(current_run)
                    temp_task_info.append("A")
                    task_start = current_run
                    current_task.t_left -= 1
                    print ('time left' + str(current_task.t_left))
                    if current_task.t_left == 0:
                        task_queue.remove(current_task)
                        task_queue_ID.remove(current_task.id)
                        deadlines[current_task.id -1] = -1
                    
                    final_task_list.append(temp_task_info)
                    current_task = next_task
                
                else:
                    current_task = next_task
                    current_task.t_left -=1
                    if current_task.t_left == 0:
                        task_queue.remove(current_task)
                        task_queue_ID.remove(current_task.id)
                        deadlines[current_task.id -1] = -1
                        if current_task is not None:
                            temp_task_info.append(current_task.id)
                            temp_task_info.append(task_start)
                            temp_task_info.append(current_run)
                            temp_task_info.append("B")
                            final_task_list.append(temp_task_info)
        
                            task_start = current_run
                    
            else:
                current_task.t_left -= 1
                if current_task.t_left == 0:
                    task_queue.remove(current_task)
                    task_queue_ID.remove(current_task.id)
                    temp_task_info = []
                    deadlines[current_task.id -1] = -1
                    if current_task is not None:
                        temp_task_info.append(current_task.id)
                        temp_task_info.append(task_start)
                        temp_task_info.append(current_run)
                        temp_task_info.append("C")
                        final_task_list.append(temp_task_info)
                        task_start = current_run
                            
            '''
            
            task_info.append[current_task.id, current_run, current_run+current_task.period]
            current_run = current_run + current_task.period
            for task in task_queue:
                if task.id == current_task.id:
                    if task.actual > 0:
                        task.actual -=1
                    else:
                        task_queue.remove(current_task)
'''
            print (task_queue_ID)
            print ()
            deadlines = [x-1 for x in deadlines]                
            current_run += 1
            
                
                
                   
                
                
            
            
        



        #for task in tasks_with_min_period:
        #   print(task.id)
        
        
    
    def task_sched(self):
        # While(current_run <= self.hyp_per)
        # Sort tasks in order of ascending period
        # Schedule in order of list using ps_select(task_util(self))
        # When task has run i.e t_left (task variable) = 0 set has_run of that task to zero
        # To check whether a task has been released again initialize a separate
        # list of periods (only for has_run tasks) and take the modulus
        # current run time % task period. If this operation is zero the task is
        # re-released into the list of TBS_tasks and must be resorted.
        # create list(s) of completed tasks and their pstates.
        # output whether the tasks were feasibly scheduled.
        return -1


a = Scheduler(list1, 1)