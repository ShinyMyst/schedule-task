from apscheduler.schedulers.blocking import BlockingScheduler
import win32console   
import win32gui       
import datetime
import time

window = win32console.GetConsoleWindow()

def run_script(window):
    win32gui.ShowWindow(window, 1)  # Show window
    print('This works.')
          
win32gui.ShowWindow(window, 0)  # Hide window
scheduler = BlockingScheduler()
scheduler.add_job(run_script, 'cron', hour=10, minute=58, args=[window])
scheduler.start()

# Hiding and Showing Windows: https://stackoverflow.com/questions/67215357/hide-a-python-caused-window

