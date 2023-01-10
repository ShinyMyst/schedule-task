from apscheduler.schedulers.blocking import BlockingScheduler
import win32console   
import win32gui       
import datetime
import time



def user_input():
    print("Please select a time.")
    print("Must be in 24hr format.")
    time = input()
    minute = int(time[-2:])
    hour = int(time[:-2])
    print("Select your message.")
    message = input()
    print("You want to say:", message, "at", time, "?")
    answer = input().lower()

    if answer.startswith("y"):
        return hour, minute, message
    else:
        print("Let's try again")
        


def create_job(scheduler, window, hour, minute, message):
    scheduler.add_job(run_script, 'cron', hour=hour, minute=minute, args=[window, message])

                         

def run_script(window, message):
    """Displays provided message"""
    win32gui.ShowWindow(window, 1) 
    print(message)
          

def main():
    window = win32console.GetConsoleWindow()
    scheduler = BlockingScheduler()
    
    args = user_input()
    create_job(scheduler, window, *args)
    win32gui.ShowWindow(window, 0) 
    scheduler.start()


if __name__ == "__main__":
    main()

# Possible additions
# GUI to display messages instead of CMD
# Other scheduled tasks besides messages


# Hiding and Showing Windows: https://stackoverflow.com/questions/67215357/hide-a-python-caused-window

