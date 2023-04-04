##################################################################################################################
#                                         ENGR 467 GROUP PROJECT                                                 #
##################################################################################################################

# Our group project has made a Cycle Conserving (Premptive) EDF Simulator 
# It has three pages - Start Page, Data Entry, and Results


# Import everything ##############################################################################################

import tkinter as tk            # import tkinter and refer to tkinter as tk in code
from tkinter import *           # import all the functions and built-in modules in the tkinter library
from tkinter import ttk         # Used for styling the GUI
from tkinter import messagebox  # Used for pop up warnings
import numpy as np              # import libaray to use matrix functions

# Global Variables ##############################################################################################
# Task Entry Global Variables

count_T = 1         # Current number of Tasks (for data entry)
flag_T = 0          # flag for removing/adding Tasks 0=add, 1=remove
MAX_NUM_T = 5       # Max of 5 tasks will be accepted in this simulator
MIN_NUM_T = 1       # Min of 1 task is will be accepted in this simulator
Task_output = []   # Initialize the final entry data matrix  


#P-State  Entry Global Variables

count_P = 0         # Current number of Custom P-States
flag_P=0            # flag for removing/adding P-States 0=add, 1=remove
MAX_NUM_P =5        # Max of 5 custom p-states will be allowed in this simulator
MIN_NUM_P=0         # the minimum number of p states allowed (0) becasue three preselcted options cn be selected
Pstate_output =[]   # Initialize the final P-State data array 

# General Formating ##############################################################################################

SMALLERFONT =("Verdana", 8)
SMALLFONT =("Verdana", 10)
MEDIUMFONT =("Verdana", 18)
LARGEFONT =("Verdana", 25)

##################################################################################################################
#                         Set up Class/Master Container/Def to switch between Pages                              #
##################################################################################################################

class tkinterApp(tk.Tk):

    # Initialize function for class tkinterApp
    def __init__(self, *args, **kwargs): 

        # Initialize function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Create a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        
        # Create top level title
        self.wm_title("ENGR 467 Group Project - Cycle Conserving EDF Simulator")
        
        container.grid_rowconfigure(0, weight = 1)

        # Create a dictionary of frames
        self.frames = {} 

        # Add frame components to the dictionary.
        for F in (StartPage, Page1, Page2):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="news")

        self.show_frame(StartPage)

    # Display the current frame passed as a parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

##################################################################################################################
#                                               Start Page                                                       #
##################################################################################################################

class StartPage(tk.Frame):

    # Initialize  function for class Start Page
    def __init__(self, parent, controller):

        # Initialize function for Frame
        tk.Frame.__init__(self, parent)
        
        # Start Page info/instructions
        group_label = ttk.Label(self, text ="ENGR 467 Group Project", font = LARGEFONT)
        instuctions_title_label = ttk.Label(self, text ="Instructions", font = MEDIUMFONT)
        instuctions_label = ttk.Label(self, 
        text ="please enter the period, the worst case execution time and the actual execution time in the following page", font = SMALLFONT)
        
        # Place the Start Page info/instructions on grid
        group_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky="w")
        instuctions_title_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky="w")
        instuctions_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky="w")

        # Create begin button (to go to page1) and place on grid
        button1 = ttk.Button(self, text ="Begin >>>", command = lambda : controller.show_frame(Page1))
        button1.grid(row = 4, column = 0, padx = 10, pady = 10, sticky="se")


##################################################################################################################
#                                             Data Entry Page                                                    #
##################################################################################################################

class Page1(tk.Frame):

# Initialize function for class Page1
    def __init__(self, parent, controller):

# Initialize function for Frame
        tk.Frame.__init__(self, parent)
        
        
