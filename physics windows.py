import tkinter
import time
import threading
print("starting")
class window_handler:
    def __init__(self) -> None:
        self.windows = {}
    def new_window(self,name):#send a string with the window name
        window_container = {"root":tkinter.Tk()}
        window_container["root"].title(name)
        self.windows[name] = window_container
        self.update_windows()
    def update_windows(self):#since tkinter hates threading ima have to update the windows within the main thread
        for i in self.windows:
            self.windows[i]["root"].update()
class main(window_handler):
    def __init__(self) -> None:
        super().__init__()
        self.new_window("window 1")
        self.new_window("window 2")
        self.new_window("window 3")
        self.windows["window 1"]["button"] = tkinter.Button(self.windows["window 1"]["root"],text="button",command=self.trigger1)
        self.windows["window 1"]["button"].pack()
        self.windows["window 3"]["button"] = tkinter.Button(self.windows["window 3"]["root"],text="button",command=self.trigger2)
        self.windows["window 3"]["button"].pack()
        self.windows["window 2"]["text"] = tkinter.Text(self.windows["window 2"]["root"])
        self.windows["window 2"]["text"].pack()
        self.mainloop()
    def trigger1(self):
        self.windows["window 2"]["text"].insert(tkinter.END,"based\n")
    def trigger2(self):
        self.windows["window 2"]["text"].insert(tkinter.END,"cringe\n")
    def mainloop(self):
        while True:
            self.update_windows()
main()
