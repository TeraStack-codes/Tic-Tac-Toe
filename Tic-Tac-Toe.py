import tkinter as tk 
from tkinter import *

#Main

root = tk.Tk()
root.geometry('500x500+650+150')
#root.iconbitmap(r'Images\tictactoe_X5c_icon.ico')
root.resizable(0,0)
root.title('Tic-Tac-Toe')   

#Variables

button1var = StringVar()
button2var = StringVar()
button3var = StringVar()
button4var = StringVar()
button5var = StringVar()
button6var = StringVar()
button7var = StringVar()
button8var = StringVar()
button9var = StringVar()
X_score = StringVar()
O_score = StringVar()
X_score.set('0')
O_score.set('0')
small_x_score = 0
small_o_score = 0
times = 'X'
button1var.set('-')
button2var.set('-')
button3var.set('-')
button4var.set('-')
button5var.set('-')
button6var.set('-')
button7var.set('-')
button8var.set('-')
button9var.set('-')



#Functions

def reset():
    global X_score,O_score
    X_score.set('0')
    O_score.set('0')
    clear()

def clear():
    global button1var,button2var,button3var,button4var,button5var,button6var,button7var,button8var,button9var,times
    times = 'X'
    btn_1['state'] = NORMAL
    btn_2['state'] = NORMAL
    btn_3['state'] = NORMAL
    btn_4['state'] = NORMAL
    btn_5['state'] = NORMAL
    btn_6['state'] = NORMAL
    btn_7['state'] = NORMAL
    btn_8['state'] = NORMAL
    btn_9['state'] = NORMAL
    button1var.set('-')
    button2var.set('-')
    button3var.set('-')
    button4var.set('-')
    button5var.set('-')
    button6var.set('-')
    button7var.set('-')
    button8var.set('-')
    button9var.set('-')
    

def checker():
    global button1var,button2var,button3var,button4var,button5var,button6var,button7var,button8var,button9var,small_o_score,small_x_score,X_score,O_score
    
    if button1var.get() == 'X' and button2var.get() == 'X' and button3var.get() == 'X':
        small_x_score = small_x_score + 1
        X_score.set(small_x_score)
        clear()
    
    elif button4var.get() == 'X' and button5var.get() == 'X' and button6var.get() == 'X':
        small_x_score = small_x_score + 1
        X_score.set(small_x_score)
        clear()
    
    elif button7var.get() == 'X' and button8var.get() == 'X' and button9var.get() == 'X':
        small_x_score = small_x_score + 1
        X_score.set(small_x_score)
        clear()
    
    elif button1var.get() == 'X' and button4var.get() == 'X' and button7var.get() == 'X':
        small_x_score = small_x_score + 1
        X_score.set(small_x_score)
        clear()
    
    elif button2var.get() == 'X' and button5var.get() == 'X' and button8var.get() == 'X':
        small_x_score = small_x_score + 1
        X_score.set(small_x_score)
        clear()
    
    elif button3var.get() == 'X' and button6var.get() == 'X' and button9var.get() == 'X':
        small_x_score = small_x_score + 1
        X_score.set(small_x_score)
        clear()
    
    elif button1var.get() == 'X' and button5var.get() == 'X' and button9var.get() == 'X':
        small_x_score = small_x_score + 1
        X_score.set(small_x_score)
        clear()
    
    elif button7var.get() == 'X' and button5var.get() == 'X' and button3var.get() == 'X':
        small_x_score = small_x_score + 1
        X_score.set(small_x_score)
        clear()
    elif button1var.get() == 'O' and button2var.get() == 'O' and button3var.get() == 'O':
        small_o_score = small_o_score + 1
        O_score.set(small_o_score)
        clear()
    
    elif button4var.get() == 'O' and button5var.get() == 'O' and button6var.get() == 'O':
        small_o_score = small_o_score + 1
        O_score.set(small_o_score)
        clear()
    
    elif button7var.get() == 'O' and button8var.get() == 'O' and button9var.get() == 'O':
        small_x_score = small_x_score + 1
        X_score.set(small_x_score)
        clear()
    
    elif button1var.get() == 'O' and button4var.get() == 'O' and button7var.get() == 'O':
        small_o_score = small_o_score + 1
        O_score.set(small_o_score)
        clear()
    
    elif button2var.get() == 'O' and button5var.get() == 'O' and button8var.get() == 'O':
        small_o_score = small_o_score + 1
        O_score.set(small_o_score)
        clear()
    
    elif button3var.get() == 'O' and button6var.get() == 'O' and button9var.get() == 'O':
        small_o_score = small_o_score + 1
        O_score.set(small_o_score)
        clear()
    
    elif button1var.get() == 'O' and button5var.get() == 'O' and button9var.get() == 'O':
        small_o_score = small_o_score + 1
        O_score.set(small_o_score)
        clear()
    
    elif button7var.get() == 'O' and button5var.get() == 'O' and button3var.get() == 'O':
        small_o_score = small_o_score + 1
        O_score.set(small_o_score)
        clear()
    
    elif btn_1['state'] == DISABLED and btn_2['state'] == DISABLED and btn_3['state'] == DISABLED and btn_4['state'] == DISABLED and btn_5['state'] == DISABLED and btn_6['state'] == DISABLED and btn_7['state'] == DISABLED and btn_8['state'] == DISABLED and btn_9['state'] == DISABLED : 
        clear()
    

