import tkinter as tk
from tkinter import BOTH, X, Y

class PyStation(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.login_panel = self.build_login_panel()

    def build_login_panel(self):
        frame = tk.Frame(self)
        frame.pack(expand=1, fill=BOTH)

        self.logo_panel = self.build_logo_panel(frame)
        self.entry_panel = self.build_entry_panel(frame)

        return frame

    def build_logo_panel(self, parent):
        frame = tk.Frame(parent)
        frame.pack(expand=1, fill=X , side="top")

#        self.logo = tk.Image()

        return frame

    def build_entry_panel(self, parent):
        frame = tk.Frame(parent)
        frame.pack(expand=1, fill=X, side="bottom")

        self.login_button = tk.Button(frame, text="login", command=self.test_command)
        self.login_button.config(height=3, width=9)
        self.login_button.pack(side="bottom")

        return frame

    def test_command(self):
        print("test")

def main():
    root = tk.Tk()
    root.title("Ground Station")
    root.geometry("1200x900")
    root.configure(background="#000000")
    application = PyStation(master=root)
    application.mainloop()
    root.destory()

if __name__ == '__main__':
    main()