from tkinter import *
from tkinter import filedialog
#import test_file
import numpy as np
from PIL import ImageTk, Image

from tools import predict

animals = ['Borboleta','Galinha','Elefante','Cavalo','Aranha','Esquilo']

class root(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("700x500")
        Label(self,text='Classificação de Animais',font=('Arial',40)).pack(pady=15)
        
        bt = Button(self,text='Submeter imagem',command=self.open,font=('Arial',20))
        bt.pack()

        self.img_label = Label(self)
        self.img_label.pack(pady=15)



        self.txt0 = Label(self,font=('Arial',24),fg='blue')
        self.txt0.pack(pady=5)
        
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
        filename = filedialog.askopenfilename()
        if not filename:
            return


        
        img = Image.open(filename).resize((80,80))
        img.save('temp.jpg')
    
        img_tk = ImageTk.PhotoImage(img)

        self.img_label.configure(image = img_tk)
        self.img_label.image = img_tk
        


        pred = predict(filename)
        i = pred.index(max(pred))

        self.txt0['text'] = "{} !".format(animals[i])
        
        for j,(a, p) in enumerate(zip(animals, pred)):
            self.txt[j]['text'] = f"{a} --> {p*100:.2f} %"#.format(a,p)
        
        

#        self.txt0['text'] = ''
#        for t in self.txt:
#            t['text'] = ''
        
        
    # def predict(self):
    #     pred  = test_file.animal_class(self.file)
        
    #     i = np.where(pred[0] == pred[0].max())[0]
        
    #     #print(int(i))
    #     #print(pred[0])
    #     #print(animals)
    #     self.txt0['text'] = "{} !".format(animals[int(i)])
        
        
        
    #     for j,(p,a) in enumerate(zip(pred[0],animals)):
    #         self.txt[j]['text'] = "{} --> {:.4f}".format(a,p)
        
        







if __name__ == '__main__':
    r = root()
    r.mainloop()