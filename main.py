from tkinter import *
from  tkinter import ttk



#colors
co0 = "#ffffff" #white
co1 = "#262624"  #black
co2 = "#ff843d"  #orange
co3 = "#334acc"  
co4 = "#e1e4f2"  #ash

all_values = ""
text_values = StringVar()

def entering_values(number):
   global all_values

   all_values = all_values + str(number)
   text_value.set(all_values)

window = Tk ()
window.title ("Calculator")
window.geometry ('235x318')
window.configure(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_score = Frame(window, width=300, height=56, bg=co1, pady=0, padx=0)
frame_score.grid(row=1, column=0, sticky=NW)

frame_buttons = Frame(window, width=300, height=340, bg=co1, pady=0, padx=0)
frame_buttons.grid(row=2, column=0, sticky=NW)

app_screen = Label(frame_score, width=16, height=2, textvariable=text_value, padx=7, archor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg=co1, fg=co0)
app_screen.place(x=0, y=0)


b_1 = Button(frame_buttons, text="C", command=lambda:clear_screen(), width=11, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_buttons, text="%", command = lambda:entering_values("%"), width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_buttons, text="/", command = lambda:entering_values("/"), width=5, height=2, bg=co2, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_buttons, text="7",  command = lambda:entering_values("7"), width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_buttons, text="8",  command = lambda:entering_values("8"), width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_buttons, text="9", command = lambda:entering_values("9"),  width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_buttons, text="*",  command = lambda:entering_values("*"), width=5, height=2, bg=co2, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_buttons, text="4", command = lambda:entering_values("4"), width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_buttons, text="5",  command = lambda:entering_values("5"), width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_buttons, text="6", command = lambda:entering_values("6"), width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_buttons, text="-", command = lambda:entering_values("-"), width=5, height=2, bg=co2, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_buttons, text="1", command = lambda:entering_values("1"), width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_buttons, text="2", command = lambda:entering_values("2"), width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_buttons, text="3", command = lambda:entering_values("3"), width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_buttons, text="+", command = lambda:entering_values("+"), width=5, height=2, bg=co2, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_buttons, text="0", command = lambda:entering_values("0"),  width=11, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_buttons, text=".",  command = lambda:entering_values("."), width=5, height=2, bg=co4, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_buttons, text="=", command = lambda:calculate(), width=5, height=2, bg=co2, fg=co1, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)









window.mainloop ()