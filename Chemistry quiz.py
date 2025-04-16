from tkinter import*
import ctypes
import tkinter.font as tkFont
from tkinter import messagebox
#---------------PLAY BUTTON PAGE---------------#
def openplayb():
    # window details
    global playb
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
    global Enickname 
    Enickname = Entry(playb, width = 31, font = custom_font, borderwidth=0, highlightthickness=0)
    Enickname.place(x=300, y=130.5)
    # Questions entry
    global Equestions 
    Equestions = Entry(playb, width = 17, font = custom_font, borderwidth=0, highlightthickness=0)
    Equestions.place(x=145, y=352.5)
    # Range entry
    global Erange 
    Erange = Entry(playb, width = 17, font = custom_font, borderwidth=0, highlightthickness=0)
    Erange.place(x=433, y=352.5)
    # Topic entry
    global Etopic 
    Etopic = Entry(playb, width = 51, font = custom_font, borderwidth=0, highlightthickness=0)
    Etopic.place(x=112, y=578)
    # Continue button
    playb.continue_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/continue button.png')
    playb.continue_button = Button(playb, command = b_continue, image = playb.continue_image, borderwidth =0, highlightthickness =0 )
    playb.continue_button.place(relx= 0.5, rely= 0.92, anchor = 'center') 

    #---------------(continue button)---------------# 
def b_continue():
    try:
        global nickname
        nickname = str(Enickname.get())
        global questions_num
        questions_num = int(Equestions.get())
        global range_val
        range_input = Erange.get()
        global min_val, max_val
        min_val, max_val = map(int, map(str.strip, range_input.split(',')))
        range_val = (min_val, max_val)
        global topic
        topic = str(Etopic.get())
        test()
    except:
        show_message()
#---------------ALL ERROR MESSAGES---------------#
def show_message(): 
    messagebox.showerror("Oops!", "error")
    
#----------------this is just a dev test (will be removed later)---------------#
def test():
    test=Toplevel(pg)
    l_test = Label(test, text = f'{nickname}, {questions_num}, {min_val}, {max_val}, {topic}')
    l_test.pack()
    playb.lift()
    playb.focus_force()


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

    #---------------(info lists)---------------#
names = [
    'hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon', 'sodium', 'magnesium', 'aluminium', 'silicon', 
    'phosphorus', 'sulfur', 'chlorine', 'argon', 'potassium', 'calcium', 'scandium', 'titanium', 'vanadium', 'chromium', 'manganese', 'iron', 'cobalt', 'nickel', 
    'copper', 'zinc', 'gallium', 'germanium', 'arsenic', 'selenium', 'bromine', 'krypton', 'rubidium', 'strontium', 'yttrium', 'zirconium', 'niobium', 
    'molybdenum', 'technetium', 'ruthenium', 'rhodium', 'palladium', 'silver', 'cadmium', 'indium', 'tin', 'antimony', 'tellurium', 'iodine', 'xenon', 
    'cesium', 'barium', 'lanthanum', 'cerium', 'praseodymium', 'neodymium', 'promethium', 'samarium', 'europium', 'gadolinium', 'terbium', 'dysprosium', 
    'holmium', 'erbium', 'thulium', 'ytterbium', 'lutetium', 'hafnium', 'tantalum', 'tungsten', 'rhenium', 'osmium', 'iridium', 'platinum', 'gold', 'mercury', 
    'thallium', 'lead', 'bismuth', 'polonium', 'astatine', 'radon', 'francium', 'radium', 'actinium', 'thorium', 'protactinium', 'uranium', 'neptunium', 
    'plutonium', 'americium', 'curium', 'berkelium', 'californium', 'einsteinium', 'fermium', 'mendelevium', 'nobelium', 'lawrencium', 'rutherfordium', 
    'dubnium', 'seaborgium', 'bohrium', 'hassium', 'meitnerium', 'darmstadtium', 'roentgenium', 'copernicium', 'nihonium', 'flerovium', 'moscovium', 
    'livermorium', 'tennessine', 'oganesson'
]
symbols = [
    'h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne', 'na', 'mg', 'al', 'si','p', 's', 'cl', 'ar', 'k', 'ca', 'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni', 
    'cu', 'zn', 'ga', 'ge', 'as', 'se', 'br', 'kr', 'rb', 'sr', 'y', 'zr', 'nb','mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn', 'sb', 'te', 'i', 'xe', 
    'cs', 'ba', 'la', 'ce', 'pr', 'nd', 'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho','er', 'tm', 'yb', 'lu', 'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg', 
    'tl', 'pb', 'bi', 'po', 'at', 'rn', 'fr', 'ra', 'ac', 'th', 'pa', 'u', 'np','pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no', 'lr', 'rf', 'db', 'sg', 
    'bh', 'hs', 'mt', 'ds', 'rg', 'cn', 'nh', 'fl', 'mc', 'lv', 'ts', 'og'
]
ato_num = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 
    43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 
    83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 
    118
]
groups = [
    1, 18, 1, 2, 13, 14, 15, 16, 17, 18, 1, 2, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 4, 5, 6, 
    7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 
    1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
]
periods = [
    1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 
    5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]


pg.mainloop()