# Task Frame Creation ##############################################################################################  
# Create a Master Frame on left of Page 1 to contain all Task Entry frames and/or widgets
        frame_left=Frame(self, highlightbackground="grey", highlightthickness=1)
        frame_left.grid(column=0,row=0,rowspan=16,padx=5,pady=10,sticky="news")
        
        # Create Frame for "Enter Task Data" title
        frameTitle = Frame(frame_left)
        frameTitle.grid(column=0,row=0,pady=3,sticky="w")
        # Label and Place "Enter Task Data" 
        label = ttk.Label(frameTitle, text ="Enter Task Data", font = MEDIUMFONT)
        label.grid(row = 0, column = 0, padx = 20, pady = 5, sticky="nsew")

        # Create Frame 1 for Default Task 1 Name, Label, and Entry positions
        frame1 = Frame(frame_left)
        frame1.grid(column=0,row=2,rowspan=2,columnspan=4,padx=20,pady=3,sticky="nsew")
        
        # Label Default Text labels " Task, Period, Worst Case, Actual" For Task 1
        Task_1_label= tk.Label( frame1, text="Task 1")
        Period_label= tk.Label( frame1, text="Period", font = SMALLERFONT)
        Worst_Case_label= tk.Label( frame1, text="Worst Case", font = SMALLERFONT)
        Actual_Execution_label= tk.Label(frame1, text="Actual", font = SMALLERFONT)
        
        # Place Default Text Labels
        Task_1_label.grid(row=2, column=0, sticky="nsew")
        Period_label.grid(row=1, column=1, sticky="nsew")
        Worst_Case_label.grid(row=1, column=2, sticky="nsew")
        Actual_Execution_label.grid(row=1, column=3, sticky="nsew")

        # Generate Global variables for Task 1 (default) entries
        global T1PE
        global T1WC
        global T1BC
        
        # Define Task 1 (default) entry positions as entry boxes
        T1PE = tk.Entry(frame1)
        T1WC = tk.Entry(frame1)
        T1BC = tk.Entry(frame1)
        # Place Task 1 (default) entry boxes
        T1PE.grid(row=2, column=1)
        T1WC.grid(row=2, column=2)
        T1BC.grid(row=2, column=3)
        
        # Create Frames for task 2 through task 5
        frame_T2E = Frame(frame_left)
        frame_T3E = Frame(frame_left)
        frame_T4E = Frame(frame_left)
        frame_T5E = Frame(frame_left)
        
        # Place Frames for task 2 through task 5.
        frame_T2E.grid(column=0,row=4,columnspan=4,padx=20,pady=3, sticky="nsew")
        frame_T3E.grid(column=0,row=5,columnspan=4,padx=20,pady=3, sticky="nsew")
        frame_T4E.grid(column=0,row=6,columnspan=4,padx=20,pady=3, sticky="nsew")
        frame_T5E.grid(column=0,row=7,columnspan=4,padx=20,pady=3, sticky="nsew")
        
        # Create Frame for Task ADD and REMOVE Buttons
        frame_add_remove_T = Frame(frame_left)
        frame_add_remove_T.grid(column=0,row=10,columnspan=4, pady=20, padx=20,sticky="nsew")
# P-State Frame Creation #########################################################################################
# Create a Master Frame on right of Page 1 to contain all P-State Entry frames and/or widgets
        frame_right = Frame(self,highlightbackground="grey", highlightthickness=1)
        frame_right.grid(row=0, rowspan=16,column=1,padx=10,pady=10,sticky="news")

        # Create frame for P-State titles/options/info to 
        frame_PS_pre=Frame(frame_right)
        frame_PS_pre.grid(row=2, column=4)
        
        # Create frame for "P-State Selection" title
        frame_title_P=Frame(frame_right)
        frame_title_P.grid(row=2, column=0)
        # Create Label and Place 
        label = ttk.Label(frame_title_P, text ="P-State Selection", font = MEDIUMFONT)
        label.grid(row = 0, column = 0, padx = 20, pady = 5, sticky="w")
        
        #Create Frame for "Use Preselected P-states" info
        frame_use_presele=Frame(frame_right)
        frame_use_presele.grid(row=3, column=0)
        #Create Label and pLace
        label = ttk.Label(frame_use_presele, text ="Use Preselected P-States", font = SMALLFONT)
        label.grid(row = 0, column = 0, padx = 20, pady = 5, sticky="w")
        
        # Create frames for each Checkbox option
        frame_opt1=Frame(frame_right)
        frame_opt2=Frame(frame_right)
        frame_opt3=Frame(frame_right)
        
        # Place Frames for each checkbox option
        frame_opt1.grid(row=4, column=0)
        frame_opt2.grid(row=5, column=0)
        frame_opt3.grid(row=6, column=0)
        
        # Allows for the pre-selected P-State values to be toggled
        def clear2and3():
                
                var2.set('0')
                var3.set('0')
            
        def clear3and1():
                
                var3.set('0')
                var1.set('0')
                
        def clear1and2():
                
                var1.set('0')
                var2.set('0')
        
        # Define the check buttons C1,C2,C3
        var1 = tk.IntVar()
        var1.set('0')
        c1 = tk.Checkbutton(frame_opt1, text='1, 0.9, 0.8', variable=var1, onvalue=1, offvalue=0, command=clear2and3)
        c1.grid(row=0)
        
        var2 = tk.IntVar()
        var2.set('0')
        c2 = tk.Checkbutton(frame_opt2, text='0.9, 0.8, 0.7',variable=var2, onvalue=1, offvalue=0, command=clear3and1)
        c2.grid(row=0)
        
        var3=tk.IntVar()
        var3.set('0')
        c3 = tk.Checkbutton(frame_opt3, text='0.8, 0.7, 0.6',variable=var3, onvalue=1, offvalue=0, command=clear1and2)
        c3.grid(row=0)
        
        
        #Create a frame for the title "Select your own P-State values"
        frame_select=Frame(frame_right)
        frame_select.grid(row=7, column=0)
        #create Label and place
        label = ttk.Label(frame_select, text ="Select your own P State values", font = SMALLFONT)
        label.grid(row = 0, column = 0, padx = 20, pady = 5, sticky="w")
        
        #Create Frames for Custom P-State Entry Boxes
        frame_P1E=Frame(frame_right)
        frame_P2E=Frame(frame_right)
        frame_P3E=Frame(frame_right)
        frame_P4E=Frame(frame_right)
        frame_P5E=Frame(frame_right)
        #Place Frames for Custom P-State Entry Boxes
        frame_P1E.grid(row=8, column=0)
        frame_P2E.grid(row=9, column=0)
        frame_P3E.grid(row=10, column=0)
        frame_P4E.grid(row=11, column=0) 
        frame_P5E.grid(row=12, column=0)
        
        #Create Frame for ADD/REMOVE Custom P-State Button
        frame_add_remove_p=Frame(frame_right)
        frame_add_remove_p.grid(row=14, column=0)
        
        
        
