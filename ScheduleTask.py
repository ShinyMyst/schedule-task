from apscheduler.schedulers.blocking import BlockingScheduler
import win32console   
import win32gui       
import datetime
import time

window = win32console.GetConsoleWindow()


def user_input():
    print("Please select a time.")
    print("Must be in 24hr format.")
    time = input()
    minutes = int(time[-2:])
    hours = int(time[:-2])
    print("Select your message.")
    message = input()
    print("You want to say:", message, "at", time, "?")
    answer = input().lower()

    if answer.startswith("y"):
        pass
    else:
        print("Let's try again")


def create_job(scheduler, hour, minute, message):

                         

def run_script(window):
    win32gui.ShowWindow(window, 1)  # Show window
    print('Its time to leave.')
          
win32gui.ShowWindow(window, 0)  # Hide window
scheduler = BlockingScheduler()
scheduler.add_job(run_script, 'cron', hour=10, minute=1, args=[window])
scheduler.start()





def main():
    pass

if __name__ == "__main__":
    main()

# Hiding and Showing Windows: https://stackoverflow.com/questions/67215357/hide-a-python-caused-window

