from tkinter import *
import datetime
from mypeople import Mypeople
from addpeople import Addpeople

date = datetime.datetime.now().date()

date = str(date)
class Application(object):
    def __init__(self, master):
        # frames
        self.master = master
        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(master, height=500, bg='#abd8eb')
        self.bottom.pack(fill=X)
        # top_frame_design
        self.top_image = PhotoImage(file='icon/pb.png')
        # bg is white by default and putting img on top frame
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=25, y=25)
        # creating label for heading
        self.heading = Label(self.top, text="My PhoneBook App", font="arial 16 bold", bg="white", fg="#f57e42")
        self.heading.place(x=180, y=40)
        self.date_label = Label(self.top, text="Today's date:" + date, font="arial 12 bold", bg="white", fg="#f57e42")
        self.date_label.place(x=300, y=125)
        # creating button to perform operations such as add

        # button1->add
        self.addButton = Button(self.bottom, text="Add Person", fg="black",bg="white",font="arial 12 bold", width="10", command=self.addpeoplefunction)
        self.addButton.place(x=200, y=30)
        # button2->view
        self.viewButton = Button(self.bottom, text="My People", fg="black",bg="white",font="arial 12 bold", width="11", command=self.my_people)
        self.viewButton.place(x=200, y=80)
        # button3->about
        self.aboutButton = Button(self.bottom, text="About Us", fg="black",bg="white",font="arial 12 bold", width="10")
        self.aboutButton.place(x=200, y=130)
    def my_people(self):
        people=Mypeople()
    def addpeoplefunction(self):
        addpeoplewindow = Addpeople( )


# creating main class to design the main GUI
def main():
    root = Tk()
    app = Application(root)
    root.title("Phonebook App")
    root.geometry("500x550+350+200")
    root.resizable('false', 'false')
    root.mainloop()

#whenever someone call this program the main function should be invoked
if __name__ == '__main__':
    main()