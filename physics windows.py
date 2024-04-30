import tkinter
import time
import threading
print("starting")
class window_handler:
    def __init__(self) -> None:
        self.windows = {}
    def new_window(self,name):#send a string with the window name and returns the root object back
        window_container = {"root":tkinter.Tk()}
        window_container["root"].title(name)
        self.windows[name] = window_container
        self.update_windows()
        return window_container["root"]
    def delete_window(self,name):
        self.windows[name]["root"].destroy()
    def update_windows(self):#since tkinter hates threading ima have to update the windows within the main thread
        try:
            for i in self.windows:
                self.windows[i]["root"].update()
        except Exception as problem:
            print("problem with the window update")
            print(problem)
    def move_window(self,name,x,y):
        root = self.windows[name]["root"]
        root.geometry("+"+str(root.winfo_x()+x)+"+"+str(root.winfo_y()+y))
class main(window_handler):
    def __init__(self) -> None:
        super().__init__()
        win1root = self.new_window("window 1")
        win2root = self.new_window("window 2")
        win3root = self.new_window("window 3")
        self.windows["window 1"]["button"] = tkinter.Button(win1root,text="button",command=self.trigger1)
        self.windows["window 1"]["button"].pack()
        self.windows["window 3"]["button"] = tkinter.Button(win3root,text="button",command=self.trigger2)
        self.windows["window 3"]["button"].pack()
        self.windows["window 2"]["text"] = tkinter.Button(win2root,text="move down 10",command=lambda:self.move_window("window 2",0,10))
        self.windows["window 2"]["text"].pack()
        self.mainloop()
    def trigger1(self):
        for i in range(10):
            self.delete_window(str(i))
    def trigger2(self):
        for i in range(10):
            self.new_window(str(i))
    def mainloop(self):
        while True:
            self.update_windows()
main()
