class DataProcessor(object):
    def __init__(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def load_data(self, file_path):
        pass

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