from tkinter import*
#---------------Play Button Page---------------#
def openplayb():
    playb = Toplevel(pg)
    playb.title('GAME Options')
    playb.geometry('500x600')
    playb.config(bg='#2C5570')
    
#---------------MAIN PAGE---------------#
#window details
pg=Tk()
pg.geometry
pg.config(bg='#2C5570')
pg.title('CHEMISTRY QUIZ')
#logo image
image= PhotoImage(file='C:/Users/azzan/OneDrive/Desktop/Python/SOFTWARE_QUIZ/Chemistry Quiz (1).png')
image_label = Label(pg, image = image,bd=0).pack()
#---------------------------------------------------can1 = Canvas(pg,bg='blue',height=200,width=200)
#----------------------------------------------------can1.pack(pady=40)
#----------------------------------------------------can2 = Canvas(pg,bg='blue',height=90,width=360) 
#----------------------------------------------------can2.pack(pady=30)
can2 = Button(pg,bg='blue',text='PLAY',command=openplayb)
can2.pack(pady=30)
l1=Label(pg, text= 'Name/Nickname (15 charecters):',font=50,bg='#2C5570',fg='white') 
l1.pack(pady=5)
l1=Entry(pg,font=50,bd=15)
l1.pack()

pg.mainloop()