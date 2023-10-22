import os;
from sys import platform
from datetime import datetime, time
from tkinter import *

DIALOG_DURATION_MS = 300000
REFRESH_PERIOD_SECONDS = 60
HOURLY_BREAK_IN_MINUTES = [0, 30]
CLOSE_KEY = 'E'
FORCED_SLEEP_PERIOD = (time(hour=23,minute=30), time(hour=8,minute=30))

class DialogueBox():
    def check_for_closing(self, event=Tk.event_info):
        w=Label(self.win,text="Key Pressed:"+event.char)
        w.place(x=70,y=90)
        if(event.char == CLOSE_KEY):
            self.win.destroy()
    def disable_closing():
        pass
    def __init__(self,message=str) -> None:
        self.win = Tk()
        self.win.geometry("600x350")
        Label(self.win, 
            text= message,
            font=('Helvetica bold', 15)
        ).pack(pady=20)
        self.win.attributes('-topmost',True)
        self.win.overrideredirect(True)
        self.win.after(DIALOG_DURATION_MS, 
            lambda:self.win.destroy()
        )
        self.win.bind("<Key>",self.check_for_closing)
        self.win.protocol("WM_DELETE_WINDOW",self.disable_closing)
        self.win.state('zoomed')
        self.win.mainloop()
        pass

def is_time_for_rest(current_time=datetime):
    if current_time > FORCED_SLEEP_PERIOD[0] or current_time < FORCED_SLEEP_PERIOD[1]:
        return True
    return False

def is_time_for_break(current_time=datetime):
    if current_time.minute in HOURLY_BREAK_IN_MINUTES:
        return True
    return False

def force_shut_down():
    if platform == "linux" or platform == "linux2":
    # linux
        return
    elif platform == "darwin":
    # OS X
        return
    elif platform == "win32":
        os.system("shutdown /s /t 1")
    DialogueBox(message="Computer Will Be shutting down.")



def open_warning_dialog():
    DialogueBox(message="Hello! Please Take some rest first")

def main():
    while(True):
        current_time = datetime.now()
        if is_time_for_break(current_time):
            open_warning_dialog()
        if is_time_for_rest(current_time):
            force_shut_down()
        time.sleep(REFRESH_PERIOD_SECONDS) 


if __name__ == "__main__":
    main()