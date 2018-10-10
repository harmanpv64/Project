     #       ---NOTE TAKING APP---

from tkinter import *                                     #import all tkinter functions
import sqlite3                                            #import all database libary functions
conn=sqlite3.connect('Note.db')                           #create the database with name note.db
#conn.execute("drop table Note")
#conn.execute("CREATE TABLE Note(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,CONTENT TEXT NOT NULL,PRIORITY NOT NULL);")
conn.commit()                                             #commit the table
master=Tk()                                               #take tk = master
master.title('Note Taking App')                           #make the title 'Note Taking'
frame1=Frame(master)                                      #create the frame
frame1.grid(row=0)                                        #create the frame in row = 0
frame2=Frame(master)                                      #create the frame
frame2.grid(row=2)                                        #create the frame in row = 2
frame3=Frame(master)                                      #create the frame
frame3.grid(row=1)                                        #create the frame in row = 1
frame4=Frame(master)                                      #create the frame
frame4.grid(row=4)                                        #create the frame in row = 4
frame5=Frame(master)                                      #create the frame
frame5.grid(row=4,column=2)                               #create the frame in row = 4 , column = 2

p = StringVar()                                           #used to check the data type

prio=IntVar()                                             #check for int data type


def add():                                               #define the add function
    top=Toplevel()                                       #define top in the add as objectt to call it
    top.title('Add New Notes')                           #give the title to the frame 1 'Add New Notes'
    fr=Frame(top)                                        #fr = frame at the top in 'Add New Notes' button
    fr.grid(row=3,column=0)                              #make a empty frame in row 3 and column 0
    e1 = Entry(top,width=45,textvariable=p)              #make a entry box for input as e1
    e1.grid(row=0,column=0)                              #e1 in row 0 column 0
    b1=Label(top,text='Add Name',width=15,bg='cyan',fg='black')            #make a lable b1 and name it as Add Name
    b1.grid(row=0,column=1)                                                #make the lable in row 0 column 1
    b2 =Label(top, text='Add PRIORITY', width=15, bg='cyan', fg='black')   #make lable b2 name it as Add PRIORITY
    b2.grid(row=1, column=1)                                               #make the lable in row 1 column 1

    e2 = Entry(top, width=45,textvariable=prio)           #make a entry box for input as e2
    e2.grid(row=1,column=0)                               #e2 in row 1 column 0
    lb=Label(top,text='Add Content',width=20)             #make a lable lb and name it as Add Content
    lb.grid(row=2,column=0)                               #lb in row 2 column 0

    scrollb = Scrollbar(fr, width=16)                    #make scrollbar by using the scrollb function
    scrollb.pack(side=RIGHT,fill=Y)                      #make the scrolbar on the right side
    scrollbar.config(command=myLis.yview)                #config the scrollbar put command mylist.yview to scroll list

    e3 = Text(fr, width=45,yscrollcommand=scrollb.set)     #make a entry box for input as e3
    e3.pack(side=LEFT,fill=BOTH)                           #e3 on left side

    c=Button(top, text='QUIT', width=15, height=2, bg='red', fg='white',command=top.destroy)  #create quit button
    c.grid(row=4, column=1)                                #c button  in row 4 column 1


    def save():                                            #create the save function
        x=str(p.get())                                     #check x
        m=prio.get()

        input = str(e3.get("1.0",END))                     #take the content of note
        conn.execute("INSERT INTO Note(NAME,CONTENT,PRIORITY)VALUES(?,?,?)",(x,input,m))    #execute
        conn.commit()                                                                       #commit
        top.destroy()                                                                       #destroy function
    br = Button(top, text='SAVE', width=15, height=2, bg='green', fg='orange',command=save).grid(row=4, column=0) #save button

button1=Button(frame1,text='Add New Notes>>',bg='red',width=25,height=2,fg='white',command=add).grid(row=0,column=0,padx=5,pady=10)  #Add New Notes botton
lbl=Label(frame3,text='Search Notes',height=3,width=20).grid(row=1,column=0)                                                         #create lable Search Notes
v=StringVar()                                                                  #check function to check datatype
e=Entry(frame2,width=45,textvariable=v).grid(row=2,column=0)                   #create entry box in row2 column 0
lb1=Label(master,text='-- Notes --',height=3,width=10).grid(row=3,column=0)    #create lable --Notes-- in row 3 column 0
scrollbar = Scrollbar(frame4, width=16)                                        #scrollbar function in frame 4
scrollbar.pack(side=RIGHT, fill=Y)                                             #pack (put) it on right side and y fill

myLis = Listbox(frame4, yscrollcommand=scrollbar.set,width=45)                 #create listbox by mylis
myLis.pack(side=LEFT, fill=BOTH)                                               #pack (put) it on left side and both(x,y) fill
scrollbar.config(command=myLis.yview)                                          #scrollbar function config command mylis to view the listbox


def liste():                                                                  #create the liste function
    myLis.delete(0,END)                                                       #delete funtion
    cursor=conn.execute("SELECT ID,NAME from Note")                           #execute the cursor
    for row in cursor:                                                        #apply for loop
        myLis.insert(END,str(row))                                            #insert in the mylis

    myLis.pack(side=LEFT, fill=BOTH)                                          #pack(put) it on left side and both(x,y) fill

    butt()                                                                    #button


def search():                                                            #define search function
    myLis.delete(0, END)                                                 #delete function
    z=str(v.get())                                                       #check the data type
    cursor = conn.execute("SELECT ID,NAME from Note where NAME=?",(z,))  #cussor execute
    for row in cursor:                                                   #apply the for loop
        myLis.insert(END, str(row))                                      #codition
    butt()                                                               #button


