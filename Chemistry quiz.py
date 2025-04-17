from tkinter import*
import ctypes
import tkinter.font as tkFont
from tkinter import messagebox
import random
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
    global hangyaboly_14
    ctypes.windll.gdi32.AddFontResourceW(r"SOFTWARE_QUIZ/Chemistry-Quiz/Fonts/Hangyaboly.ttf")
    hangyaboly_14 = tkFont.Font(family="hangyaboly", size=14)
    # playb page image
    playb.optionspg= PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/ChemistryQuiz options page.png')
    playb_image = Label(playb, image = playb.optionspg, bd=0)
    playb_image.pack()
    # nickname entry
    global Enickname 
    Enickname = Entry(playb, width = 31, font = hangyaboly_14, borderwidth=0, highlightthickness=0)
    Enickname.place(x=300, y=130.5)
    # Questions entry
    global Equestions 
    Equestions = Entry(playb, width = 17, font = hangyaboly_14, borderwidth=0, highlightthickness=0)
    Equestions.place(x=137, y=349.5)
    # Highest Range entry
    global Emaxrange 
    Emaxrange = Entry(playb, width = 9, font = hangyaboly_14, borderwidth=0, highlightthickness=0)
    Emaxrange.place(x=380, y=349.5)
    # Lowest Range entry
    global Eminrange 
    Eminrange = Entry(playb, width = 9, font = hangyaboly_14, borderwidth=0, highlightthickness=0)
    Eminrange.place(x=520, y=349.5)
    # Topic entry
    global Etopic 
    Etopic = Entry(playb, width = 51, font = hangyaboly_14, borderwidth=0, highlightthickness=0)
    Etopic.place(x=112, y=578)
    # Continue button
    playb.continue_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/continue button.png')
    continue_button = Button(playb, command = b_continue, image = playb.continue_image, borderwidth =0, highlightthickness =0 )
    continue_button.place(relx= 0.5, rely= 0.92, anchor = 'center') 

    #---------------(continue button)---------------# 
def b_continue():
    try:
        global nickname
        nickname = str(Enickname.get())
        global questions_num
        questions_num = int(Equestions.get())
        global maxrange
        maxrange = int(Emaxrange.get()) - 1 #to match the list as it starts from zero and the periodic table begins at one
        global minrange
        minrange = int(Eminrange.get()) - 1 #same reason as maxrange
        global topic
        topic = str(Etopic.get())
        playb.destroy() 
        quizpage()
    except:
        show_message()
#---------------ALL ERROR MESSAGES---------------#
def show_message(): 
    messagebox.showerror("Oops!", "error")
    
#---------------QUIZ PAGE---------------#  
def quizpage():
    # fonts
    global CaveatBrush_62
    ctypes.windll.gdi32.AddFontResourceW(r"SOFTWARE_QUIZ/Chemistry-Quiz/Fonts/CaveatBrush-Regular.ttf")
    CaveatBrush_62 = tkFont.Font(family="Caveat Brush", size=62)
    global hangyaboly_20
    ctypes.windll.gdi32.AddFontResourceW(r"SOFTWARE_QUIZ/Chemistry-Quiz/Fonts/Hangyaboly.ttf")
    hangyaboly_20 = tkFont.Font(family="hangyaboly", size=20)
    global hangyaboly_30
    ctypes.windll.gdi32.AddFontResourceW(r"SOFTWARE_QUIZ/Chemistry-Quiz/Fonts/Hangyaboly.ttf")
    hangyaboly_30 = tkFont.Font(family="hangyaboly", size=30)
    ctypes.windll.gdi32.AddFontResourceW(r"SOFTWARE_QUIZ/Chemistry-Quiz/Fonts/Hangyaboly.ttf")
    hangyaboly_90 = tkFont.Font(family="hangyaboly", size=150)

    # window details
    global quiz
    quiz = Toplevel(pg)
    quiz.attributes('-fullscreen', True)
    quiz.title('Questions')
    quiz.lift()
    quiz.focus_force()
    quiz.grab_set
    # background image
    quiz.quizimage= PhotoImage(file=r"SOFTWARE_QUIZ/Chemistry-Quiz/Quiz page.png")
    quizimage_label = Label(quiz, image = quiz.quizimage,bd=0)
    quizimage_label.pack()
    # sumbit button 
    quiz.submit_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/Submit button.png')
    submit_button = Button(quiz, image = quiz.submit_image, borderwidth =0, highlightthickness =0 )
    submit_button.place(relx= 0.875, rely= 0.84, anchor = 'center') 
    # menu button
    quiz.menu_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/Menu button.png')
    menu_button = Button(quiz, image = quiz.menu_image, borderwidth =0, highlightthickness =0, command= quiz.destroy )
    menu_button.place(relx= 0.12, rely= 0.84, anchor = 'center') 

    #------First iteration of loop (question 1)------#
    # List of all questions
    questions = [
        "What is this element's name?", "What is this element's symbol?", "What is this element's atomic number?",
        "What is this element's Group?", "What is this element's period?"
    ]
    # label of tile
    L_title = Label(quiz, text = 'Question 1',bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#54bfe3', font= CaveatBrush_62)
    L_title. place(relx=0.5, rely=0.10, anchor= 'center')
    #Question entry
    global E_quiz
    E_quiz = Entry(quiz, width = 25, font = hangyaboly_30, borderwidth=0, highlightthickness=0, justify='center')
    E_quiz.place(relx=0.5, rely=0.69, anchor= 'center')
    # question label
    L_question = Label(quiz, text = "", bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#b2ca9a', font= hangyaboly_20)
    L_question.place(relx=0.5, rely=0.59, anchor= 'center')
    #frame
    frame1 = Frame(quiz)
    frame1.config(height= 280, width=280, bg= '#2c5570')
    frame1.place(relx=0.5, rely=0.375, anchor= 'center')
    global correct_answer
    correct_answer= ''

    if topic.lower() == 'name':
        L_question.config(text = questions[0])
        quiz.framei= PhotoImage(file=r"SOFTWARE_QUIZ/Chemistry-Quiz/Frame 1.png")
        frami_label = Label(frame1, image = quiz.framei,bd=0)
        frami_label.pack()
        global ranint1
        ranint1 = random.randint(minrange,maxrange)
        L_symbol = Label(frame1 ,text= Symbol[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
        L_symbol.place(relx=0.5, rely=0.5, anchor= 'center')
        correct_answer= Name[ranint1]

def b_submit():
    if Name[ranint1].lower() == str(E_quiz.get()):
        show_message()
        print('correct')



        






#---------------MAIN PAGE---------------#
# window details
pg=Tk()
pg.attributes('-fullscreen', True)
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
Name = [
    'Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon',
    'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium',
    'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc',
    'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium',
    'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin',
    'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium',
    'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium',
    'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury',
    'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium',
    'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium',
    'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium',
    'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson'
]
Symbol = [
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
    'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
    'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
    'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
    'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
    'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
    'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
    'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
    'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
    'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
    'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'
]
pg.mainloop()