# Button Frame Creation #########################################################################################
# Create 2 Frames on Bottom for "Return to instructions and " Schedule Feasibility" buttons
        Return_Button = Frame(self,bg='red')
        Check_SF_Button = Frame(self,bg='yellow')
        Return_Button.grid(column=0,row=16, pady=10, padx=5,sticky="w")
        Check_SF_Button.grid(column=1,row=16, pady=10, padx=5,sticky="e")
        

#                                               Task ADD/REMOVE                                                 #
################################################################################################################## 

        # Function that allows Tasks to be ADDED
        def add():
            
            global count_T
            global MAX_NUM_T

            if count_T < MAX_NUM_T:
                count_T += 1 # Increase the count by 1
                print("Task Number", count_T)
                command=Populate_Task_Matrix()
            else:
                tk.messagebox.showwarning(title="Error", message="You cannot add anymore tasks.")

        # Function that allows Tasks to be REMOVED
        def remove():
            global count_T
            global flag_T 
            global MIN_NUM_T 
            if count_T > MIN_NUM_T:
                count_T -= 1 # decrease the count by 1
                print("Task Number", count_T)
                flag_T=1
                command=Populate_Task_Matrix()
                flag_T=0 #reset flag to zero
                
            else: 
                tk.messagebox.showwarning(title="Error", message="You must have atleast 1 task.")


        # Function that is called by ADD and REMOVE TASKS to repopulate the Task Entry Boxes
        def Populate_Task_Matrix():
            global flag_T
            if count_T == 2 and flag_T ==0:  #ADD frame for task 2 and then place task label and entrys inside
                r=0 #row of task

                Task_2_label= tk.Label(frame_T2E, text="Task 2")
                Task_2_label.grid(row=0, column=0)

                global T2PE
                global T2WC
                global T2BC

                T2PE = tk.Entry(frame_T2E)
                T2WC = tk.Entry(frame_T2E)
                T2BC = tk.Entry(frame_T2E)

                T2PE.grid(row=r, column=1)
                T2WC.grid(row=r, column=2)
                T2BC.grid(row=r, column=3)  
                
                                
            elif count_T == 1 and flag_T ==1: #REMOVE task 2 by destroying the widget in frame 2
                for widgets in frame_T2E.winfo_children():
                    widgets.destroy()  
        
            elif count_T == 3 and flag_T ==0: #ADD frame for task 3 and then place task label and entrys inside:
                r=4 #row of task
                T3L= tk.Label(frame_T3E, text="Task 3")
                T3L.grid(row=r, column=0)

                global T3PE
                global T3WC
                global T3BC

                T3PE = tk.Entry(frame_T3E)
                T3WC = tk.Entry(frame_T3E)
                T3BC= tk.Entry(frame_T3E)

                T3PE.grid(row=r, column=1)
                T3WC.grid(row=r, column=2)
                T3BC.grid(row=r, column=3)

            elif count_T == 2 and flag_T ==1: #REMOVE task 2 by destroying the widget in frame 3
                for widgets in frame_T3E.winfo_children():
                    widgets.destroy()  
            
            elif count_T == 4 and flag_T ==0: #ADD frame for task 4 and then place task label and entrys inside:
                r=5 #row of task
                T4L= tk.Label(frame_T4E, text="Task 4")
                T4L.grid(row=r, column=0)

                global T4PE
                global T4WC
                global T4BC

                T4PE = tk.Entry(frame_T4E)
                T4WC = tk.Entry(frame_T4E)
                T4BC= tk.Entry(frame_T4E)

                T4PE.grid(row=r, column=1)
                T4WC.grid(row=r, column=2)
                T4BC.grid(row=r, column=3)

            elif count_T == 3 and flag_T ==1: #REMOVE task 4 by destroying the widget in frame 4
                for widgets in frame_T4E.winfo_children():
                    widgets.destroy()  

            elif count_T == 5 and flag_T ==0: #ADD frame for task 5 and then place task label and entrys inside:
                r=6 #row of task
                T5L= tk.Label(frame_T5E, text="Task 5")
                T5L.grid(row=r, column=0)

                global T5PE
                global T5WC
                global T5BC

                T5PE = tk.Entry(frame_T5E)
                T5WC = tk.Entry(frame_T5E)
                T5BC= tk.Entry(frame_T5E)
                
                T5PE.grid(row=r, column=1)
                T5WC.grid(row=r, column=2)
                T5BC.grid(row=r, column=3)

                
            elif count_T == 4 and flag_T ==1: #REMOVE task 5 by destroying the widgets in frame T5E
                for widgets in frame_T5E.winfo_children():
                    widgets.destroy()  

