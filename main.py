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


class DialogueBox():
    def check_for_closing(self, event=Tk.event_info):
        if(event.char == CLOSE_KEY):
            self.win.destroy()


    def disable_closing():
        pass


    def __init__(self,message=str) -> None:
        self.win = Tk()
        self.win.geometry("600x350")
        Label(self.win, 
            text= message,
            font=('Helvetica bold', FONT_SIZE)
        ).pack(expand=True,pady=20)
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
    if current_time.time() > FORCED_SLEEP_PERIOD[0] or current_time.time() < FORCED_SLEEP_PERIOD[1]:
        return True
    return False


def is_time_for_break(current_time=datetime):
    if current_time.minute in HOURLY_BREAK_IN_MINUTES:
        return True
    return False


def get_os_info():
    return platform.system().lower()


def force_shut_down():
    # Missing guard checks for user with root access.

    # Linux platform
    if get_os_info() == "linux":
        os.system("shutdown -h now")

    # MacOS platform
    elif get_os_info == "darwin":
        os.system("shutdown -h now")

    # Windows platform
    # Modified windows checking platform, should use sys.platform to get "win32" and platform.system() for "windows"
    elif get_os_info == "windows" or sys.platform == "win32":
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
        sleep(REFRESH_PERIOD_SECONDS) 


if __name__ == "__main__":
    if(len(argv) > 1 and argv[1] == "--test"):
        open_warning_dialog()
    else:
        main() 