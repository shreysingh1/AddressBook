from tkinter import *
import sqlite3
from addpeople import Addpeople
from updatepeople import Update
from display import Display
from tkinter import messagebox

con=sqlite3.connect('database.db')
cur=con.cursor()
class Mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("500x550+650+100")
        self.title("My People")
        self.resizable('false', 'false')
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg='#abd8eb')
        self.bottom.pack(fill=X)
        # top_frame_design
        self.top_image = PhotoImage(file='icon/ppl.png.')
        # bg is white by default and putting img on top frame
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=30, y=25)
        # creating label for heading
        self.heading = Label(self.top, text="My People", font="arial 16 bold", bg="white", fg="#f57e42")
        self.heading.place(x=120, y=40)

        #adding scrollbar and Listbox
        self.scroll = Scrollbar(self.bottom,orient =VERTICAL)
        #setting up the scrollbar on listbox
        self.listBox = Listbox(self.bottom , width=40 , height=30)
        self.listBox.grid(row=0, column=0 , padx=(40,0))
        self.scroll.config(command= self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll)
        self.scroll.grid(row=0 , column=1, sticky=N+S)
        self.listBox.config(yscrollcommand=self.scroll.set)

        persons  = cur.execute("select * from 'addressbook'")
        print(persons)
        count= 0
        for person in persons:
            self.listBox.insert(count, str(person[0])+ ".  "+person[1] +"  "+person[2])
            count+=1


        #button
        self.btnadd=Button(self.bottom, text='Add', width=12, font='sans 12 bold', command=self.add_people)
        self.btnadd.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        self.btnupdt = Button(self.bottom, text='Update', width=12, font='sans 12 bold', command=self.update_func)
        self.btnupdt.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        self.btndisp = Button(self.bottom, text='Display', width=12, font='sans 12 bold', command = self.display_func)
        self.btndisp.grid(row=0, column=2, padx=20, pady=90, sticky=N)

        self.btndel = Button(self.bottom, text='Delete', width=12, font='sans 12 bold', command=self.delete_func)
        self.btndel.grid(row=0, column=2, padx=20, pady=130, sticky=N)



    def add_people(self):
        add_page=Addpeople()
        self.destroy()

    def update_func(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        updatepage=Update(person_id)

    def display_func(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        displaypage=Display(person_id)

    def delete_func(self):
        selected_item = self.listBox.curselection()
        person = self.listBox.get(selected_item)
        person_id = person.split(".")[0]
        query="delete from 'addressbook' where person_id={}".format(person_id)
        string_for_mbox= person.split(".")[1]
        answer= messagebox.askquestion("WARNING",f"Do You Want To delete{string_for_mbox},Contact?")
        if answer == 'yes':
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("SUCCESS","Deleted Successfully!!")
                self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Info", str(e))