#                                             P State ADD/REMOVE                                                #
##################################################################################################################        
        
        # Function that allows P-States to be ADDED
        def add_p():
            
            global count_P
            global MAX_NUM_P

            if count_P < MAX_NUM_T:
                count_P += 1 # Increase the count by 1
                print("Custom P States Number", count_P)
                command=Populate_Task_Matrix_P()
            else:
                tk.messagebox.showwarning(title="Error", message="You cannot add anymore P-States.")
                
        # Function that allows P-States to be REMOVED
        def remove_p():
            global count_P
            global flag_P 
            global MIN_NUM_P 
            if count_P > MIN_NUM_P:
                count_P -= 1 # decrease the count by 1
                print("Custom P State Number", count_P)
                flag_P=1 # Set flage to 1
                command=Populate_Task_Matrix_P()
                flag_P=0 #reset flag to zero
                
            else: 
                tk.messagebox.showwarning(title="Error", message="Please select at least one custom P-State or use the preselected options above")

        # Function that is called by ADD and REMOVE P STATE to repopulate the P-State Entry Boxes
        def Populate_Task_Matrix_P():
            global flag_P
            if count_P == 1 and flag_P ==0:  #ADD frame for P-State 1 and then place P-State 1 label and entry inside
                r=0 #row of task

                P1L= tk.Label(frame_P1E, text="P-State 1")
                P1L.grid(row=0, column=0)
                global P1E
                P1E = tk.Entry(frame_P1E)
                P1E.grid(row=r, column=1)

                                
            elif count_P == 0 and flag_P ==1: #REMOVE P-State 1 by destroying all widgets in the frame_P1E
                for widgets in frame_P1E.winfo_children():
                    widgets.destroy()  

            elif count_P == 2 and flag_P ==0: #ADD frame for P-State 2 and then place P-State 2 label and entry inside
                r=0 #row of task
                
                P2L= tk.Label(frame_P2E, text="P-State 2")
                P2L.grid(row=0, column=0)
                global P2E
                P2E = tk.Entry(frame_P2E)
                P2E.grid(row=r, column=1)
                
            elif count_P == 1 and flag_P ==1: #REMOVE P-State 2 by destroying all widgets in the frame_P2E
                for widgets in frame_P2E.winfo_children():
                    widgets.destroy()  
            
            elif count_P == 3 and flag_P ==0: #ADD frame for P-State 3 and then place P-State 3 label and entry inside
                r=0 
                
                P3L= tk.Label(frame_P3E, text="P-State 3")
                P3L.grid(row=0, column=0)
                global P3E
                P3E = tk.Entry(frame_P3E)
                P3E.grid(row=r, column=1)

            elif count_P == 2 and flag_P ==1: #REMOVE P-State 3 by destroying all widgets in the frame_P3E
                for widgets in frame_P3E.winfo_children():
                    widgets.destroy()  

            elif count_P == 4 and flag_P ==0: #ADD frame for P-State 4 and then place P-State 4 label and entry inside
                r=0#row of task
                
                P4L= tk.Label(frame_P4E, text="P-State 4")
                P4L.grid(row=0, column=0)
                global P4E
                P4E = tk.Entry(frame_P4E)
                P4E.grid(row=r, column=1)

                
            elif count_P == 3 and flag_P ==1: #REMOVE P-State 4 by destroying all widgets in the frame_P4E
                for widgets in frame_P4E.winfo_children():
                    widgets.destroy()  
                    
            elif count_P == 5 and flag_P ==0: #ADD frame for P-State 5 and then place P-State 5 label and entry inside
                r=0#row of task
                
                P5L= tk.Label(frame_P5E, text="P-State 5")
                P5L.grid(row=0, column=0)
                global P5E
                P5E = tk.Entry(frame_P5E)
                P5E.grid(row=r, column=1)

                
            elif count_P == 4 and flag_P ==1: #REMOVE P-State 5 by destroying all widgets in the frame_P5E
                for widgets in frame_P5E.winfo_children():
                    widgets.destroy()  
                    

        # Create Task Button and place
        ADD_P = ttk.Button(frame_add_remove_p, text='(+) ADD P-STATE', command=add_p).grid(row = 14, column = 1, padx = 10, pady = 10,sticky='s')
        # Create Remove task button and place
        REMOVE_P = ttk.Button(frame_add_remove_p, text='(-) REMOVE P-STATE', command=remove_p).grid(row = 14, column = 2, padx = 10, pady = 10,sticky='s')
        

