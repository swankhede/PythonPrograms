from tkinter import *
import time
import threading

root = Tk()
root.geometry('300x400+600+100')
root.title("reminder")
lbl = Label(root,text='type note here')
note = Text(root)

class t1(threading.Thread):
    
   def run(self):
       root.withdraw()
       for i in range(1,5):
        print(i)
        time.sleep(1)

        if i == 4:
            root.deiconify()
            #self.start()


    


obj1 = t1()
btn = Button(root,text='save' ,command=obj1.start)
lbl.pack()

note.pack()
btn.pack()
root.mainloop()
