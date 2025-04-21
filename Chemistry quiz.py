from tkinter import*
import ctypes
import tkinter.font as tkFont
from tkinter import messagebox
import random
from tkinter import ttk
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
    def enter_key(event):
        b_continue()
    
    playb.bind('<Return>', enter_key)

    #---------------(continue button)---------------# 
def b_continue():
    global num_correct_answers
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
    except Exception as e:
        show_message()
        print(e)
    
    num_correct_answers = 0
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
    global hangyaboly_90
    ctypes.windll.gdi32.AddFontResourceW(r"SOFTWARE_QUIZ/Chemistry-Quiz/Fonts/Hangyaboly.ttf")
    hangyaboly_90 = tkFont.Font(family="hangyaboly", size=90)
    global hangyaboly_150
    ctypes.windll.gdi32.AddFontResourceW(r"SOFTWARE_QUIZ/Chemistry-Quiz/Fonts/Hangyaboly.ttf")
    hangyaboly_150 = tkFont.Font(family="hangyaboly", size=150)

    #styles
    quiz_style = ttk.Style()
    quiz_style.theme_use('default')
    quiz_style.configure("Quiz.Horizontal.TProgressbar", thickness=20, troughcolor='#2c5570', background='#54bfe3')


    # window details
    global quiz
    quiz = Toplevel(pg)
    quiz.attributes('-fullscreen', True)
    quiz.title('Questions')
    quiz.lift()
    quiz.focus_force()
    quiz.grab_set()
    global iteration_count
    iteration_count = 0
    is_answered = False
    # background image
    quiz.quizimage= PhotoImage(file=r"SOFTWARE_QUIZ/Chemistry-Quiz/Quiz page.png")
    quizimage_label = Label(quiz, image = quiz.quizimage,bd=0)
    quizimage_label.pack()
    #start 
    start = Label(quiz, text = 'Start',bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#54bfe3', font= hangyaboly_20)
    start. place(relx=0.12, rely=0.198, anchor= 'center')
    # progress bar
    global progressbar
    progressbar = ttk.Progressbar(quiz,style ="Quiz.Horizontal.TProgressbar", orient= HORIZONTAL, length = 1060, mode= 'determinate')
    progressbar.place(relx=0.5, rely=0.198, anchor= 'center')
    progressbar['value'] = 0
    #finish
    finish = Label(quiz, text = 'Finish',bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#54bfe3', font= hangyaboly_20)
    finish. place(relx=0.88, rely=0.198, anchor= 'center')
    # next button 
    global next_button
    quiz.next_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/Next button.png')
    next_button = Button(quiz, image = quiz.next_image, borderwidth =0, highlightthickness =0, command= iterations )
    next_button.place(relx= 0.875, rely= 0.84, anchor = 'center')
    # sumbit button 
    quiz.submit_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/Submit button.png')
    submit_button = Button(quiz, image = quiz.submit_image, borderwidth =0, highlightthickness =0, command= b_submit )
    submit_button.place(relx= 0.5, rely= 0.84, anchor = 'center') 
    # menu button
    quiz.menu_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/Menu button.png')
    menu_button = Button(quiz, image = quiz.menu_image, borderwidth =0, highlightthickness =0, command= quiz.destroy )
    menu_button.place(relx= 0.12, rely= 0.84, anchor = 'center') 
    # label of tile
    global L_title
    L_title = Label(quiz, text = f'Question 1',bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#54bfe3', font= CaveatBrush_62)
    L_title. place(relx=0.5, rely=0.10, anchor= 'center')
    # question label
    global L_question
    L_question = Label(quiz, text = "", bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#b2ca9a', font= hangyaboly_20)
    L_question.place(relx=0.5, rely=0.59, anchor= 'center')
    #Question entry
    global E_quiz
    E_quiz = Entry(quiz, width = 25, font = hangyaboly_30, borderwidth=0, highlightthickness=0, justify='center')
    E_quiz.place(relx=0.5, rely=0.69, anchor= 'center')
    # label of check (correct/incorrect)
    global L_check
    L_check = Label(quiz, text = f'', bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#b2ca9a', font= hangyaboly_20)
    L_check.place(relx=0.5, rely=0.765, anchor= 'center')

    def enter(event=None):
        nonlocal is_answered
        if not is_answered:
            b_submit()  # the function checks the answer
            is_answered = True
        else:
            if iteration_count == questions_num:
                b_finish()
            else:
                iterations()  # Your function to go to the next question
                is_answered = False
    quiz.bind('<Return>', enter)
    iterations()

#---------------PAGES OF QUIZ---------------#
def iterations():
    L_check.config(text = '')
    progressbar['value'] = progressbar['value'] + (100/questions_num)
    global iteration_count
    L_title.config(text = f'Questions {iteration_count+1}')
    global correct_answer
    correct_answer= ''
    global ranint1
    ranint1 = random.randint(minrange,maxrange)
    if iteration_count + 1 == questions_num:
        quiz.finish_image = PhotoImage(file= r'SOFTWARE_QUIZ/Chemistry-Quiz/Finish button.png')
        next_button.config(image= quiz.finish_image, command = b_finish)
    if topic.lower() == 'name':
        name_topic()
    elif topic.lower() == 'symbol':
        symbol_topic()
    elif topic.lower() == 'atomic number':
        atonum_topic()
    elif topic.lower() == 'group':
        group_topic()
    elif topic.lower() == 'period':
        period_topic()
    elif topic.lower() == 'random':
        ranint2 = random.randint(1,5)
        if ranint2 == 1:
            name_topic()
        elif ranint2 == 2:
            symbol_topic()
        elif ranint2 == 3:
            atonum_topic()
        elif ranint2 == 4:
            group_topic()
        elif ranint2 == 5:
            period_topic() 
    iteration_count += 1 
    E_quiz.delete(0,END)
    E_quiz.config(foreground='black')
#---------------PAGE IF NAME IS TOPIC---------------#
def name_topic():
    frame1 = Frame(quiz)
    frame1.place_forget()
    frame1.place(relx=0.5, rely=0.375, anchor= 'center')
    frame1.config(height= 280, width=280, bg= '#2c5570')
    quiz.frame1i= PhotoImage(file=r"SOFTWARE_QUIZ/Chemistry-Quiz/Frame 1.png")
    fram1i_label = Label(frame1, image = quiz.frame1i,bd=0)
    fram1i_label.pack()
    L_symbol = Label(frame1 ,text= Symbol[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
    L_symbol.place(relx=0.5, rely=0.5, anchor= 'center')
    L_question.config(text = questions[0])
    global correct_answer
    correct_answer= Name[ranint1]
#---------------PAGE IF SYMBOL IS TOPIC---------------#
def symbol_topic():
    frame1 = Frame(quiz)
    frame1.place_forget()
    frame1.place(relx=0.5, rely=0.375, anchor= 'center')   
    frame1.config(height=280, width=750, bg='#2c5570')
    quiz.frame2i= PhotoImage(file=r"SOFTWARE_QUIZ/Chemistry-Quiz/Frame2.png")
    fram2i_label = Label(frame1, image = quiz.frame2i,bd=0)
    fram2i_label.pack()
    L_name = Label(frame1 ,text= Name[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
    L_name.place(relx=0.5, rely=0.5, anchor= 'center')
    L_question.config(text = questions[1])
    global correct_answer
    correct_answer = Symbol[ranint1]
#---------------PAGE IF ATOMIC NUM IS TOPIC---------------#
def atonum_topic():
    frame1 = Frame(quiz)
    frame1.place_forget()
    frame1.place(relx=0.5, rely=0.375, anchor= 'center')
    frame1.config(height=280, width=750, bg='#2c5570')
    quiz.frame2i= PhotoImage(file=r"SOFTWARE_QUIZ/Chemistry-Quiz/Frame2.png")
    fram2i_label = Label(frame1, image = quiz.frame2i,bd=0)
    fram2i_label.pack()
    L_name = Label(frame1 ,text= Name[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
    L_name.place(relx=0.5, rely=0.5, anchor= 'center')
    L_question.config(text = questions[2])
    global correct_answer
    correct_answer = ato_num[ranint1]
#---------------PAGE IF GROUP IS TOPIC---------------#
def group_topic():
    frame1 = Frame(quiz)
    frame1.place_forget()
    frame1.place(relx=0.5, rely=0.375, anchor= 'center')
    frame1.config(height=280, width=750, bg='#2c5570')
    quiz.frame2i= PhotoImage(file=r"SOFTWARE_QUIZ/Chemistry-Quiz/Frame2.png")
    fram2i_label = Label(frame1, image = quiz.frame2i,bd=0)
    fram2i_label.pack()
    L_name = Label(frame1 ,text= Name[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
    L_name.place(relx=0.5, rely=0.5, anchor= 'center')
    L_question.config(text = questions[3])
    global correct_answer
    correct_answer = groups[ranint1]
#---------------PAGE IF PERIOD IS TOPIC---------------#
def period_topic():
    frame1 = Frame(quiz)
    frame1.place_forget()
    frame1.place(relx=0.5, rely=0.375, anchor= 'center')
    frame1.config(height=280, width=750, bg='#2c5570')
    quiz.frame2i= PhotoImage(file=r"SOFTWARE_QUIZ/Chemistry-Quiz/Frame2.png")
    fram2i_label = Label(frame1, image = quiz.frame2i,bd=0)
    fram2i_label.pack()
    L_name = Label(frame1 ,text= Name[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
    L_name.place(relx=0.5, rely=0.5, anchor= 'center')
    L_question.config(text = questions[4])
    global correct_answer
    correct_answer = periods[ranint1]

#---------------SUBMIT BUTTON---------------#
def b_submit():
    global answer, num_correct_answers
    answer = E_quiz.get()
    
    if str(correct_answer).lower() == str(answer).lower():
        L_check.config(text = f'{nickname} your answer is correct!!!!', foreground = 'green')
        E_quiz.config(foreground='green')
        num_correct_answers += 1
    else:
        L_check.config( text = f'{nickname} your answer is incorrect :(', foreground= 'red')
        E_quiz.insert(END, f' :The correct answer is {correct_answer}')
        E_quiz.config(foreground='red')

#---------------FINISH PAGE---------------#
def b_finish():
    global finishpg, L_moderate, L_weak, L_proficient, percent_correct, L_total, L_correct, quit_finish_button, menue_finish_button, scorebar
    finishpg = Toplevel(pg)
    finishpg.attributes('-fullscreen', True)
    finishpg.title('Questions')
    finishpg.lift()
    finishpg.focus_force()
    finishpg.grab_set()
    finishpg.image2= PhotoImage(file=r"SOFTWARE_QUIZ/Chemistry-Quiz/score page.png")
    image2_label = Label(finishpg, image = finishpg.image2,bd=0)
    image2_label.place(relx=0.5, rely=0.5, anchor= 'center')
    # progress bar
    style0 = ttk.Style(finishpg)
    style0.theme_use('default')
    style0.configure("style0.Horizontal.TProgressbar", thickness = 40, troughcolour = '#ff6666', background = '#a6a6a6' )

    style1 = ttk.Style(finishpg)
    style1.theme_use('default')
    style1.configure("style1.Horizontal.TProgressbar", thickness = 40, troughcolour = '#ff6666', background = '#ff5757' )

    style2 = ttk.Style(finishpg)
    style2.theme_use('default')
    style2.configure("style2.Horizontal.TProgressbar", thickness = 40, troughcolour = '#ff6666', background = '#ff914d' )

    style3 = ttk.Style(finishpg)
    style3.theme_use('default')
    style3.configure("style3.Horizontal.TProgressbar", thickness = 40, troughcolour = '#ff6666', background = '#00bf63' )

    scorebar = ttk.Progressbar(finishpg, style = "style0.Horizontal.TProgressbar", orient= HORIZONTAL, length = 1300, mode= 'determinate')
    scorebar.place(relx=0.5, rely=0.72, anchor= 'center')  
        #lable for bar 1
    L_weak = Label(finishpg, text = 'WEAK', foreground= '#ffffff', bg = '#2c5570',borderwidth=0, highlightthickness=0, font = hangyaboly_20)
    L_weak.place(relx=0.25, rely=0.67, anchor= 'center')
        # label for bar 2
    L_moderate = Label(finishpg, text = 'MODERATE', foreground= '#ffffff', bg = '#2c5570',borderwidth=0, highlightthickness=0, font = hangyaboly_20)
    L_moderate.place(relx=0.50, rely=0.67, anchor= 'center')
        # label for bar 3
    L_proficient = Label(finishpg, text = 'PROFICIENT', foreground= '#ffffff', bg = '#2c5570',borderwidth=0, highlightthickness=0, font = hangyaboly_20)
    L_proficient.place(relx=0.75, rely=0.67, anchor= 'center')

    # label of num_correct
    L_correct = Label(finishpg, text = '------', foreground= '#ffffff', bg = '#6796b5',borderwidth=0, highlightthickness=0, font = hangyaboly_90)
    L_correct.place(relx=0.5, rely=0.30, anchor= 'center')
    # label of question_num
    L_total = Label(finishpg, text = '------', foreground= '#ffffff', bg = '#6796b5',borderwidth=0, highlightthickness=0, font = hangyaboly_90)
    L_total.place(relx=0.5, rely=0.50, anchor= 'center')

    # quit button
    finishpg.quit_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/quit button_finish.png')
    quit_finish_button = Button(finishpg, image = finishpg.quit_image, borderwidth =0, highlightthickness =0, command= pg.destroy )
    quit_finish_button.place(relx= 0.35, rely= 0.84, anchor = 'center') 

    # quit button
    finishpg.menue_image = PhotoImage(file = r'SOFTWARE_QUIZ/Chemistry-Quiz/menue button_finish.png')
    menue_finish_button = Button(finishpg, image = finishpg.menue_image, borderwidth =0, highlightthickness =0, command= finishpg.destroy )
    menue_finish_button.place(relx= 0.65, rely= 0.84, anchor = 'center') 

    percent_correct = (num_correct_answers/questions_num)*100
    scorebar['value'] = 0
    quiz.destroy()
    score_progbar()

def score_progbar():
    global percent_correct
    if scorebar['value'] < percent_correct and scorebar['value'] < 100 :
        scorebar['value'] += 1
        if 16 <= scorebar['value'] < 17:
            L_weak.config(foreground= '#ff5757')
            scorebar.config(style = "style1.Horizontal.TProgressbar")
        elif 49 <= scorebar['value'] < 50:
            L_moderate.config(foreground= '#ff914d')
            scorebar.config(style = "style2.Horizontal.TProgressbar")
        elif scorebar['value'] == 83:
            L_weak.config(foreground= '#00bf63')
            scorebar.config(style = "style3.Horizontal.TProgressbar")
        finishpg.after(20, score_progbar)
    else:
        L_correct.config(text = num_correct_answers)
        L_total.config(text = questions_num)
    


        


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
questions = [
    "What is this element's name?", "What is this element's symbol?", "What is this element's atomic number?",
    "What is this element's group?", "What is this element's period?"
]
pg.mainloop()