#                                               Task READ entries                                               #
##################################################################################################################   
    
        def read_data_T():
            global Task_output
            global warn_T
            warn_T=0
            
            if count_T >= 1:
                a=T1PE.get()
                b=T1WC.get()
                c=T1BC.get()
                d=[0,0,0]
                if len(a) !=0 and len(b) !=0 and len(c) !=0:
                    if a.isalpha() or b.isalpha() or c.isalpha():
                        tk.messagebox.showwarning(title="Error 7", message="Task 1 - Please don't type in letters")
                        warn_T=1   
                    else:
                        a=float(a)  
                        b=float(b)
                        c=float(c)

                        if a !=0 and b !=0 and c !=0:
                        
                            if a > 0 and b > 0 and c > 0:
                        
                                if b >= c:
                        
                                    if b <= a:
                        
                                        if c <= a:
                                            d=[a,b,c]
                                            Task_output=np.matrix([d])  
                                        else:
                                            tk.messagebox.showwarning(title="Error 1", message="The Task 1 Worst Case Execution time cannot be longer than the period")
                                            warn_T=1  
                                    else:
                                        tk.messagebox.showwarning(title="Error 2", message="The Task 1 Actual Case Execution time cannot be longer than the period")
                                        warn_T=1  
                                else:
                                    tk.messagebox.showwarning(title="Error 3", message="The Task 1 Worst Case Execution time must be longer than (or equal to) the Actual Execution time")
                                    warn_T=1   
                            else:
                                tk.messagebox.showwarning(title="Error 4", message="Task 1 cannot have any negative values")
                                warn_T=1        
                        else:
                            tk.messagebox.showwarning(title="Error 5", message="Task 1 cannot have any values equal to 0")
                            warn_T=1  
                else:
                    tk.messagebox.showwarning(title="Error 6", message="Task 1 - Please make sure all entry boxes are filled")
                    warn_T=1      

            
            if count_T >= 2:
                a=T2PE.get()
                b=T2WC.get()
                c=T2BC.get()
                e=[0,0,0]
                if len(a) !=0 and len(b) !=0 and len(c) !=0:
                    if a.isalpha() or b.isalpha() or c.isalpha():
                        tk.messagebox.showwarning(title="Error 7", message="Task 2- Please don't type in letters")
                        warn_T=1    
                    else: 
                        a=float(a)  
                        b=float(b)
                        c=float(c)
                        
                        if a !=0 and b !=0 and c !=0:
                            
                                if a > 0 and b > 0 and c > 0:
                            
                                    if b >= c:
                            
                                        if b <= a:
                            
                                            if c <= a:
                                                e=[a,b,c]
                                                Task_output=np.matrix([d, e])  
                
                                            else:
                                                tk.messagebox.showwarning(title="Error 1", message="The Task 2 Worst Case Execution time cannot be longer than the period")
                                                warn_T=1  
                                        else:
                                            tk.messagebox.showwarning(title="Error 2", message="The Task 2 Actual Case Execution time cannot be longer than the period")
                                            warn_T=1  
                                    else:
                                        tk.messagebox.showwarning(title="Error 3", message="The Task 2 Worst Case Execution time must be longer than (or equal to) the Actual Execution time")
                                        warn_T=1   
                                else:
                                    tk.messagebox.showwarning(title="Error 4", message="Task 2 cannot have any negative values")
                                    warn_T=1        
                        else:
                                tk.messagebox.showwarning(title="Error 5", message="Task 2 cannot have any values equal to 0")
                                warn_T=1  
                else:
                    tk.messagebox.showwarning(title="Error 6", message="Task 2 - Please make sure all entry boxes are filled")
                    warn_T=1  

            if count_T >= 3:
                a=T3PE.get()
                b=T3WC.get()
                c=T3BC.get()
                f=[0,0,0]
                if len(a) !=0 and len(b) !=0 and len(c) !=0:
                    if a.isalpha() or b.isalpha() or c.isalpha():
                        tk.messagebox.showwarning(title="Error 7", message="Task 3 - Please don't type in letters")
                        warn_T=1    
                    else: 
                        a=float(a)  
                        b=float(b)
                        c=float(c)
                        
                        if a !=0 and b !=0 and c !=0:
                            
                                if a > 0 and b > 0 and c > 0:
                            
                                    if b >= c:
                            
                                        if b <= a:
                            
                                            if c <= a:
                                                f=[a,b,c] 
                                                Task_output=np.matrix([d, e, f])  
                                            else:
                                                tk.messagebox.showwarning(title="Error 1", message="The Task 3 Worst Case Execution time cannot be longer than the period")
                                                warn_T=1  
                                        else:
                                            tk.messagebox.showwarning(title="Error 2", message="The Task 3 Actual Case Execution time cannot be longer than the period")
                                            warn_T=1  
                                    else:
                                        tk.messagebox.showwarning(title="Error 3", message="The Task 3 Worst Case Execution time must be longer than (or equal to) the Actual Execution time")
                                        warn_T=1   
                                else:
                                    tk.messagebox.showwarning(title="Error 4", message="Task 3 cannot have any negative values")
                                    warn_T=1        
                        else:
                                tk.messagebox.showwarning(title="Error 5", message="Task 3 cannot have any values equal to 0")
                                warn_T=1  
                else:
                    tk.messagebox.showwarning(title="Error 6", message="Task 3 - Please make sure all entry boxes are filled")
                    warn_T=1   
                    
            if count_T >= 4:
                a=T4PE.get()
                b=T4WC.get()
                c=T4BC.get()
                g=[0,0,0]
                if len(a) !=0 and len(b) !=0 and len(c) !=0: 
                    if a.isalpha() or b.isalpha() or c.isalpha():
                        tk.messagebox.showwarning(title="Error 7", message="Task 4- Please don't type in letters")
                        warn_T=1    
                    else:
                        a=float(a)  
                        b=float(b)
                        c=float(c)
                        
                        if a !=0 and b !=0 and c !=0:
                            
                                if a > 0 and b > 0 and c > 0:
                            
                                    if b >= c:
                            
                                        if b <= a:
                            
                                            if c <= a:
                                                g=[a,b,c]
                                                Task_output=np.matrix([d, e, f, g])   
                                            else:
                                                tk.messagebox.showwarning(title="Error 1", message="The Task 4 Worst Case Execution time cannot be longer than the period")
                                                warn_T=1  
                                        else:
                                            tk.messagebox.showwarning(title="Error 2", message="The Task 4 Actual Case Execution time cannot be longer than the period")
                                            warn_T=1  
                                    else:
                                        tk.messagebox.showwarning(title="Error 3", message="The Task 4 Worst Case Execution time must be longer than (or equal to) the Actual Execution time")
                                        warn_T=1   
                                else:
                                    tk.messagebox.showwarning(title="Error 4", message="Task 4 cannot have any negative values")
                                    warn_T=1        
                        else:
                                tk.messagebox.showwarning(title="Error 5", message="Task 4 cannot have any values equal to 0")
                                warn_T=1  
                                
                else:
                    tk.messagebox.showwarning(title="Error 6", message="Task 4 - Please make sure all entry boxes are filled") 
                    warn_T=1  


            if count_T >= 5:
                a=T5PE.get()
                b=T5WC.get()
                c=T5BC.get()
                h=[0,0,0]
                
                if len(a) !=0 and len(b) !=0 and len(c) !=0:
                    if a.isalpha() or b.isalpha() or c.isalpha():
                        tk.messagebox.showwarning(title="Error 7", message="Task 5 - Please don't type in letters")
                        warn_T=1    
                    else: 
                        a=float(a)  
                        b=float(b)
                        c=float(c)
                        
                        
                        if a !=0 and b !=0 and c !=0:
                        
                            if a > 0 and b > 0 and c > 0:
                        
                                if b >= c:
                        
                                    if b <= a:
                        
                                        if c <= a:
                                            h=[a,b,c]
                                            Task_output=np.matrix([d, e, f, g, h])  
                                        else:
                                            tk.messagebox.showwarning(title="Error 1", message="The Task 5 Worst Case Execution time cannot be longer than the period")
                                            warn_T=1  
                                    else:
                                        tk.messagebox.showwarning(title="Error 2", message="The Task 5 Actual Case Execution time cannot be longer than the period")
                                        warn_T=1  
                                else:
                                    tk.messagebox.showwarning(title="Error 3", message="The Task 5 Worst Case Execution time must be longer than (or equal to) the Actual Execution time")
                                    warn_T=1   
                            else:
                                tk.messagebox.showwarning(title="Error 4", message="Task 5 cannot have any negative values")
                                warn_T=1        
                        else:
                            tk.messagebox.showwarning(title="Error 5", message="Task 5 cannot have any values equal to 0")
                            warn_T=1  
                    
                else:
                    tk.messagebox.showwarning(title="Error 6", message="Task 5 - Please make sure all entry boxes are filled")
                    warn_T=1   
            if warn_T==1:
                Task_output=[]
            print("Final Task Output Matrix",Task_output)
