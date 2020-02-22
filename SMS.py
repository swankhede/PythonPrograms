from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import bs4
import tkinter.font as font
import requests
import socket
import cx_Oracle
import math
fr = Tk()
fr.title("student management")
fr.configure(background='#E63462')
fr.geometry("700x700+600+100")
myfont = font.Font(size=20,family='consolas')
def f1(n):
        if n == 1: 
            #print("hello world")
            add = Tk()
            fr.withdraw()
            add.title("add")
            add.geometry("700x700+600+100")
            add.configure(background='#E63462')
           
            def func():
                flag = None
                try:
                    n = int(t1.get())
                    if n<0:
                        messagebox.showerror("error","pls enter valid +ve numbers only")
                        t1.delete(0,END)
                        t1.focus_force()
                        flag=1
                except ValueError as e :
                    
                    
                    msg="invalid value:numbers only"
                    messagebox.showerror("intergers only",msg)
                    t1.delete(0,END)
                    t1.focus_force()
                    flag=1

                
              
                
                
                try:
                    n2 = int(t3.get())
                    
                    if n2<0 or n2>100:
                        messagebox.showerror("error","marks must be between 0 to 100")
                        t3.delete(0,END)
                        t3.focus_force()
                        flag=1
                except ValueError as e :
                    
                    
                    msg="invalid value:marks must be numbers only"
                    messagebox.showerror("intergers only",msg)
                    t3.delete(0,END)
                    t3.focus_force()
                    flag=1
                
                t =t2.get()  
                if t.isalpha() ==False:
                        messagebox.showerror("error","pls enter valid name")
                        t2.delete(0,END)
                        t2.focus_force()
                        flag=1
                else:
                    if len(t)<2:
                        messagebox.showerror("error","name should be 2 character long")
                        t2.delete(0,END)
                        t2.focus_force()
                        flag=1
                                
                try:
                    con=None
                    con = cx_Oracle.connect('system/123')
                    print("connected")
                    #print(flag)
                                    
                    if flag is None:
                        print("everthing is ok")
                        
                       
                        cursor =con.cursor()
                        sql = "insert into students values('%d','%s','%d')"
                        args=(n,t,n2)
                        cursor.execute(sql % args)
                        con.commit()
         
                        messagebox.showinfo("success",str(cursor.rowcount) + "inserted")
                        t1.delete(0,END)
                        t2.delete(0,END)
                        t3.delete(0,END)
                        t1.focus_force()
                except cx_Oracle.DatabaseError as e:
                    con.rollback()
                    print("issue: ",e)
                    messagebox.showerror("failure",e)
                    t1.delete(0,END)
                    t1.focus_force()
                    flag=1
                       
                    
                    
                except TypeError as e:
                    con.rollback()
                    msg="invalid value:string only"
                    messagebox.showerror("string only",msg)
                    t2.delete(0,END)
                    t2.focus_force()
                    flag=1
                
                    
                finally:
                    
                    if con is not None:
                        con.close()
                    print("u r are disconnected....")
                        
                        
                
            
               

            def back():
                #print("back")
                fr.deiconify()
                add.withdraw()
            lbl1 = Label(add,text="Enter roll no",bg="#E63462")
            lbl1['font']=font.Font(size='11')
            t1 = Entry(add,width='30')
            lbl2 = Label(add,text="Enter name",bg="#E63462")
            lbl2['font']=font.Font(size='11')
            t2 = Entry(add,width='30')
            lbl3 = Label(add,text="Enter marks",bg="#E63462")
            lbl3['font']=font.Font(size='11')
            t3 = Entry(add,width='30')
            
            sv = Button(add,text="Save",bg='#333745',fg='white',width='20',height='2',command=func)
        
            back = Button(add,text="Back",bg='#333745',fg='white',width='20',height='2',command=back)
            lbl1.pack(pady=20)
            t1.pack(pady=20)
            lbl2.pack(pady=20)
            t2.pack(pady=20)
            lbl3.pack(pady=20)
            t3.pack(pady=20)
            sv.pack(pady=10)
            back.pack(pady=10)
        
        if n == 2:
            try:
                con=None
                con = cx_Oracle.connect('system/123')
                print("connected")
                #print("hello world")
                add = Tk()
                fr.withdraw()
                add.title("view")
                add.geometry("700x700+600+100")
                add.configure(background='#E63462')
                def back():
                    #print("back")
                    fr.deiconify()
                    add.withdraw()

        
                t1 =scrolledtext.ScrolledText(add)
                
            
            
                back = Button(add,text="Back",bg='#333745',fg='white',width='20',height='2',command=back)
            
                t1.pack(pady=20)
                
            
                back.pack(pady=10)
                cursor=con.cursor()
                sql = "select * from students"
                cursor.execute(sql)
                data= cursor.fetchall()
                mdata=""
                for d in data:
                    mdata=mdata+str(d[0])+" "+d[1]+" "+str(d[2])+"\n"
                t1.insert(INSERT,mdata)
                t1['state']='disable'
            except cx_Oracle.DatabaseError as e:
                    con.rollback()
                    print("issue: ",e)
                    messagebox.showerror("failure",e)
                    t2.delete(0,END)
                    t2.focus_force()
            finally:
                    if cursor is not None:
                        cursor.close()
                    if con is not None:
                        con.close()
                    print("u r are disconnected....")
            
               
                

        
                         
           
      
            
        if n==3:
            
            add = Tk()
            fr.withdraw()
            add.title("update")
            add.geometry("700x700+600+100")
            add.configure(background='#E63462')
            
            def func():
                flag = None
                try:
                    n = int(t1.get())
                    if n<0:
                        messagebox.showerror("error","pls enter valid +ve numbers only")
                        t1.delete(0,END)
                        t1.focus_force()
                        flag=1
                except ValueError as e :
                    
                    
                    msg="invalid value:numbers only"
                    messagebox.showerror("intergers only",msg)
                    t1.delete(0,END)
                    t1.focus_force()
                    flag=1

                
              
                
                
                try:
                    n2 = int(t3.get())
                    
                    if n2<0 or n2>100:
                        messagebox.showerror("error","marks must be between 0 to 100")
                        t3.delete(0,END)
                        t3.focus_force()
                        flag=1
                except ValueError as e :
                    
                    
                    msg="invalid value:marks must be numbers only"
                    messagebox.showerror("intergers only",msg)
                    t3.delete(0,END)
                    t3.focus_force()
                    flag=1
                
                t =t2.get()  
                if t.isalpha() ==False:
                        messagebox.showerror("error","pls enter valid name")
                        t2.delete(0,END)
                        t2.focus_force()
                        flag=1
                else:
                    if len(t)<2:
                        messagebox.showerror("error","name should be 2 character long")
                        t2.delete(0,END)
                        t2.focus_force()
                        flag=1
                                
                
                
                    try:
                        con = cx_Oracle.connect('system/123')
                        print("connected")  
                        if flag is None:

                            print("everthing is ok")
                            cursor = con.cursor()
                            sql ="update students SET rollno='%d',name='%s',marks='%d' where rollno='%d'"
                            args=(n,t,n2,n)
                            cursor.execute(sql % args)
                            if cursor.rowcount==0:
                                msg="roll number doesn't exist"
                                messagebox.showerror("issue",msg)
                                t1.delete(0,END)
                                t1.focus_force()

                            else:
                                con.commit()
                                messagebox.showinfo("success",str(cursor.rowcount) + "updated")
                                t1.delete(0,END)
                                t2.delete(0,END)
                                t3.delete(0,END)
                                t1.focus_force()
                                        
                    except cx_Oracle.DatabaseError as e:
                        con.rollback()
                        print("issue: ",e)
                        messagebox.showerror("failure",e)
                        t1.delete(0,END)
                        t1.focus_force()
                    
                    
                    except TypeError as e:
                        con.rollback()
                        msg="invalid value:string only"
                        t.delete(0,END)
                        t.focus_force()
                        messagebox.showerror("string only",msg)
                    finally:
                    
                        if con is not None:
                            con.close()
                        print("u r are disconnected....")    
                        
                
                                        
                        
                
            
               

            def back():
                #print("back")
                fr.deiconify()
                add.withdraw()
            lbl1 = Label(add,text="Enter roll no",bg="#E63462")
            lbl1['font']=font.Font(size='11')
            t1 = Entry(add,width='30')
            lbl2 = Label(add,text="Enter name",bg="#E63462")
            lbl2['font']=font.Font(size='11')
            t2 = Entry(add,width='30')
            lbl3 = Label(add,text="Enter marks",bg="#E63462")
            lbl3['font']=font.Font(size='11')
            t3 = Entry(add,width='30')
            
            sv = Button(add,text="Save",bg='#333745',fg='white',width='20',height='2',command=func)
        
            back = Button(add,text="Back",bg='#333745',fg='white',width='20',height='2',command=back)
            lbl1.pack(pady=20)
            t1.pack(pady=20)
            lbl2.pack(pady=20)
            t2.pack(pady=20)
            lbl3.pack(pady=20)
            t3.pack(pady=20)
            sv.pack(pady=10)
            back.pack(pady=10)

        if n == 4:
            con = cx_Oracle.connect('system/123')
            print("connected")
            print("hello world")
            add = Tk()
            fr.withdraw()
            add.title("delete")
            add.geometry("700x700+600+100")
            add.configure(background='#E63462')
            def func():
                try:
                    n = int(t1.get())
                    cursor =con.cursor()
                    sql2="select count(*) from students where rollno = %d"
                    args1=n
                    cursor.execute(sql2 % args1)
             
                    result = cursor.fetchone()
                    for i in result:
                        #print(i)
                        if i == 0:
                              messagebox.showerror("error","roll no does not exists")
                              t1.delete(0,END)
                              t1.focus_force()
                            

                        else:
                            sql="delete  from students where rollno = %d "
                            args=n
                            cursor.execute(sql % args)
                            con.commit()
                            msg = "rollno:"+ str(n) +"deleted"
                            messagebox.showinfo("deleted", msg)
                            t1.delete(0,END)
                            t1.focus_force()
                except ValueError:
                    messagebox.showerror("error","pls enter valid numbers only")
                    t1.delete(0,END)
                    t1.focus_force()

                   
                
                

            def back():
                #print("back")
                fr.deiconify()
                add.withdraw()
            lbl1 = Label(add,text="Enter roll no",bg="#E63462")
            lbl1['font']=font.Font(size='11')
            t1 = Entry(add,width='30')
        
        
            delete = Button(add,text="Delete" ,bg='#333745',fg='white',width='20',height='2',command=func)
            back = Button(add,text="Back",bg='#333745',fg='white',width='20',height='2',command=back)
            lbl1.pack(pady=20)
            
            t1.pack(pady=20)
            delete.pack(pady=20)
            back.pack(pady=10)
            

        if n == 5:
            try:
                
                #print("hello world")
                add = Tk()
                fr.withdraw()
                add.title("graph")
                add.geometry("700x700+600+100")
                add.configure(background='#E63462')
                con = cx_Oracle.connect('system/123')
                #print("connected") 
                
                def back():
                    #print("back")
                    fr.deiconify()
                    add.withdraw()
                def graph(n):
                    from matplotlib import pyplot as plt
                    import numpy as np
                    
                    cursor = con.cursor()
                    sql = "select * from students"
                    
                    row = cursor.execute(sql)
                    list1 =[]
                    list2=[]
                    for i in row:
                        #print(i[1],i[2])
                        list1.append(i[1])
                        list2.append(i[2])
                        #print(list1,list2)
                    if n== 1:
                        plt.title("students marks")
                        x = np.arange(len(list1))
                        plt.bar(x,list2)
                        plt.xticks(x,list1)
                        plt.xlabel("students")
                        plt.ylabel("marks")
                        plt.grid()
                        plt.show()
                        #print("bar")
                    if n==2:
                        plt.plot(list1,list2)
                        plt.xlabel('students')
                        plt.ylabel('marks')
                        plt.title("students marks")
                        
                        plt.grid()
                        plt.show()
                        #print("line")
                
            except cx_Oracle.DatabaseError as e:
                    
                    print("issue: ",e)
                    messagebox.showerror("failure",e)
                    
            finally:
                    
                    if con is None:
                        con.close()
                        #print("u r are disconnected....")   
            sv = Button(add,text="Bar",bg='#333745',fg='white',width='20',height='2',command=lambda:graph(1))
            line = Button(add,text="Line",bg='#333745',fg='white',width='20',height='2',command=lambda:graph(2))
            back = Button(add,text="Back",bg='#333745',fg='white',width='20',height='2',command=back)
            sv.pack(pady=10)
            line.pack(pady=10)
            back.pack(pady=10)
                    


