from apscheduler.schedulers.blocking import BlockingScheduler
import win32console   
import win32gui       
import datetime
import time

#dateparser.parse(value, settings={'TIMEZONE': 'UTC'})

class TimmeFormatError(Exception):
    pass

class ScheduleTask():
    """Schedules a message to be sent via the command prompt at specified time."""
    
    def __init__(self):
        self.window = win32console.GetConsoleWindow()
        self.scheduler = BlockingScheduler()

        
    def verify_time(self):
        """Ensures valid time input.  Returns the minute and hour."""
        while True:
            try:
                time = input()
                minute = int(time[-2:])
                hour = int(time[:-2])
                if len(time) > 4:
                    raise TimeFormatError()
                if minute < -1 or minute > 59:
                    raise TimeFormatError()
                if hour < -1 or hour > 23:
                    raise TimeFormatError()
            except:
                print("Incorrect value.  Please try again in HHMM format.")
                continue
            else:
                return minute, hour

    def user_input(self):
        while True:
            # Get and verify time
            print("Please select a time.")
            print("Must be in 24hr format.")
            minute, hour = self.verify_time()
            
            # Get and verify message
            print("Select your message.")
            message = input()

            # Confirm message
            print("You want to say:")
            print(message, "at", str(hour)+str(minute) + "?")
            answer = input().lower()
            if answer.startswith("y"):
                return hour, minute, message
            else:
                print("Restarting questions...")

    def send_msg(self, message):
        """Opens window and displays message."""
        win32gui.ShowWindow(self.window, 1) 
        print(message, '\n')
        self.new_message_prompt()
        
                
    def create_task(self):
        """Creates a task."""
        hour, minute, message = self.user_input()
        self.scheduler.add_job(self.send_msg, 'cron', hour=hour, minute=minute, args=[message])


    def run_tasks(self):
        """Hides window and runs created tasks."""
        win32gui.ShowWindow(self.window, 0) 
        self.scheduler.start()

        
    def new_message_prompt(self):
        """Prompt user to create a new message."""
        print("Create a new message?")
        if answer.startswith("y"):
            self.create_task()
            self.run_tasks()
        
            
def main():
    task = ScheduleTask()
    task.create_task()
    task.run_tasks()


if __name__ == "__main__":
    main()

# Hiding and Showing Windows: https://stackoverflow.com/questions/67215357/hide-a-python-caused-window
# Put message in a windows pop-up box instead
# Setting up multiple tasks
# View scheduled tasks
# Running in the hidden icons section of start bar
# GUI options



