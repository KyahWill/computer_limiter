import os;
from sys import platform, argv
from datetime import datetime, time
from tkinter import *
from time import sleep

DIALOG_DURATION_MS = 300000
REFRESH_PERIOD_SECONDS = 60
HOURLY_BREAK_IN_MINUTES = [0, 30]
CLOSE_KEY = 'E'
FORCED_SLEEP_PERIOD = (time(hour=23,minute=0), time(hour=8,minute=30))
FONT_SIZE = 72
RESOLUTION = '1440x720'


class DialogueBox():
    def initialize_windows(self):
        import winsound
    def close_window(self):
        self.win.destroy()
        if platform == "linux" or platform == "linux2":
        # linux
            return
        elif platform == "darwin":
        # OS X
            return
        elif platform == "win32":
            for i in range(3):
                freq=1000
                dur=500
                winsound.Beep(freq,dur)
    def check_for_closing(self, event=Tk.event_info):
        if(event.char == CLOSE_KEY):
            self.close_window()
    def disable_closing():
        pass
    def __init__(self,message=str) -> None:
        if platform == "win32":
            self.initialize_windows()
        
        self.win = Tk()
        self.win.geometry(RESOLUTION)
        Label(self.win, 
            text= message,
            font=('Helvetica bold', FONT_SIZE)
        ).pack(expand=True,pady=20)
        self.win.attributes('-topmost',True)
        self.win.overrideredirect(True)
        self.win.after(DIALOG_DURATION_MS, 
            lambda:self.close_window()
        )
        self.win.bind("<Key>",self.check_for_closing)
        self.win.protocol("WM_DELETE_WINDOW",self.disable_closing)
        self.win.state('normal')
        self.win.mainloop()
        pass

def is_time_for_rest(current_time=datetime):
    if current_time.time() > FORCED_SLEEP_PERIOD[0] or current_time.time() < FORCED_SLEEP_PERIOD[1]:
        return True
    return False

def is_time_for_break(current_time=datetime):
    if current_time.minute in HOURLY_BREAK_IN_MINUTES:
        return True
    return False

def force_shut_down():
    if platform == "linux" or platform == "linux2":
        os.system("shutdown")
    # linux
        return
    elif platform == "darwin":
    # OS X
        return
    elif platform == "win32":
        os.system("shutdown /s /t 30")
    DialogueBox(message="Computer Will Be shutting down.")

def open_warning_dialog():
    DialogueBox(message="Hello! Please Take some rest first")

def main(no_break = False, no_shutdown= False):
    while(True):
        current_time = datetime.now()
        if is_time_for_break(current_time) and no_break == False:
            open_warning_dialog()
        if is_time_for_rest(current_time) and no_shutdown == False:
            force_shut_down()
        sleep(REFRESH_PERIOD_SECONDS) 


if __name__ == "__main__":
    if (len(argv) > 1):
        if(argv[1] == "--test"):
            open_warning_dialog()
        if(argv[1] == "--no-shutdown"):
            main(no_shutdown = True)
        if(argv[1] == "--no-breaks"):
            main(no_break = True)
    else:
        main() 