btn1 = Button(fr,text="ADD" ,bg='#333745',fg='white',width='20',height='2',command=lambda:f1(1))
btn2 = Button(fr,text="VIEW" ,bg='#333745',fg='white',width='20',height='2',command=lambda:f1(2))
btn3 = Button(fr,text="UPDATE" ,bg='#333745',fg='white',width='20',height='2',command=lambda:f1(3))
btn4 = Button(fr,text="DELETE", bg='#333745',fg='white',width='20',height='2',command=lambda:f1(4))
btn5 = Button(fr,text="GRAPH" ,bg='#333745',fg='white',width='20',height='2',command=lambda:f1(5))



btn1.pack(pady=30)
btn2.pack(pady=30)
btn3.pack(pady=30)
btn4.pack(pady=30)
btn5.pack(pady=30)
try:
        res=requests.get("http://www.brainyquote.com/quotes_of_the_day.html")
        print(res)
        soup=bs4.BeautifulSoup(res.text,'lxml')
        quote=soup.find('img',{"class":"p-qotd"})
     
        text=quote['alt']
        label = Label(fr,text=text)
        label.pack()
        

        socket.create_connection(("www.google.com",80))
        print("u r connected")
        city ='thane'
        a1 = "http://api.openweathermap.org/data/2.5/weather?"

        a2 = "q=" +city + "&units=metric"
        a3 = "&APPID=fa531e4e62b7ffeb91c7ea854ddf347a"
        api_address = a1+a2+a3
        res1 = requests.get(api_address)
        print(res1)
        
        d = res1.json()
        
        d1=d['main']['temp']
        temp = 'Thane(current temperature): '+str(d1)
        
        label2 = Label(fr,text=temp)
        label2.pack(pady=10)
	
	
except OSError as e:
        messagebox.showerror('issue',e)
        print("issue ",e)
        


fr.mainloop()            

        
	
    
        
    
    
    



