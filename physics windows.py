import tkinter
import time
import threading
import random
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
        self.lock_wait()
        self.windows[name]["root"].destroy()
        self.windows.pop(name)
    def update_windows(self):#since tkinter hates threading ima have to update the windows within the main thread
        try:
            for i in self.windows:
                self.windows[i]["root"].update()
        except Exception as problem:
            print("problem with the window update")
            print(problem)
    def move_window(self,name,x,y):#supply the name and position to move it by (not to)
        try:
            root = self.windows[name]["root"]
            y = y-32 #weird bug where the .geometry() function y position is skewed by an extra 32. could be to do with the top window bar??????
            root.geometry("+"+str(root.winfo_x()+x)+"+"+str(root.winfo_y()+y))
        except Exception as problem:
            print(problem)
    def lock_dictionary(self):#creates a lock variable so that the dictionary can be prevented from being modifyed
        self.lock = True
    def unlock_dictionary(self):
        self.lock = False
    def lock_wait(self):#waits for the lock to release before continuing
        while self.lock:
            pass
class main(window_handler):
    def __init__(self) -> None:
        super().__init__()
        for i in range(10):
            i = str(i)
            root = self.new_window(i)
            self.windows[i]["button"] = tkinter.Button(root,text="kill",command=lambda i=i:self.delete_window(i))
            self.windows[i]["button"].pack()
        print(self.windows)
        self.mainloop()
    def mainloop(self):
        while True:
            self.lock_dictionary()
            for i in self.windows:
                self.move_window(i,random.randint(-1,1),random.randint(-1,1))
            self.unlock_dictionary()
            self.update_windows()
main()
