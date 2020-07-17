from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect('database.db')
cur=con.cursor()
class Addpeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("Add People")
        self.resizable('false', 'false')

        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=600, bg='#abd8eb')
        self.bottom.pack(fill=X)
        # top_frame_design
        self.top_image = PhotoImage(file='icon/add.png')
        # bg is white by default and putting img on top frame
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=30, y=25)
        # creating label for heading
        self.heading = Label(self.top, text="Add People", font="arial 16 bold", bg="white", fg="#f57e42")
        self.heading.place(x=120, y=40)

        #name
        self.label_fname=Label(self.bottom, text='First Name:', font='arial 12 bold', fg='#ffffff',bg='#0d1137', width=15)
        self.label_fname.place(x=40, y=40)
        self.entry_fname=Entry(self.bottom, width=30, border=4)
        self.entry_fname.insert(0, 'Enter first Name')
        self.entry_fname.place(x=200, y=40)

        #last_name
        self.label_lname = Label(self.bottom, text='Last Name:', font='arial 12 bold', fg='#ffffff', bg='#0d1137', width=15)
        self.label_lname.place(x=40, y=80)
        self.entry_lname = Entry(self.bottom, width=30, border=4)
        self.entry_lname.insert(0, 'Enter last Name')
        self.entry_lname.place(x=200, y=80)

        #phone_number
        self.label_number = Label(self.bottom, text='Phone Number:', font='arial 12 bold', fg='#ffffff', bg='#0d1137', width=15)
        self.label_number.place(x=40, y=120)
        self.entry_number = Entry(self.bottom, width=30, border=4)
        self.entry_number.insert(0, 'Enter Number')
        self.entry_number.place(x=200, y=120)

        # email
        self.label_email = Label(self.bottom, text='Email Address:', font='arial 12 bold', fg='#ffffff', bg='#0d1137', width=15)
        self.label_email.place(x=40, y=160)
        self.entry_email = Entry(self.bottom, width=30, border=4)
        self.entry_email.insert(0, 'Enter email address')
        self.entry_email.place(x=200, y=160)

        # address
        self.label_address = Label(self.bottom, text='Address:', font='arial 12 bold', fg='#ffffff', bg='#0d1137', width=15)
        self.label_address.place(x=40, y=200)
        self.entry_address = Text(self.bottom, width=35, height=15)
        self.entry_address.place(x=200, y=200)

        #submit
        self.submitbutton=Button(self.bottom, text='SUBMIT', font='arial 12 bold', fg='#ffffff', bg='#0d1137', command=self.add_people)
        self.submitbutton.place(x=270, y=460)

    def add_people(self):
        first_name = self.entry_fname.get()
        last_name = self.entry_lname.get()
        phone = self.entry_number.get()
        email = self.entry_email.get()
        address = self.entry_address.get(1.0, 'end-1c')

        if first_name and last_name and email and phone and address!="":
            try:
                #add to database
                #insert into addressbook(person_id, person_fname, person_lname, person_email, person_phone , person_address
                #id is autoincreamented
                query = "insert into 'addressbook'(person_fname, person_lname, person_email, person_phone , person_address) values(?,?,?,?,?)"
                cur.execute(query, (first_name, last_name, email, phone, address))
                con.commit()
                messagebox.showinfo("SUCCESS","CONTACT ADDED!!")
                self.destroy()
            except EXCEPTION as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error","FILL ALL THE FIELDS", icon="warning")