#####################                   GET Preselected P-States                #############################               
            global Pstate_output
            if var1.get()==1:
                a=1
                b=0.9
                c=0.8
                
                Pstate_output.append(a)
                Pstate_output.append(b)
                Pstate_output.append(c)
                
            elif var2.get()==1:
                a=0.9
                b=0.8
                c=0.7
                
                Pstate_output.append(a)
                Pstate_output.append(b)
                Pstate_output.append(c)
                
            elif var3.get()==1:
                a=0.8
                b=0.7
                c=0.6
                
                Pstate_output.append(a)
                Pstate_output.append(b)
                Pstate_output.append(c)
                
            elif count_P==0:
                tk.messagebox.showwarning(title="Error", message="You must either use Preselected P-States or add your own")
#####################                       GET Custom P-State Values                  ############################# 
            global warn_p
            warn_p=0
            if count_P >= 1:  
                a= P1E.get()
                if len(a) !=0: 
                    if a.isalpha():
                        tk.messagebox.showwarning(title="Error 7", message="P-State 1 - Please don't type in letters")
                        warn_p=1   
                    else: 
                        a=float(a) 
                        
                        if a !=0: 
                            if a > 0:
                                if a <= 1:
                                    Pstate_output.append(a)
                                else:    
                                    tk.messagebox.showwarning(title="Error 1", message="Custom P-State 1 cannot be larger than 1")
                                    warn_p=1  
                            else:
                                tk.messagebox.showwarning(title="Error 2", message="Custom P-State 1 cannot have any negative values")
                                warn_p=1   
                        else:
                            tk.messagebox.showwarning(title="Error 3", message="Custom P-State 1 cannot have any values equal to 0")
                            warn_p=1   
                else:
                    tk.messagebox.showwarning(title="Error 6", message="Custom P-State 1 - Please make sure all entry boxes are filled")
                    warn_p=1 
                    
            if count_P >= 2:
                a= P2E.get()
                if len(a) !=0: 
                    if a.isalpha():
                        tk.messagebox.showwarning(title="Error 7", message="P-State 1 - Please don't type in letters")
                        warn_p=1 
                    else: 
                        a=float(a) 
                                
                        if a !=0: 
                            if a > 0:
                                if a <= 1:
                                    Pstate_output.append(a)
                                else:    
                                    tk.messagebox.showwarning(title="Error 1", message="Custom P-State 2 cannot be larger than 1")
                                    warn_p=1  
                            else:
                                tk.messagebox.showwarning(title="Error 2", message="Custom P-State 2 cannot have any negative values")
                                warn_p=1   
                        else:
                            tk.messagebox.showwarning(title="Error 3", message="Custom P-State 2 cannot have any values equal to 0")
                            warn_p=1   
                else:
                    tk.messagebox.showwarning(title="Error 6", message="Custom P-State 2 - Please make sure all entry boxes are filled")
                    warn_p=1     
                    
            if count_P >= 3:
                a= P3E.get()
                if len(a) !=0: 
                    if a.isalpha():
                        tk.messagebox.showwarning(title="Error 7", message="P-State 1 - Please don't type in letters")
                        warn_p=1  
                    else:
                        a=float(a) 
                                
                        if a !=0: 
                            if a > 0:
                                if a <= 1:
                                    Pstate_output.append(a)
                                else:    
                                    tk.messagebox.showwarning(title="Error 1", message="Custom P-State 3 cannot be larger than 1")
                                    warn_p=1  
                            else:
                                tk.messagebox.showwarning(title="Error 2", message="Custom P-State 3 cannot have any negative values")
                                warn_p=1   
                        else:
                            tk.messagebox.showwarning(title="Error 3", message="Custom P-State 3 cannot have any values equal to 0")
                            warn_p=1   
                else:
                    tk.messagebox.showwarning(title="Error 6", message="Custom P-State 3 - Please make sure all entry boxes are filled")
                    warn_p=1 
                    
            if count_P >= 4:
                a= P4E.get()
                if len(a) !=0: 
                    if a.isalpha():
                        tk.messagebox.showwarning(title="Error 7", message="P-State 1 - Please don't type in letters")
                        warn_p=1 
                    else: 
                        a=float(a) 
                                
                        if a !=0: 
                            if a > 0:
                                if a <= 1:
                                    Pstate_output.append(a)
                                else:    
                                    tk.messagebox.showwarning(title="Error 1", message="Custom P-State 4 cannot be larger than 1")
                                    warn_p=1   
                            else:
                                tk.messagebox.showwarning(title="Error 2", message="Custom P-State 4 cannot have any negative values")
                                warn_p=1   
                        else:
                            tk.messagebox.showwarning(title="Error 3", message="Custom P-State 4 cannot have any values equal to 0")
                            warn_p=1   
                else:
                    tk.messagebox.showwarning(title="Error 6", message="Custom P-State 4 - Please make sure all entry boxes are filled")
                    warn_p=1    
                    
            if count_P >= 5:
                a= P5E.get()
                if len(a) !=0: 
                    if a.isalpha():
                        tk.messagebox.showwarning(title="Error 7", message="P-State 1 - Please don't type in letters")
                        warn_p=1 
                    else: 
                        a=float(a) 
                        if a !=0: 
                            if a > 0:
                                if a <= 1:
                                    Pstate_output.append(a)
                                else:    
                                    tk.messagebox.showwarning(title="Error 1", message="Custom P-State 5 cannot be larger than 1")
                                    warn_p=1   
                            else:
                                tk.messagebox.showwarning(title="Error 2", message="Custom P-State 5 cannot have any negative values")
                                warn_p=1   
                        else:
                            tk.messagebox.showwarning(title="Error 3", message="Custom P-State 5 cannot have any values equal to 0")
                            warn_p=1   
                else:
                    tk.messagebox.showwarning(title="Error 6", message="Custom P-State 2 - Please make sure all entry boxes are filled")
                    warn_p=1 
            if warn_p==1:
                Pstate_output=[]
                warn_p=0 #reset flag
                    
            Pstate_output = list(set(Pstate_output))
            print("P-State Output", Pstate_output)
#####################                          PAGE 1  BUTTONS                      #############################

        # Create "Return to instructions" button and place
        button1 = ttk.Button(Return_Button, text ="<<< Return to Instructions",
                            command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 10, column=0,  sticky='w')

        # Create "Check Schedule feasibility" button and place
        button2 = ttk.Button(Check_SF_Button, text ="Check Schedule Feasibility >>>", command = read_data_T )
                            # command = lambda : controller.show_frame(Page2))
                            
        button2.grid(row = 10, column=0, sticky='news')


        # Create Task Button and place
        ADD_P = ttk.Button(frame_add_remove_T, text='(+) ADD TASK', command=add).grid(row = 16, column = 1, padx = 10, pady = 10,sticky='w')


        # Create Remove task button and place
        REMOVE_P = ttk.Button(frame_add_remove_T, text='(-) REMOVE TASK', command=remove).grid(row = 16, column = 2, padx = 10, pady = 10,sticky='e')

##################################################################################################################
#                                               Results Page                                                     #
##################################################################################################################

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Results", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="New Data Entry",
                            command = lambda : controller.show_frame(Page1))
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
# Driver Code
app = tkinterApp()
app.mainloop()