def Button1clicked():
    global button1var,times
    if times == 'X':
        button1var.set('X')
        times = 'O'
        btn_1['state'] = DISABLED
        checker()
    elif times == 'O':
        button1var.set('O')
        times = 'X'
        btn_1['state'] = DISABLED
        checker()
 
def Button2clicked():
    global button2var,times
    if times == 'X':
        button2var.set('X')
        times = 'O'
        btn_2['state'] = DISABLED
        checker()
    elif times == 'O':
        button2var.set('O')
        times = 'X'
        btn_2['state'] = DISABLED
        checker()
 
def Button3clicked():
    global button3var,times
    if times == 'X':
        button3var.set('X')
        times = 'O'
        btn_3['state'] = DISABLED
        checker()
    elif times == 'O':
        button3var.set('O')
        times = 'X'
        btn_3['state'] = DISABLED
        checker()
 
def Button4clicked():
    global button4var,times
    if times == 'X':
        button4var.set('X')
        times = 'O'
        btn_4['state'] = DISABLED
        checker()
    elif times == 'O':
        button4var.set('O')
        times = 'X'
        btn_4['state'] = DISABLED
        checker()
 
def Button5clicked():
    global button5var,times
    if times == 'X':
        button5var.set('X')
        times = 'O'
        btn_5['state'] = DISABLED
        checker()
    elif times == 'O':
        button5var.set('O')
        times = 'X'
        btn_5['state'] = DISABLED
        checker()
 
def Button6clicked():
    global button6var,times
    if times == 'X':
        button6var.set('X')
        times = 'O'
        btn_6['state'] = DISABLED
        checker()
    elif times == 'O':
        button6var.set('O')
        times = 'X'
        btn_6['state'] = DISABLED
        checker()
 
def Button7clicked():
    global button7var,times
    if times == 'X':
        button7var.set('X')
        times = 'O'
        btn_7['state'] = DISABLED
        checker()
    elif times == 'O':
        button7var.set('O')
        times = 'X'
        btn_7['state'] = DISABLED
        checker()
 
def Button8clicked():
    global button8var,times
    if times == 'X':
        button8var.set('X')
        times = 'O'
        btn_8['state'] = DISABLED
        checker()
    elif times == 'O':
        button8var.set('O')
        times = 'X'
        btn_8['state'] = DISABLED
        checker()
 
def Button9clicked():
    global button9var,times
    if times == 'X':
        button9var.set('X')
        times = 'O'
        btn_9['state'] = DISABLED
        checker()
    elif times == 'O':
        button9var.set('O')
        times = 'X'
        btn_9['state'] = DISABLED
        checker()
 

#Frames

