from tkinter import *
from tkinter import filedialog
import example

class root(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("700x335")
        Label(self,text='Animal Classificator',font=('Arial',30)).pack(pady=15)
        bt = Button(self,text='Open',command=self.open,font=('Arial',14))
        bt.pack()
        self.lb = Listbox(self,width=80,height=1)
        self.lb.pack(pady=15)

        bt2 = Button(self,text='Predict',command=self.predict,font=('Arial',14))
        bt2.pack()

        self.txt = Label(self,font=('Arial',18),fg='blue')
        self.txt.pack(pady=20)
    def open(self):
        self.file = filedialog.askopenfilename()
        self.lb.delete(0,END)
        self.lb.insert(0,self.file)
        self.txt['text'] = ''
    def predict(self):
        animal = example.animal_class(self.file)
        self.txt['text'] = animal + ' !'

if __name__ == '__main__':
    r = root()
    r.mainloop()