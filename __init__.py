import tkinter as tk
import subprocess
import os
import sys
from math import *
from time import sleep
subprocess.run(["xrdb", "-merge", os.path.dirname(os.path.abspath(__file__)) + "/Xdefaults"])
class Terminal(tk.Frame):
    def __init__(self, master=None, font='Monospace', size=12):
        super().__init__(master)
        self.master = master
        self.create_widgets(font,size)

    def create_widgets(self,font, size):
        # Create a frame to hold the xterm window
        self.xterm_frame = tk.Frame(self.master,bg="white")
        self.xterm_frame.pack(fill="both", expand=True)
        # Wait for the xterm_frame to be created
        self.xterm_frame.update_idletasks()
        self.update_resolution()
        self.run(command='true')
        # Get the xterm_frame window ID
        xterm_window_id = self.xterm_frame.winfo_id()
        print(xterm_window_id)
        if xterm_window_id:
            # Launch the xterm window with the appropriate font
            xterm_command="'python command_tkterm " + str(xterm_window_id) + " && sleep 10 || sleep 10'"
            command = f"xterm -ah -into {xterm_window_id} -rightbar -fa '{font}' -fs '{size}' -e '{xterm_command}' &>/dev/null"
            subprocess.Popen([command], shell=True)
        else:
            print("Unable to get window ID for xterm")
    def update_resolution(self):
        with open("/tmp/tkTermrs" + str(self.xterm_frame.winfo_id()), 'w') as reso:
            width = round(self.xterm_frame.winfo_width() / 10) - 1
            height = round(self.xterm_frame.winfo_height() / 19) - 1
            reso.write("\e[8;" + str(height) + ";" + str(width) + "t")
        self.after(100, self.update_resolution)
    def run(self, command="bash"):
        with open("/tmp/tkTerm" + str(self.xterm_frame.winfo_id()), 'a') as command_file:
            command_file.write("\n" + command)
    def display_true(self):
        self.xterm_frame.pack(fill="both", expand=True)
        self.xterm_frame.update_idletasks()
    def display_false(self):
        self.xterm_frame.pack_forget()
        
if __name__=="__main__":
    root = tk.Tk()
    root.title("TkTerminal")
    root.geometry("700x600")
    app = Terminal(root)
    app.run()
    root.mainloop()
