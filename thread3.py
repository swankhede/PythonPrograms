from tkinter import *
import threading
import time
root =Tk()
root.title('example')
root.geometry("400x300+600+100")
class t1(threading.Thread):
    def run(self):
        print("entering into thread")
        for i in range(1,20):
            print(i)
            time.sleep(1)
obj1 = t1()
btn = Button(root,text="click me to start first  thread",command=obj1.start)

class t2(threading.Thread):
   def run(self):
       root.configure(background='darkslateblue')
           
        


obj2 = t2()
btn1 = Button(root,text="start second thread",command=obj2.start)
btn.pack()
btn1.pack()



root.mainloop()