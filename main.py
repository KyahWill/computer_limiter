import os;
from datetime import datetime
from tkinter import *
import time

DIALOG_DURATION_MS = 300000
REFRESH_PERIOD_SECONDS = 60
HOURLY_BREAK_IN_MINUTES = [0, 30]
FORCED_SLEEP_PERIOD = (datetime.time(23,30,0), datetime.time(8,30,0))
def is_time_for_break(current_time):
    if current_time.minute in HOURLY_BREAK_IN_MINUTES:
        return True
    return False

def open_warning_dialog():
    win = Tk()
    win.geometry("600x350")
    Label(win, 
        text= "Hello! Please take some rest! ",
        font=('Helvetica bold', 15)
    ).pack(pady=20)
    win.attributes('-topmost',True)
    win.overrideredirect(True)
    win.after(DIALOG_DURATION_MS, 
        lambda:win.destroy()
    )
    win.mainloop()

def main():
    while(True):
        current_time = datetime.now()
        if is_time_for_break(current_time):
            open_warning_dialog()
        time.sleep(REFRESH_PERIOD_SECONDS) 


if __name__ == "__main__":
    open_warning_dialog()