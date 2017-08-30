import tkinter as tk
from tkinter import BOTH, X, Y
from DataProcessor import DataProcessor
from PIL import Image, ImageTk

class PyStation(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.login_processor = None
        self.login_panel = self.build_login_panel()

    def build_login_panel(self):
        frame = tk.Frame(self)
        frame.pack(expand=1, fill=BOTH)

        self.logo_panel = self.build_logo_panel(frame)
        self.entry_panel = self.build_entry_panel(frame)

        return frame

    def build_logo_panel(self, parent):
        frame = tk.Frame(parent)
        frame.configure(background="#000000")
        frame.pack(expand=1, fill=X , side="top")

        self.logo = ImageTk.PhotoImage(Image.open("C:/Users/JakeT/onedrive/documents/visual studio 2017/Projects/PyStation/PyStation/static/images/rcr-logo-dark.png"))
        tk.Label(frame, image=self.logo, fg="#0B3D91", bg="#000000").pack(fill="both", expand="yes")
        print(self.logo)

        return frame

    def build_entry_panel(self, parent):
        frame = tk.Frame(parent)
        frame.configure(background="#000000")
        frame.pack(expand=1, fill=X, side="bottom")

        self.build_entry_column("left", frame)
        self.build_entry_column("right", frame)

        self.login_button = tk.Button(frame, text="login", command=self.login, fg="#FFF", bg="#000000")
        self.login_button.config(height=2, width=9)
        self.login_button.pack(side="bottom")

        return frame

    def build_entry_column(self, side, parent):
        column = tk.Frame(parent)
        column.pack(side="left")
        column.configure(background="black")

        if side == "left":
            self.username_label = tk.Label(column, text="username:", fg="#FFF", bg="#000000")
            self.password_label = tk.Label(column, text="password:", fg="#FFF", bg="#000000")

            self.username_label.pack(side="top")
            self.password_label.pack(side="top")
        else:
            self.username_entry = tk.Entry(column)
            self.password_entry = tk.Entry(column)

            self.username_entry.pack(side="top")
            self.password_entry.pack(side="top")
        return column

    def login(self):
        username_input = self.username_entry.get()
        password_input = self.password_entry.get()
        self.login_processor = DataProcessor(file_path="C:/Users/JakeT/onedrive/documents/visual studio 2017/Projects/PyStation/PyStation/static/config/users.csv")
        database = self.login_processor.data

        for entry in database:
            print(entry, "entry")
            print(type(entry), "type(entry)")
            print(entry[0], "entry[0]")
            print(entry[1], "entry[1]")
            if username_input == entry[0] and password_input == entry[1]:
                print("CORRECT USERNAME AND PASSWORD")
#            print(entry,"value")
 #           print(type(entry),"type")

        print(self.login_processor)

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
    processor = DataProcessor()
#    processor.main()