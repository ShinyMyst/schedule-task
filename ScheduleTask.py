from apscheduler.schedulers.blocking import BlockingScheduler
import win32console   
import win32gui       
import datetime
import time
import tkinter as tk
from tkinter import messagebox as msgbox


class TimeFormatError(Exception):
    pass

    """def handle_exception(self):
        print("RUN")
        msgbox.showerror(title="TEST", message="THIS IS TEST")"""



class MessageWindow():  
    def __init__(self, title, size=None):
        # Create root window and hide it until called.
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(size) # Size in format "intxint"
        self.root.withdraw()

        # Store Entry Data
        self.entry_data = []


    def create_label(self, text, size=None):
        """Creates a line of text in the window."""
        label = tk.Label(self.root, text=text, font=(size))
        label.pack()


    def create_entry(self):
        """Creates an entry box for the window"""
        entry = tk.Entry(self.root)
        self.entry_data.append(entry)
        entry.pack()


    def create_button(self, text, size=None,  command=None):
        """Create a button that executes given command"""
        button = tk.Button(self.root, text=text, font=(size), command=command)
        button.pack()
        
    def get_entry_data(self):
        """Collect and return the data from all entry fields."""
        data = []
        for entry in self.entry_data:
            data.append(entry.get())
        return data
        # print(data)


    def destroy(self):
        """Destroys window entirely."""
        self.root.destroy()

    def show_window(self):
        """Shows window on screen, restarting the event loop."""
        self.root.deiconify()
 

    
              


class ScheduleTask():
    """Schedules a message to be sent via the command prompt at specified time."""
    
    def __init__(self):
        self.scheduler = BlockingScheduler()
        

        
    def _process_time(self, time):
        """Ensures valid time input.  Returns the minute and hour."""

        while True:
            try:
                minute = int(time[-2:])
                hour = int(time[:-2])
                if len(time) > 4:
                    raise TimeFormatError
                if minute < -1 or minute > 59:
                    raise TimeFormatError()
                if hour < -1 or hour > 23:
                    raise TimeFormatError
            except:
                print("Incorrect value.  Please try again in HHMM format.")
                continue
            else:
                return hour, minute


    def _submit_input(self):
        """When user form is submitted, processes data input and schedules the task."""
        # Retrieve Submitted Data - Data will be recieved in a list - [time:str, message:str]
        data = self._entry_window.get_entry_data()
        time = data[0]
        message = data[1]

        # Process info and schedule task
        hour, minute = self._process_time(time)
        self._schedule_task(hour, minute, message)       


    def create_input_window(self):
        """Creates window to accept user input"""
        self._entry_window = MessageWindow("Task Scheduler", "300x150")

        # Time Entry
        self._entry_window.create_label("Please select time:", 20)
        self._entry_window.create_label("Must be 24hr format", 20)
        self._entry_window.create_entry()
        # Text Entry
        self._entry_window.create_label("Please input message:", 20)
        self._entry_window.create_entry()
        # Submit
        self._entry_window.create_button("Submit", command = self._submit_input)
        self._entry_window.show_window()

       

    def _show_message(self, message):
        """Opens window and displays message."""
        self.notify_window = MessageWindow("Notification", "300x150")
        self.notify_window.create_label(message, 20)
        self.notify_window.show_window()
        print("SHOW")

        
                
    def _schedule_task(self, hour, minute, message):
        """Schedules a task and starts the scheduler."""
        print("Task created.  Send:", message, "at", hour,':',minute)
        self._entry_window.destroy()
        self.scheduler.add_job(self._show_message, 'cron', hour=hour, minute=minute, args=[message])
        self.scheduler.start()


       
    def new_message_prompt(self):
        """Prompt user to create a new message."""
        # Not yet updated to fit new methods.I
        return
        """print("Create a new message?")
        if answer.startswith("y"):
            self.create_task()
            self.run_tasks()"""
        
            
def main():
    task = ScheduleTask()
    task.create_input_window()


if __name__ == "__main__":
    main()

# Hiding and Showing Windows: https://stackoverflow.com/questions/67215357/hide-a-python-caused-window
# Put message in a windows pop-up box instead
# Setting up multiple tasks
# View scheduled tasks
# Running in the hidden icons section of start bar
# GUI options
# Error pop-up if there's an issue
# Alternatively, red text above the box and submission fails

# Fix window class
# Message window not appearing for final message
# Data validation needs fixed