def dele():                                                              #define dele function
    del_id = myLis.get(myLis.curselection())                             #del id
    l = list(del_id.split(","))
    del_id = l[0][1:]
    conn.execute("DELETE FROM Note where ID=?", (del_id,))
    conn.commit()
    liste()
#    myLis.delete(0, END)


def Up():                                                        #define the up function
    del_id = myLis.get(myLis.curselection())
    top = Toplevel()
    top.title('Update Notes')                                    #title update notes
    fr = Frame(top)                                              #create the frame
    fr.grid(row=3, column=0)                                     #in row 3 column 0

    l = list(del_id.split(","))
    del_id=l[0][1:]

    vr=StringVar()
    vrr = StringVar()
    l=conn.execute("SELECT NAME,PRIORITY,CONTENT FROM Note where ID=?", (del_id,))

    for row in l:                                              #apply for loop
        x=row[0]
        y=row[1]
        z=row[2]

    e1 = Entry(top, width=45, textvariable=vr)                         #create the entry box e1
    vr.set(x)
    e1.grid(row=0, column=0)                                           #in row 0 column 0
    b1 = Label(top, text='Name', width=15, bg='cyan', fg='black')      #create the lable b1 'Name'
    b1.grid(row=0, column=1)                                           #in row 0 column 1
    b2 = Label(top, text='PRIORITY', width=15, bg='cyan', fg='black')  #create lable b2 'PRIORITY'
    b2.grid(row=1, column=1)                                           #in row 1 column 1

    e2 = Entry(top, width=45,textvariable=vrr)                         #create the entry box e2
    e2.grid(row=1, column=0)                                           #in row 1 column 0
    vrr.set(y)
    lb = Label(top, text='Content', width=20)                         #create a lable Content
    lb.grid(row=2, column=0)                                          #in row 2 column 0

    scrollb = Scrollbar(fr, width=16)                                 #scrollbar function
    scrollb.pack(side=RIGHT, fill=Y)                                  #pack it on right side
    scrollbar.config(command=myLis.yview)                             #put command in scrollbar
    e3 = Text(fr, width=45, yscrollcommand=scrollb.set)               #create the entry box e3
    e3.pack(side=LEFT, fill=BOTH)                                     #pack on left side

    e3.insert(INSERT,z)                                               #insert the entry box
    c = Button(top, text='QUIT', width=15, height=2, bg='red', fg='white', command=top.destroy)   #quit button to destroy
    c.grid(row=4, column=1)                                                                       #in row 4 column 1


    def save():                                                 #def save function
        x = str(vr.get())
        m = vrr.get()

        input = str(e3.get("1.0", END))                        #input
        conn.execute("INSERT INTO Note(NAME,CONTENT,PRIORITY)VALUES(?,?,?)", (x, input, m))
        conn.commit()                                           #commit
        top.destroy()                                           #destory command
        conn.execute("DELETE FROM Note where ID=?", (del_id,))  #execute
        conn.commit()                                           #commit

        liste()

    br = Button(top, text='SAVE', width=15, height=2, bg='green', fg='orange', command=save).grid(row=4, column=0)  #SAVE botton
    liste()


def redd():                                              #def redd function
    del_id = myLis.get(myLis.curselection())
    l = list(del_id.split(","))
    del_id=l[0][1:]
    print(l)
    l=conn.execute("SELECT NAME,PRIORITY,CONTENT FROM Note where ID=?", (del_id,))
    for row in l:
        z=row[2]

    top = Toplevel()
    fr = Frame(top)
    fr.grid(row=1, column=0)

    top.title('Read Notes')                                   #title read notes
    lb = Label(top, text='Content', width=20)                 #lable
    lb.grid(row=0, column=0)                                  #row 0 column 0

    scrollb = Scrollbar(fr, width=16)                         #scrollbar function
    scrollb.pack(side=RIGHT, fill=Y)                          #pack scrollbar
    scrollbar.config(command=myLis.yview)                     #command configure

    e3 = Text(fr, width=45, yscrollcommand=scrollb.set)       #entry box
    e3.pack(side=LEFT, fill=BOTH)                             #pack the entry box

    e3.insert(INSERT,z)
    c = Button(top, text='QUIT', width=15, height=2, bg='red', fg='white', command=top.destroy)     #quit button
    c.grid(row=4, column=0)                                                                         #pack button


def sot():                                                     #def sort function
    myLis.delete(0, END)
    cursor=conn.execute("SELECT ID,NAME FROM Note ORDER BY PRIORITY ASC")
    for row in cursor:                                          #apply for loop
        myLis.insert(END, str(row))


def butt():                                                                                      #def button function
    b = Button(frame5, text='Update', bg='light blue', fg='red', command=Up).grid(row=5,column=2)   #update button pack

    c = Button(frame5, text='Delete', bg='light blue', fg='red', command=dele).grid(row=6,column=2) #delete button pack

    d = Button(frame5,  text='Read',  bg='light blue', fg='red', command=redd).grid(row=4,column=2)   #read button pack

    e=Button(frame5,    text='Sort',  bg='light blue', fg='red', command=sot).grid(row=3,column=2)      #sort button pack

button2=Button(frame1,text='List All Notes',bg='red',width=25,height=2,fg='white',command=liste).grid(row=0,column=1,padx=5,pady=10)  #button List All Notes pack
button3=Button(frame2,text='Search',bg='red',width=10,height=1,fg='white',command=search).grid(row=2,column=1)                        #button Search pack

mainloop()