btnrow1 = Frame(root,bg = '#000000')
btnrow1.pack(expand = True, fill = 'both')

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = 'both')

btnrow3 = Frame(root,bg = '#000000')
btnrow3.pack(expand = True, fill = 'both')

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = 'both')

btnrow5 = Frame(root)
btnrow5.pack(expand = True, fill = 'both')

#Row 1

btn_1 = Button(
    btnrow1,
    textvariable = button1var,
    font = ('Verdana', 22),
    relief = SUNKEN,
    border = 5 ,
    command = Button1clicked
)
btn_1.pack(side = LEFT, expand = True,fill='both')
btn_2 = Button(
    btnrow1,
    textvariable = button2var,
    font = ('Verdana', 22),
    relief = SUNKEN,
    border = 5 ,
    command = Button2clicked
)
btn_2.pack(side = LEFT, expand = True,fill='both')
btn_3 = Button(
    btnrow1,
    textvariable = button3var,
    font = ('Verdana', 22),
    relief = SUNKEN,
    border = 5 ,
    command = Button3clicked
)
btn_3.pack(side = LEFT, expand = True,fill='both')

#Row 2

btn_4 = Button(
    btnrow2,
    textvariable = button4var,
    font = ('Verdana', 22),
    relief = SUNKEN,
    border = 5 ,
    command = Button4clicked 
)
btn_4.pack(side = LEFT, expand = True,fill='both')
btn_5 = Button(
    btnrow2,
    textvariable = button5var,
    font = ('Verdana', 22),
    relief = SUNKEN,
    border = 5 ,
    command = Button5clicked
)
btn_5.pack(side = LEFT, expand = True,fill='both')

btn_6 = Button(
    btnrow2,
    textvariable = button6var,
    font = ('Verdana', 22),
    relief = SUNKEN,
    border = 5 ,
    command = Button6clicked
)
btn_6.pack(side = LEFT, expand = True,fill='both')

#Row 3

btn_7 = Button(
    btnrow3,
    textvariable = button7var,
    font = ('Verdana', 22),
    relief = SUNKEN,
    border = 5 ,
    command = Button7clicked
)
btn_7.pack(side = LEFT, expand = True,fill='both')
btn_8 = Button(
    btnrow3,
    textvariable = button8var,
    font = ('Verdana', 22),
    relief = SUNKEN,
    border = 5 ,
    command = Button8clicked
)
btn_8.pack(side = LEFT, expand = True,fill='both')
btn_9 = Button(
    btnrow3,
    textvariable = button9var,
    font = ('Verdana', 22),
    relief = SUNKEN,
    border = 5 ,
    command = Button9clicked
)
btn_9.pack(side = LEFT, expand = True,fill='both')

#Scores

X_text = Label(btnrow4,
    text = 'X',
    background = '#ffffff',
    fg = 'Red',
    font = ('Verdana', 22)
)
X_text.pack(expand = True, fill = 'both')

x_score_label = Label(btnrow4,
    textvariable = X_score,
    background = 'Red',
    fg = '#ffffff',
    font = ('Verenda',22) 
    )
x_score_label.pack(expand = True, fill = 'both')

O_text = Label(btnrow5,
    text = 'O',
    background = '#ffffff',
    fg = 'Blue',
    font = ('Verdana', 22)
)
O_text.pack(expand = True, fill = 'both')

O_score_label = Label(btnrow5,
    textvariable = O_score,
    background = 'Blue',
    fg = '#ffffff',
    font = ('Verenda',22) 
    )
O_score_label.pack(expand = True, fill = 'both')

#Reset button

Clear_button = Button(
    btnrow5,
    text = 'Clear',
    font = ('Verdana', 22),
    relief = RAISED,
    border = 5 ,
    command = clear
)
Clear_button.pack(side = LEFT, expand = True,fill='both')

Reset_button = Button(
    btnrow5,
    text = 'Reset',
    font = ('Verdana', 22),
    relief = RAISED,
    border = 5 ,
    command = reset
)
Reset_button.pack(side = LEFT, expand = True,fill='both')

root.mainloop()