from customtkinter import*
from PIL import Image, ImageTk
#---------------Play Button Page---------------#
def openplayb():
    playb = CTkToplevel(pg)
    playb.title('GAME Options')
    playb.geometry('500x600')
    playb.resizable(False, False)
    playb.config(bg='#2C5570')
    playb.lift()
    playb.focus_force()
   
#---------------MAIN PAGE---------------#
# window details
pg=CTk()
screen_width = pg.winfo_screenwidth()
screen_height = pg.winfo_screenheight()
pg.attributes('-fullscreen', True)
pg.config(bg='#2C5570')
pg.title('CHEMISTRY QUIZ')
# main page image
image1= CTkImage(Image.open(r"SOFTWARE_QUIZ/Chemistry-Quiz/Chemistry Quiz front page and quiz.png"), size=(screen_width,screen_height))
image1_label = CTkLabel(pg, image = image1, text='').place(anchor = 'center')
# play button
play_image = CTkImage(Image.open(r'SOFTWARE_QUIZ/Chemistry-Quiz/play button.png'), size=(432,126))
play_button = CTkButton(pg, image= play_image, command = openplayb, text='').place(relx= 0.5, rely=0.59, anchor = 'center')
# quit button
quit_image = CTkImage(Image.open(r'SOFTWARE_QUIZ/Chemistry-Quiz/quit button.png'), size=(432,127))
quit_button = CTkButton(pg, image= quit_image, command = pg.destroy , text='').place(relx= 0.5, rely=0.75, anchor = 'center')




pg.mainloop()
