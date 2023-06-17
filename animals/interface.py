from tkinter import *
from tkinter import filedialog
import test_file
import numpy as np

animals = ['Borboleta','Galinha','Elefante','Cavalo','Aranha','Esquilo']

class root(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("700x500")
        Label(self,text='Animal Classificator',font=('Arial',40)).pack(pady=15)
        bt = Button(self,text='Open',command=self.open,font=('Arial',20))
        bt.pack()
        self.lb = Listbox(self,width=80,height=1)
        self.lb.pack(pady=15)

        bt2 = Button(self,text='Predict',command=self.predict,font=('Arial',20))
        bt2.pack()

        self.txt0 = Label(self,font=('Arial',24),fg='blue')
        self.txt0.pack(pady=15)
        
        self.txt = {}
        
        self.txt[0] = Label(self,font=('Arial',12))
        self.txt[0].pack(pady=1)
        self.txt[1] = Label(self,font=('Arial',12))
        self.txt[1].pack(pady=1)    
        self.txt[2] = Label(self,font=('Arial',12))
        self.txt[2].pack(pady=1)
        self.txt[3] = Label(self,font=('Arial',12))
        self.txt[3].pack(pady=1)
        self.txt[4] = Label(self,font=('Arial',12))
        self.txt[4].pack(pady=1)
        self.txt[5] = Label(self,font=('Arial',12))
        self.txt[5].pack(pady=1)    
        
    def open(self):
        self.file = filedialog.askopenfilename()
        self.lb.delete(0,END)
        self.lb.insert(0,self.file)
        self.txt0['text'] = ''
        for t in self.txt:
            t['text'] = ''
        
        
    def predict(self):
        pred  = test_file.animal_class(self.file)
        
        i = np.where(pred[0] == pred[0].max())[0]
        
        #print(int(i))
        #print(pred[0])
        #print(animals)
        self.txt0['text'] = "{} !".format(animals[int(i)])
        
        
        
        for j,(p,a) in enumerate(zip(pred[0],animals)):
            self.txt[j]['text'] = "{} --> {:.4f}".format(a,p)
        
        







if __name__ == '__main__':
    r = root()
    r.mainloop()