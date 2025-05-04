from tkinter import*
import ctypes
import tkinter.font as tkFont
from tkinter import messagebox
import random
from tkinter import ttk
import sys
#---------------PLAY BUTTON PAGE---------------#
def openplayb():
    # window details
    global playb, hangyaboly_14, Enickname, Equestions, Emaxrange, Eminrange,Etopic, continue_button, play_image
    playb = Toplevel(pg)
    playb.title('Options')
    playb.geometry('750x750')
    playb.lift()
    playb.focus_force()
    #font creation for options entry
    ctypes.windll.gdi32.AddFontResourceW(r"Fonts/Hangyaboly.ttf")
    hangyaboly_14 = tkFont.Font(family="hangyaboly", size=14)
    # playb page image
    playb.optionspg= PhotoImage(file = r'Images/options page.png')
    playb_image = Label(playb, image = playb.optionspg, bd=0)
    playb_image.pack()
    # nickname entry
    nickcommand = (pg.register(limit_nickname), '%P')
    Enickname = Entry(playb, width = 31, font = hangyaboly_14, borderwidth=0, highlightthickness=0, validate = 'key', validatecommand= nickcommand )
    Enickname.place(x=300, y=130.5)
    Enickname.focus_set()
    # Questions entry
    questiocommand = (pg.register(limit_questions), '%P')
    Equestions = Entry(playb, width = 17, font = hangyaboly_14, borderwidth=0, highlightthickness=0, validate = 'key', validatecommand= questiocommand )
    Equestions.place(x=137, y=349.5)
    #Range
    range_topic_command = (pg.register(limit_range_topic), '%P')
    # Highest Range entry
    Emaxrange = Entry(playb, width = 9, font = hangyaboly_14, borderwidth=0, highlightthickness=0, validate = 'key', validatecommand= range_topic_command )
    Emaxrange.place(x=380, y=349.5)
    # Lowest Range entry
    Eminrange = Entry(playb, width = 9, font = hangyaboly_14, borderwidth=0, highlightthickness=0, validate = 'key', validatecommand= range_topic_command )
    Eminrange.place(x=520, y=349.5)
    # Topic entry
    Etopic = Entry(playb, width = 51, font = hangyaboly_14, borderwidth=0, highlightthickness=0, validate = 'key', validatecommand= range_topic_command)
    Etopic.place(x=112, y=578)
    # Continue button
    playb.continue_image = PhotoImage(file = r'Images/continue button.png')
    continue_button = Button(playb, command = b_continue, image = playb.continue_image, borderwidth =0, highlightthickness =0 )
    continue_button.place(relx= 0.5, rely= 0.92, anchor = 'center')
    playb.bind('<Return>', enter_key)
#----limits to charecter input in entries----#
def limit_nickname(val):
    return len(val) <= 34, 
def limit_questions(val1):
    return len(val1) <= 17
def limit_range_topic(val2):
    return len(val2) <= 13
#------Enter key bind-------#
def enter_key(event):
        b_continue()
        



    #---------------(continue button)---------------#
def b_continue():
    global num_correct_answers, nickname, questions_num, maxrange, minrange, topic
    nickname = Enickname.get()
    questions_num_str = Equestions.get().strip()
    topic = Etopic.get().strip().lower()
    maxrange_str = Emaxrange.get().strip().lower()
    minrange_str = Eminrange.get().strip().lower()
    valid = True  # validation flag
    num_correct_answers = 0
    # Check for empty fields
    if not nickname or not questions_num_str or not maxrange_str or not minrange_str or not topic:
        messagebox.showerror("Oops!", "Please fill in all the required fields.")
        valid = False
    # Check if number of questions is a valid int >= 1
    elif not questions_num_str.isdigit() or int(questions_num_str) <= 1:
        messagebox.showerror("Oops!", "Please enter a valid integer (larger than 1) in the questions section.")
        valid = False
    # Convert ranges and validate
    if valid:
        try:
            maxrange = name_lowered.index(maxrange_str)
            minrange = name_lowered.index(minrange_str)
        except ValueError:
            messagebox.showerror("Oops!", "Highest and lowest elements must be real elements.")
            valid = False

    if valid and maxrange < minrange:
        messagebox.showerror("Oops!", "Highest element must be farther down the periodic table than the lowest.")
        valid = False
    # Topic validation
    if valid and topic not in valid_topics:
        messagebox.showerror("Oops!", "Please enter a valid topic.")
        valid = False
    # If everything is valid, start the quiz
    if valid:
        questions_num = int(questions_num_str)
        quizpage()
    playb.destroy()

   
