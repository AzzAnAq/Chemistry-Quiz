from tkinter import*
import ctypes
import tkinter.font as tkFont
#---------------Play Button Page---------------#
def openplayb():
    # window details
    playb = Toplevel(pg)
    playb.title('GAME Options')
    playb.geometry('750x750')
    playb.lift()
    playb.focus_force()
    #font creation for options entrys 
    ctypes.windll.gdi32.AddFontResourceW(r"SOFTWARE_QUIZ/Chemistry-Quiz/Fonts/Hangyaboly.ttf")
    custom_font = tkFont.Font(family="hangyaboly", size=14)
    # playb page image
    playb.optionspg= PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/ChemistryQuiz options page.png')
    playb_image = Label(playb, image = playb.optionspg, bd=0)
    playb_image.pack()
    # nickname entry
    Enickname = Entry(playb, width = 31, font = custom_font, borderwidth=0, highlightthickness=0)
    Enickname.place(x=300, y=130.5)
    # Questions entry
    Equestions = Entry(playb, width = 17, font = custom_font, borderwidth=0, highlightthickness=0)
    Equestions.place(x=145, y=352.5)
    # Range entry
    Erange = Entry(playb, width = 17, font = custom_font, borderwidth=0, highlightthickness=0)
    Erange.place(x=433, y=352.5)
    # Topic entry
    Etopic = Entry(playb, width = 51, font = custom_font, borderwidth=0, highlightthickness=0)
    Etopic.place(x=112, y=578)
    # Continue button
    playb.continue_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/continue button.png')
    playb.continue_button = Button(playb, image= playb.continue_image, borderwidth=0, highlightthickness=0 )
    playb.continue_button.place(relx= 0.5, rely= 0.92, anchor = 'center')#command = continue_function

   
#---------------MAIN PAGE---------------#
# window details
pg=Tk()
pg.attributes('-fullscreen', True)
pg.config(bg='#2C5570')
pg.title('CHEMISTRY QUIZ')
# main page image
image1= PhotoImage(file=r"SOFTWARE_QUIZ/Chemistry-Quiz/Chemistry Quiz front page and quiz.png")
image1_label = Label(pg, image = image1,bd=0).pack()
# play button
play_image = PhotoImage(file =r'SOFTWARE_QUIZ/Chemistry-Quiz/play button.png')
play_button = Button(pg, image= play_image, command = openplayb, borderwidth=0, highlightthickness=0 ).place(relx= 0.5, rely=0.59, anchor = 'center')
# quit button
quit_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/quit button.png')
quit_button = Button(pg, image= quit_image, command = pg.destroy, borderwidth=0, highlightthickness=0 ).place(relx= 0.5, rely=0.75, anchor = 'center')



pg.mainloop()