#---------------QUIZ PAGE---------------#  
def quizpage():
    # fonts
    global CaveatBrush_62, hangyaboly_20, hangyaboly_30, hangyaboly_90, quiz, iteration_count, quizimage_label, start, progressbar,finish, next_button, submit_button, menu_button, L_title, L_question, E_quiz, L_check, is_answered, frame1
    ctypes.windll.gdi32.AddFontResourceW(r"Fonts/CaveatBrush-Regular.ttf")
    CaveatBrush_62 = tkFont.Font(family="Caveat Brush", size=70)


    ctypes.windll.gdi32.AddFontResourceW(r"Fonts/Hangyaboly.ttf")
    hangyaboly_20 = tkFont.Font(family="hangyaboly", size=20)


    ctypes.windll.gdi32.AddFontResourceW(r"Fonts/Hangyaboly.ttf")
    hangyaboly_30 = tkFont.Font(family="hangyaboly", size=30)


    ctypes.windll.gdi32.AddFontResourceW(r"Fonts/Hangyaboly.ttf")
    hangyaboly_90 = tkFont.Font(family="hangyaboly", size=90)


    #styles
    quiz_style = ttk.Style()
    quiz_style.theme_use('default')
    quiz_style.configure("Quiz.Horizontal.TProgressbar", thickness=20, troughcolor='#2c5570', background='#54bfe3')




    # window details
    quiz = Toplevel(pg)
    quiz.attributes('-fullscreen', True)
    quiz.title('Questions')
    quiz.config(bg='#2c5570')
    quiz.lift()
    F_quiz = Frame(quiz)
    F_quiz.config(height= 1080, width = 1920, bd=10)
    F_quiz.place(relx= 0.5, rely=0.5, anchor = 'center')
    iteration_count = 0
    is_answered = False
    # background image
    quiz.quizimage= PhotoImage(file=r"Images/Quiz page.png")
    quizimage_label = Label(F_quiz, image = quiz.quizimage,bd=0)
    quizimage_label.pack()
    #start
    start = Label(F_quiz, text = 'Start',bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#54bfe3', font= hangyaboly_20)
    start. place(relx=0.15, rely=0.198, anchor= 'center')
    # progress bar
    progressbar = ttk.Progressbar(F_quiz,style ="Quiz.Horizontal.TProgressbar", orient= HORIZONTAL, length = 1200, mode= 'determinate')
    progressbar.place(relx=0.5, rely=0.198, anchor= 'center')
    progressbar['value'] = 0
    #finish
    finish = Label(F_quiz, text = 'Finish',bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#54bfe3', font= hangyaboly_20)
    finish. place(relx=0.85, rely=0.198, anchor= 'center')
    # next button
    quiz.next_image = PhotoImage(file = r'Images/Next button.png')
    next_button = Button(F_quiz, image = quiz.next_image, borderwidth =0, highlightthickness =0, command= next_error )
    next_button.place(relx= 0.845, rely= 0.84, anchor = 'center')
    # sumbit button
    quiz.submit_image = PhotoImage(file = r'Images/Submit button.png')
    submit_button = Button(F_quiz, image = quiz.submit_image, borderwidth =0, highlightthickness =0, command= b_submit )
    submit_button.place(relx= 0.5, rely= 0.84, anchor = 'center')
    # menu button
    quiz.menub_image = PhotoImage(file = r'Images/Menu button.png')
    menu_button = Button(F_quiz, image = quiz.menub_image, borderwidth =0, highlightthickness =0, command= quiz.destroy )
    menu_button.place(relx= 0.155, rely= 0.84, anchor = 'center')
    # label of tile
    L_title = Label(F_quiz, text = f'Question 1',bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#54bfe3', font= CaveatBrush_62)
    L_title. place(relx=0.5, rely=0.093, anchor= 'center')
    # question label
    L_question = Label(F_quiz, text = "", bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#b2ca9a', font= hangyaboly_20)
    L_question.place(relx=0.5, rely=0.59, anchor= 'center')
    #Question entry
    E_quiz = Entry(F_quiz, width = 28, font = hangyaboly_30, borderwidth=0, highlightthickness=0, justify='center')
    E_quiz.place(relx=0.5, rely=0.685, anchor= 'center')
    E_quiz.focus_set()
    # label of check (correct/incorrect)
    L_check = Label(F_quiz, text = f'', bg = '#2c5570',borderwidth=0, highlightthickness=0, foreground='#b2ca9a', font= hangyaboly_20)
    L_check.place(relx=0.5, rely=0.765, anchor= 'center')
    frame1 = Frame(quiz)
    frame1.place(relx=0.5, rely=0.4, anchor= 'center')

    quiz.bind('<Return>', enter)
    iterations()
    
    E_quiz.focus_set()

#---------------SUBMIT BUTTON---------------#
def b_submit():
    global num_correct_answers, is_answered
    answer = E_quiz.get()
    is_answered = True
    if answer == "":
        messagebox.showerror("Oops!", "Please fill in the entry", parent = quiz)
        return
    if str(correct_answer).lower() == answer.lower():
        L_check.config(text = f'{nickname} your answer is correct 😀', foreground = 'green')
        E_quiz.config(foreground='green')
        num_correct_answers += 1
    else:
        L_check.config( text = f'{nickname} your answer is incorrect 🙁', foreground= 'red')
        E_quiz.insert(END, f' :The correct answer is {correct_answer}')
        E_quiz.config(foreground='red')
    submit_button.config(command =messgae_submit_done )
    if iteration_count< questions_num:
        next_button.config(command= iterations)
    elif iteration_count == questions_num:
        next_button.config(command = b_finish)


def enter(event=None):
    global is_answered
    answer =E_quiz.get()
    if answer == "":
            messagebox.showerror("Oops!", "Please fill in the entry", parent = quiz)
            return
    if not is_answered and answer != "":
            b_submit() # the function checks the answer
    elif is_answered and answer != "":
        if iteration_count< questions_num:
                iterations()  # the function to go to the next question
                is_answered = False
        elif iteration_count == questions_num:
                b_finish()

def next_error():
    global is_answered
    messagebox.showerror("Oops!", "Please  submit answer first", parent = quiz)
    is_answered = False

def messgae_submit_done():
    messagebox.showerror("Oops!", "Please press next", parent = quiz)


#---------------PAGES OF QUIZ---------------#
def iterations():
    global iteration_count, correct_answer, ranint1, frame1, is_answered
    L_check.config(text = '')
    L_title.config(text = f'Questions {iteration_count+1}')
    E_quiz.delete(0,END)
    E_quiz.config(foreground='black')
    correct_answer= ''
    ranint1 = random.randint(minrange,maxrange)
    if iteration_count + 1 == questions_num:
        quiz.finish_image = PhotoImage(file= r'Images/Finish button.png')
        next_button.config(image= quiz.finish_image)
    if topic == 'name':
        name_topic()
    elif topic == 'symbol':
        symbol_topic()
    elif topic == 'atomic number':
        atonum_topic()
    elif topic == 'group':
        group_topic()
    elif topic == 'period':
        period_topic()
    iteration_count += 1
    progressbar['value'] = progressbar['value'] + (100/questions_num)
    next_button.config(command = next_error)
    is_answered = False
    check_quiz_exist()
    
#---------------PAGE IF NAME IS TOPIC---------------#
def name_topic():
    global correct_answer, frame1, fram2i_label, L_symbol
    submit_button.config(command =b_submit )
    frame1.config(height= 280, width=280, bg= '#2c5570')
    quiz.frame1i= PhotoImage(file=r"Images/Frame 1.png")
    fram2i_label = Label(frame1, image = quiz.frame1i,bd=0)
    fram2i_label.place(relx= 0.5, rely=0.5, anchor = 'center')
    L_symbol = Label(frame1 ,text= Symbol[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
    L_symbol.place(relx=0.5, rely=0.5, anchor= 'center')
    L_question.config(text = questions[0])
    correct_answer= Name[ranint1]
#---------------PAGE IF SYMBOL IS TOPIC---------------#
def symbol_topic():
    global correct_answer, frame1, fram2i_label, L_name
    submit_button.config(command =b_submit )
    frame1.config(height=280, width=750, bg='#2c5570')
    quiz.frame2i= PhotoImage(file=r"Images/Frame2.png")
    fram2i_label = Label(frame1, image = quiz.frame2i,bd=0)
    fram2i_label.place(relx= 0.5, rely=0.5, anchor = 'center')
    L_name = Label(frame1 ,text= Name[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
    L_name.place(relx=0.5, rely=0.5, anchor= 'center')
    L_question.config(text = questions[1])
    correct_answer = Symbol[ranint1]
#---------------PAGE IF ATOMIC NUM IS TOPIC---------------#
def atonum_topic():
    global correct_answer, frame1, fram2i_label, L_name
    submit_button.config(command =b_submit )
    frame1.config(height=280, width=750, bg='#2c5570')
    quiz.frame2i= PhotoImage(file=r"Images/Frame2.png")
    fram2i_label = Label(frame1, image = quiz.frame2i,bd=0)
    fram2i_label.place(relx= 0.5, rely=0.5, anchor = 'center')
    L_name = Label(frame1 ,text= Name[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
    L_name.place(relx=0.5, rely=0.5, anchor= 'center')
    L_question.config(text = questions[2])
    correct_answer = ato_num[ranint1]
#---------------PAGE IF GROUP IS TOPIC---------------#
def group_topic():
    global correct_answer, frame1, fram2i_label, L_name
    submit_button.config(command =b_submit )
    frame1.config(height=280, width=750, bg='#2c5570')
    quiz.frame2i= PhotoImage(file=r"Images/Frame2.png")
    fram2i_label = Label(frame1, image = quiz.frame2i,bd=0)
    fram2i_label.place(relx=0.5, rely=0.5, anchor= 'center')
    L_name = Label(frame1 ,text= Name[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
    L_name.place(relx=0.5, rely=0.5, anchor= 'center')
    L_question.config(text = questions[3])
    correct_answer = groups[ranint1]
#---------------PAGE IF PERIOD IS TOPIC---------------#
def period_topic():
    global correct_answer, frame1, fram2i_label, L_name
    submit_button.config(command =b_submit )
    frame1.config(height=280, width=750, bg='#2c5570')
    quiz.frame2i= PhotoImage(file=r"Images/Frame2.png")
    fram2i_label = Label(frame1, image = quiz.frame2i,bd=0)
    fram2i_label.place(relx= 0.5, rely=0.5, anchor = 'center')
    L_name = Label(frame1 ,text= Name[ranint1], bg='#6796b5',borderwidth=0, highlightthickness=0, foreground= '#b2ca9a', font = hangyaboly_90)
    L_name.place(relx=0.5, rely=0.5, anchor= 'center')
    L_question.config(text = questions[4])
    correct_answer = periods[ranint1]


def check_quiz_exist():
    if not fram2i_label or not frame1:
        if not L_symbol['text']:
            quizpage.destroy()
            quizpage()
            print('had to close and restart')

#---------------FINISH PAGE---------------#
def b_finish():
    global finishpg, L_moderate, L_weak, L_proficient, percent_correct, L_total, L_correct, quit_finish_button, menue_finish_button, scorebar
    finishpg = Toplevel(pg)
    finishpg.attributes('-fullscreen', True)
    finishpg.title('Score')
    finishpg.lift()
    finishpg.focus_force()
    finishpg.grab_set()
    finishpg.config(bg = '#2c5570')
    F_finish = Frame(finishpg)
    F_finish.config(height= 1080, width = 1920, bd=10)
    F_finish.place(relx= 0.5, rely=0.5, anchor = 'center')

    finishpg.image2= PhotoImage(file=r"Images/score page.png")
    image2_label = Label(F_finish, image = finishpg.image2,bd=0)
    image2_label.pack()
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


    scorebar = ttk.Progressbar(F_finish, style = "style0.Horizontal.TProgressbar", orient= HORIZONTAL, length = 1300, mode= 'determinate')
    scorebar.place(relx=0.5, rely=0.72, anchor= 'center')  
        #lable for bar 1
    L_weak = Label(F_finish, text = 'WEAK', foreground= '#ffffff', bg = '#2c5570',borderwidth=0, highlightthickness=0, font = hangyaboly_20)
    L_weak.place(relx=0.25, rely=0.67, anchor= 'center')
        # label for bar 2
    L_moderate = Label(F_finish, text = 'MODERATE', foreground= '#ffffff', bg = '#2c5570',borderwidth=0, highlightthickness=0, font = hangyaboly_20)
    L_moderate.place(relx=0.50, rely=0.67, anchor= 'center')
        # label for bar 3
    L_proficient = Label(F_finish, text = 'PROFICIENT', foreground= '#ffffff', bg = '#2c5570',borderwidth=0, highlightthickness=0, font = hangyaboly_20)
    L_proficient.place(relx=0.75, rely=0.67, anchor= 'center')


    # label of num_correct
    L_correct = Label(F_finish, text = '------', foreground= '#ffffff', bg = '#6796b5',borderwidth=0, highlightthickness=0, font = hangyaboly_90)
    L_correct.place(relx=0.5, rely=0.30, anchor= 'center')
    # label of question_num
    L_total = Label(F_finish, text = '------', foreground= '#ffffff', bg = '#6796b5',borderwidth=0, highlightthickness=0, font = hangyaboly_90)
    L_total.place(relx=0.5, rely=0.50, anchor= 'center')


    # quit button
    finishpg.quit_image = PhotoImage(file = r'Images/quit button_finish.png')
    quit_finish_button = Button(F_finish, image = finishpg.quit_image, borderwidth =0, highlightthickness =0, command= pg.destroy )
    quit_finish_button.place(relx= 0.35, rely= 0.84, anchor = 'center')


    # quit button
    finishpg.menue_image = PhotoImage(file = r'Images/menue button_finish.png')
    menue_finish_button = Button(F_finish, image = finishpg.menue_image, borderwidth =0, highlightthickness =0, command= finishpg.destroy )
    menue_finish_button.place(relx= 0.65, rely= 0.84, anchor = 'center')


    percent_correct = float((num_correct_answers/questions_num)*100)
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
            L_proficient.config(foreground= '#00bf63')
            scorebar.config(style = "style3.Horizontal.TProgressbar")
        finishpg.after(20, score_progbar)
    else:
        L_correct.config(text = num_correct_answers)
        L_total.config(text = questions_num)
   




def about_pg():
    about = Toplevel(pg)
    about.title('About page')
    about.geometry('750x750')
    about.lift()
    about.focus_force()
    about.abouti= PhotoImage(file=r"Images/about page.png")
    L_abouti = Label(about, image = about.abouti,bd=0)
    L_abouti.place(relx= 0.5, rely=0.5, anchor = 'center')
    about.close_button_i = PhotoImage(file =r'Images/close button.png')
    close_button = Button(about, image= about.close_button_i, command = about.destroy, borderwidth=0, highlightthickness=0 )
    close_button.place(relx= 0.5, rely=0.92, anchor = 'center')




#---------------MAIN PAGE---------------#
# window details
pg=Tk()
pg.attributes('-fullscreen', True)
pg.title('CHEMISTRY QUIZ')
pg.config(bg = '#2c5570')
F_mainpage = Frame(pg)
F_mainpage.config(height= 1080, width = 1920, highlightbackground= 'white', highlightthickness=10)
F_mainpage.place(relx= 0.5, rely=0.5, anchor = 'center')
# main page image
image1= PhotoImage(file=r"Images/menu page.png")
image1_label = Label(F_mainpage, image = image1,bd=0).pack()
# play button
play_image = PhotoImage(file =r'Images/play button.png')
play_button = Button(F_mainpage, image= play_image, command = openplayb, borderwidth=0, highlightthickness=0 ).place(relx= 0.5, rely=0.515, anchor = 'center')
# quit button
quit_image = PhotoImage(file = r'Images/quit button.png')
quit_button = Button(F_mainpage, image= quit_image, command = pg.destroy, borderwidth=0, highlightthickness=0 ).place(relx= 0.5, rely=0.66, anchor = 'center')
#about button
about_image = PhotoImage(file = r'Images/about button.png')
about_button = Button(F_mainpage, image= about_image, command = about_pg, borderwidth=0, highlightthickness=0 ).place(relx= 0.5, rely=0.79, anchor = 'center')
#-----------Lists-----------#  
    #---------------(periodic table lists)-------------#
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
name_lowered = [
    'hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon',
    'sodium', 'magnesium', 'aluminium', 'silicon', 'phosphorus', 'sulfur', 'chlorine', 'argon', 'potassium', 'calcium',
    'scandium', 'titanium', 'vanadium', 'chromium', 'manganese', 'iron', 'cobalt', 'nickel', 'copper', 'zinc',
    'gallium', 'germanium', 'arsenic', 'selenium', 'bromine', 'krypton', 'rubidium', 'strontium', 'yttrium', 'zirconium',
    'niobium', 'molybdenum', 'technetium', 'ruthenium', 'rhodium', 'palladium', 'silver', 'cadmium', 'indium', 'tin',
    'antimony', 'tellurium', 'iodine', 'xenon', 'cesium', 'barium', 'lanthanum', 'cerium', 'praseodymium', 'neodymium',
    'promethium', 'samarium', 'europium', 'gadolinium', 'terbium', 'dysprosium', 'holmium', 'erbium', 'thulium', 'ytterbium',
    'lutetium', 'hafnium', 'tantalum', 'tungsten', 'rhenium', 'osmium', 'iridium', 'platinum', 'gold', 'mercury',
    'thallium', 'lead', 'bismuth', 'polonium', 'astatine', 'radon', 'francium', 'radium', 'actinium', 'thorium',
    'protactinium', 'uranium', 'neptunium', 'plutonium', 'americium', 'curium', 'berkelium', 'californium', 'einsteinium', 'fermium',
    'mendelevium', 'nobelium', 'lawrencium', 'rutherfordium', 'dubnium', 'seaborgium', 'bohrium', 'hassium', 'meitnerium', 'darmstadtium',
    'roentgenium', 'copernicium', 'nihonium', 'flerovium', 'moscovium', 'livermorium', 'tennessine', 'oganesson'
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
    #--------Extra lists---------#
questions = [
    "What is this element's name?", "What is this element's symbol?", "What is this element's atomic number?",
    "What is this element's group?", "What is this element's period?"
]
valid_topics = ['name', 'symbol', 'atomic number', 'group', 'period']





pg.mainloop()


